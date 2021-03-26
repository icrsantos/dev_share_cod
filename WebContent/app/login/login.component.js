app.controller("LoginController", function(DevShareService, $state) {
    this.data = {};
	this.processando = false;

    this.save = function() {
        this.processando = true;
        DevShareService.objRest.one('/login').customPOST(this.data)
        .then((response) => {
            $state.go("home");
        }).finally(() => {
            this.processando = false;
        });
    }
});