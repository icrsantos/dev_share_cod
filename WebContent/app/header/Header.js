app.controller("HeaderController", function(Auth, $rootScope) {
    this.user = Auth.getUser();
    this.newNotifications = $rootScope.newNotifications;

    setInterval(angular.bind(this, function() {
        this.newNotifications = $rootScope.newNotifications;
    }), 1000 * 61);
})