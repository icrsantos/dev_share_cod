app.controller("HeaderController", function(Auth, $rootScope, Restangular, $state) {
    this.user = Auth.getUser();

    this.$onInit = () => {
        if(this.user) {
            setInterval(angular.bind(this, function() {
                this.newNotifications = $rootScope.newNotifications;
            }), 100 * 61);

            if($rootScope.newNotifications) {
                this.newNotifications = $rootScope.newNotifications;
            } else {
                Restangular.one('/new-notifications/' + Auth.getUser().id).get()
                .then(angular.bind(this, function(response) {
                    if(response && response > 0) {
                        this.newNotifications = response;
                        $rootScope.newNotifications = response;
                    }
                }));
            }
        }
    }

    this.openModalNotifications = function() {
        this.newNotifications = null;
        $rootScope.newNotifications = null;

        $('#notificationsModal').modal('show');
    }

    this.goSearch = function() {
        $state.go("posts", {search: this.pesquisa});
    }
})