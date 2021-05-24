app.controller("LoginController", function (DevShareService, $state, Auth) {
    this.data = {};
    this.processando = false;

    this.save = function () {
        this.processando = true;
        DevShareService.objRest.one('/login').customPOST(this.data)
            .then((response) => {
                if (response.data !== 'False') {
                    Auth.setUser(response.data);
                    $state.go("home");
                }
            })
            .finally(() => {
                this.processando = false;
            });
    }
});