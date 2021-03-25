var app = angular.module('dev_share', ['restangular', 'LocalStorageModule', 'ui.router'])
    .config(['RestangularProvider', 'localStorageServiceProvider', '$qProvider',
        function (RestangularProvider, localStorageServiceProvider, $qProvider) {

        var apiUrl = 'http://127.0.0.1:5000/api';
        RestangularProvider.setBaseUrl(apiUrl);
        RestangularProvider.setDefaultHeaders({
            'Content-Type': 'application/json; charset=utf-8',
            'X-Requested-With': 'XMLHttpRequest'
        });
        RestangularProvider.setDefaultHttpFields({ withCredentials: true })

        $qProvider.errorOnUnhandledRejections(false);
    }]);

window.app = app;