app.component('createpost', {
    bindings: {},
    templateUrl: 'posts/CreatePost.html',
    controllerAs: 'createCtrl',
    controller: function ($scope, Auth, DevShareService, $state) {
        this.post = {};
        this.processando = false;
        this.user = Auth.getUser();

        this.$onInit = () => {
            if (this.user) {
                this.post.usuarioId = this.user.id;
                this.post.tipo = "PERGUNTA"
                this.post.relevancia = 0;
                this.post.curtidas = 0;
            }
        }

        this.closeModal = () => {
            $('#createPostModal').modal('hide');
            this.post = {};
        }

        this.savePost = () => {
            if (this.isResponseForm()) {
                this.post.titulo = "resposta:"
                this.post.tipo = "RESPOSTA";
                this.post.postagemRespondidaId = $('#responded-post-id').val();
            }
            this.processando = true;
            DevShareService.objRest.one('/postagem').customPOST(this.post)
                .then((response) => {
                    $('#createPostModal').modal('hide');
                    $state.go("post", {id: response.data});
                }).finally(() => {
                this.processando = false;
            });
        }

        this.isResponseForm = function () {
            this.respondedPostId = $('#responded-post-id').val();
            return !!this.respondedPostId;
        }
    }
})