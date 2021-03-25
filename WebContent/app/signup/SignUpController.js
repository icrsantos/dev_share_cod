app.controller('SignUpController', function($rootScope, DevShareService) {
	this.data = {};
	this.processando = false;
	
	this.save = function() {
		this.processando = true;
        DevShareService.one('/usuario').customPOST(this.data)
        .then(() => {

        }).finally(() => {
            this.processando = false;
        });
	}
	
});