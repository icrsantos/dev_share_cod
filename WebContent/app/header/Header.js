app.controller("HeaderController", function($stateParams, DevShareService, Auth, $state) {
    this.user = Auth.getUser();
})