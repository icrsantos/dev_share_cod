app.controller("PostController", function ($stateParams, DevShareService, Auth, $rootScope) {

    this.user = Auth.getUser();
    this.post = null;
    this.retornoRespostas = null;

    this.$onInit = async function (){
        let response = DevShareService.objRest.one('/postagem/' + $stateParams.id).get()
            .then((response) => {
                this.post = response.data;
            })
            .finally(async () =>{
                await DevShareService.objRest.one('/postagem/respostas/' + $stateParams.id).get()
                    .then((response) => {
                        this.retornoRespostas = response.data;
                    });
                this.defineScoringButtonStatus();
            });

    }

    this.giveLike = function (postId) {
        if (this.user) {
            DevShareService.objRest.one('/postagem/like/' + this.user.id + '/' + postId).post()
                .finally(() => {
                    window.location.reload();
                });
        }
    }

    this.giveDislike = function (postId) {
        if (this.user) {
            DevShareService.objRest.one('/postagem/dislike/' + this.user.id + '/' + postId).post()
                .finally(() => {
                    window.location.reload();
                });
        }
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
                    scoreButtons[i].disabled =  response.data === "True";
                });
            }
        }
    }
})