app.component('criar_postagem', {
    bindings: {},
    templateUrl: 'posts/CadastrarPost.html',
    controllerAs: 'criarCtrl',
    controller: function($scope, Auth) {
        this.post = {};
        this.notifications;
        this.user = Auth.getUser();

        this.$onInit = () => {
            this.post.usuario_id = this.user.id;
            this.post.nome_autor = this.user.nome;
        }

        this.closeModal = () => {
            $('#cadastrarPostModal').modal('hide');
            this.post = {};
        }
    }
})