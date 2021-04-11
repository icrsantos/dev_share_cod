app.controller("ProfileController", function(Auth, ModalService) {
    this.user = Auth.getUser();

    this.editProfile = function() {
        ModalService.open($('#editUserModal').modal(), {
            templateUrl: 'app/profile/EditProfile.modal.html',
            controller: 'AlteracaoStatusController as alteracaoStatusCtrl',
        });
    }
})