app.controller("ProfileController", function(Auth, ModalService, DevShareService) {
    this.user = Auth.getUser();
    this.processando = false;
    this.profileQuestions;
    this.profileReply;

    this.$onInit = () => {
        DevShareService.objRest.one('/postagem/usuario/' + this.user.id + '/perguntas').get()
        .then((response) => {
            this.profileQuestions = response.data;
        })

        DevShareService.objRest.one('/postagem/usuario/' + this.user.id + '/respostas').get()
        .then((response) => {
            this.profileReply = response.data;
        })
    };

    this.editProfile = function() {
        ModalService.open($('#editUserModal').modal("show"), {
            templateUrl: 'app/profile/EditProfile.modal.html',
            controller: 'AlteracaoStatusController as alteracaoStatusCtrl',
        });
    }

    this.salvarEdicaoUsuario = function() {

    }
})