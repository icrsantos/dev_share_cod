app.controller("LoginController", function (DevShareService, $state, Auth, $rootScope) {
    this.data = {};
    this.processando = false;

    this.$onInit = () => {
        gapi.signin2.render('loginGmail', {
            'scope': 'email profile https://www.googleapis.com/auth/plus.login', // solicitando acesso ao profile e ao e-mail do usuário
            'width': 200,
            'height': 30,
            'longtitle': true,
            'theme': 'dark',
            'onsuccess': onSignIn,
        });
    }

    this.save = function () {
        this.processando = true;
        DevShareService.objRest.one('/login').customPOST(this.data)
            .then((response) => {
                if (response.data && response.data !== 'False') {
                    Auth.setUser(response.data);
                    $state.go("home");
                }
            })
            .finally(() => {
                this.processando = false;
            });
    }
});