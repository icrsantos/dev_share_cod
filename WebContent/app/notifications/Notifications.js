app.component('notifications', {
    bindings: {},
    templateUrl: 'notifications/Notifications.html',
    controllerAs: 'notificationsCtrl',
    controller: function($scope, DevShareService, Auth, $state) {
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
            $('#notificationsModal').modal('hide');
            DevShareService.objRest.one('/clean-notifications/' + this.user.id).get()
            .then((response) => {
                this.notifications = response.data;
            });
        }

        this.goToPost = (postagem_id) => {
            this.closeModal();
            $state.go("post", {id: postagem_id });
        }

        this.getDataFormatadaNotificacao = (data) => {
            return moment(data, "YYYY-MM-DD HH:mm:ss").format("DD/MM/YYYY HH:mm");
        }
    }

})