app.controller("ProfileController", function(Auth, DevShareService) {
    this.user = Auth.getUser();
    this.processando = false;
    this.profileQuestions;
    this.profileReply;

    this.$onInit = () => {
        if(!this.profileQuestions) {
            DevShareService.objRest.one('/postagem/usuario/' + this.user.id + '/perguntas').get()
            .then((response) => {
                this.profileQuestions = response.data;
            }).finally(() => {
                if(!this.profileReply) {
                    DevShareService.objRest.one('/postagem/usuario/' + this.user.id + '/respostas').get()
                    .then((response) => {
                        this.profileReply = response.data;
                    })
                }
            })
        }
    };

    this.salvarEdicaoUsuario = function() {
        this.processando = true;
        DevShareService.objRest.one('/usuario').customPOST(this.user)
        .then((response) => {
            $('#editUserModal').modal('hide');
        }).finally(() => {
            this.processando = false;
        });
    }
})