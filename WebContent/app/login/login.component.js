app.controller("LoginController", function(DevShareService) {
    this.data = {};
	this.processando = false;

    this.save = function() {
        this.processando = true;
        DevShareService.objRest.one('/login').customPOST(this.data)
        .then(() => {

        }).finally(() => {
            this.processando = false;
        });
    }
});