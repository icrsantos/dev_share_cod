app.controller("PostController", function ($stateParams, DevShareService, Auth, $state) {

    this.user = Auth.getUser();
    this.post = null;
    this.retornoRespostas = null;
    this.alreadyEchoed = null;
    this.respondedPostId = null;

    this.$onInit = async function () {
        DevShareService.objRest.one('/postagem/' + $stateParams.id).get()
            .then((response) => {
                this.post = response.data;
            })
            .finally(async () => {
                await DevShareService.objRest.one('/postagem/respostas/' + $stateParams.id).get()
                    .then((response) => {
                        this.retornoRespostas = response.data;
                    });
                await DevShareService.objRest.one('/postagem/ecoExiste/' + this.user.id + '/' + $stateParams.id).get()
                    .then((response) => {
                        this.alreadyEchoed = response.data === "True";
                    });
                this.defineScoringButtonStatus();
            });
    }

    this.giveLike = function (postId) {
        this.likeButtonLoading(postId);
        if (this.user) {
            DevShareService.objRest.one('/postagem/jaAvaliada/' + this.user.id + '/' + postId).get()
                .then((response) => {
                    let operation = response.data;
                    if (operation === "LIKE") {
                        this.removeUserScoring(postId);
                    } else {
                        DevShareService.objRest.one('/postagem/like/' + this.user.id + '/' + postId).post()
                            .finally(() => {
                                window.location.reload();
                            });
                    }
                });
        } else {
            $state.go("login");
        }
    }

    this.giveDislike = function (postId) {
        this.dislikeButtonLoading(postId);
        if (this.user) {
            DevShareService.objRest.one('/postagem/jaAvaliada/' + this.user.id + '/' + postId).get()
                .then((response) => {
                    let operation = response.data;
                    if (operation === "DISLIKE") {
                        this.removeUserScoring(postId);
                    } else {
                        DevShareService.objRest.one('/postagem/dislike/' + this.user.id + '/' + postId).post()
                            .finally(() => {
                                window.location.reload();
                            });
                    }
                });
        } else {
            $state.go("login");
        }
    }

    this.removeUserScoring = function (postId) {
        DevShareService.objRest.one('/postagem/removerCurtida/' + this.user.id + '/' + postId).post()
            .finally(() => {
                window.location.reload();
            });
    }

    this.defineScoringButtonStatus = function () {
        if (this.user) {
            let scoreButtons = document.getElementsByClassName('btn-link');
            for (let i = 0; i < scoreButtons.length; i++) {
                let id = scoreButtons[i].id
                    .replace("button-like-", "")
                    .replace("button-dislike-", "");
                DevShareService.objRest.one('/postagem/jaAvaliada/' + this.user.id + '/' + id).get()
                    .then((response) => {
                        let operation = response.data;
                        if (operation === "LIKE") {
                            $('#button-dislike-' + id).prop('disabled', true);
                        } else if (operation === 'DISLIKE') {
                            $('#button-like-' + id).prop('disabled', true);
                        }
                    });
            }
        } else {
            $state.go("login");
        }
    }

    this.echoPost = function (postId) {
        this.echoButtonLoading();
        if (this.user) {
            if (this.alreadyEchoed) {
                DevShareService.objRest.one('/postagem/removerEco/' + this.user.id + '/' + postId).post()
                    .finally(() => {
                        window.location.reload();
                    });
            } else {
                DevShareService.objRest.one('/postagem/ecoar/' + this.user.id + '/' + postId).post()
                    .finally(() => {
                        window.location.reload();
                    });
            }
        } else {
            $state.go("login");
        }
    }

    this.respondPost = function (postId) {
        $('#responded-post-id').val(postId);
        $('#createPostModal').modal('show');
    }

    this.likeButtonLoading = function (id) {
        let botao = $('#button-like-' + id);
        botao.html("<div class='spinner-border spinner-border-sm text-light' role='status'>\n" +
            "  <span class='sr-only'>Loading...</span>\n" +
            "</div>");
        botao.prop('disabled', true);
    }

    this.dislikeButtonLoading = function (id) {
        let botao = $('#button-dislike-' + id);
        botao.html("<div class='spinner-border spinner-border-sm text-light' role='status'>\n" +
            "  <span class='sr-only'>Loading...</span>\n" +
            "</div>");
        botao.prop('disabled', true);
    }

    this.echoButtonLoading = function () {
        let botao = $('#button-echo-question');
        botao.html("<div class='spinner-border spinner-border-sm text-light' role='status'>\n" +
            "  <span class='sr-only'>Loading...</span>\n" +
            "</div>");
        botao.prop('disabled', true);
    }

})