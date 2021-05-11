var app = angular.module('dev_share', ['restangular', 'LocalStorageModule', 'ui.router'])
    .config(['RestangularProvider', 'localStorageServiceProvider', '$qProvider',
        function (RestangularProvider, localStorageServiceProvider, $qProvider) {

        var apiUrl = 'http://127.0.0.1:5000/api';
        RestangularProvider.setBaseUrl(apiUrl);
        RestangularProvider.setDefaultHeaders({ 'Content-Type': 'application/json; charset=utf-8' });
        RestangularProvider.setDefaultHttpFields({ withCredentials: true })

        $qProvider.errorOnUnhandledRejections(false);
    }]);

app.run(function($rootScope, Restangular, Auth, $state) {
    $rootScope.invalid = function(form, field) {
        return field && field.$invalid && (field.$dirty || form.$submitted);
    };

    $rootScope.assertStateName = function(name) {
        return  $state.$current.name == name;
    };

    setInterval(function() {
        if(Auth.getUser()) {
            Restangular.one('/new-notifications/' + Auth.getUser().id).get()
            .then(angular.bind(this, function(response) {
                if(response && response > 0)
                    $rootScope.newNotifications = response;
            }));
        }
    }, 1000 * 60);
})
window.app = app;