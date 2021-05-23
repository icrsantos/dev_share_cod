app.controller("PostController", function ($stateParams, DevShareService, Auth, $rootScope) {

    this.user = Auth.getUser();
    this.post = null;
    this.retornoRespostas = null;

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
                this.defineScoringButtonStatus();
                this.defineEchoButtonStatus($stateParams.id);
            });

    }

    this.giveLike = function (postId) {
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
        }
    }

    this.giveDislike = function (postId) {
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
            let scoreButtons = document.getElementsByClassName('btn-link')
            for (let i = 0; i < scoreButtons.length; i++) {
                let id = scoreButtons[i].id
                    .replace("button-like-", "")
                    .replace("button-dislike-", "");
                DevShareService.objRest.one('/postagem/jaAvaliada/' + this.user.id + '/' + id).get()
                    .then((response) => {
                        let operation = response.data;
                        if (operation === "LIKE") {
                            document.getElementById('button-dislike-' + id).disabled = true;
                        } else if (operation === 'DISLIKE') {
                            document.getElementById('button-like-' + id).disabled = true;
                        }
                    });
            }
        }
    }

    this.defineEchoButtonStatus = function (postId) {
        if (this.user) {
            DevShareService.objRest.one('/postagem/ecoExiste/' + this.user.id + '/' + postId).get()
                .then((response) => {
                    let alreadyEchoed = response.data;
                    if (alreadyEchoed === "True") {
                        this.echoButtonAlreadyUsed();
                    }
                });
        }
    }

    this.echoPost = function (postId) {
        if (this.user) {
            DevShareService.objRest.one('/postagem/ecoExiste/' + this.user.id + '/' + postId).get()
                .then((response) => {
                    let alreadyEchoed = response.data;
                    if (alreadyEchoed === "True") {
                        DevShareService.objRest.one('/postagem/removerEco/' + this.user.id + '/' + postId).post()
                            .finally(() => {
                                window.location.reload();
                            });
                    }
                    else{
                        DevShareService.objRest.one('/postagem/ecoar/' + this.user.id + '/' + postId).post()
                            .finally(() => {
                                window.location.reload();
                            });
                    }
                });

        }
    }

    this.echoButtonAlreadyUsed = function () {
        document.getElementById("button-echo-question").innerHTML = '<i class="fa fa-check"></i>';
        document.getElementById("button-echo-question").title = 'Postagem Ecoada!';
    }
})