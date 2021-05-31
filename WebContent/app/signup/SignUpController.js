app.controller('SignUpController', function($rootScope, DevShareService, $state) {
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

	this.save = function() {
		this.processando = true;
        DevShareService.objRest.one('/usuario').customPOST(this.data)
        .then((response) => {
            $state.go("home");
        }).finally(() => {
            this.processando = false;
        });
	}
	
});