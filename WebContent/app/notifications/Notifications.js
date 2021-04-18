app.component('notifications', {
    bindings: {},
    templateUrl: 'notifications/Notifications.html',
    controllerAs: 'notificationsCtrl',
    controller: function($scope, DevShareService, Auth) {
        this.notifications;
        this.user = Auth.getUser();

        this.$onInit = () => {
            if(this.user && (!this.notifications || $scope.newNotifications)) {
                DevShareService.objRest.one('/notifications/' + this.user.id).get()
                .then((response) => {
                    this.notifications = response.data;
                });
            }
        }

        this.closeModal = () => {

        }
    }

})