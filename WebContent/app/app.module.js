var app = angular.module('dev_share', ['restangular', 'LocalStorageModule', 'ui.router'])
    .config(['RestangularProvider', 'localStorageServiceProvider', 
        function (RestangularProvider, localStorageServiceProvider) {
        
        var apiUrl = window.location.pathname + 'api/v1';
        RestangularProvider.setBaseUrl(apiUrl);
        RestangularProvider.setDefaultHeaders({'Content-Type': 'application/json; charset=utf-8'});
        RestangularProvider.setDefaultHttpFields({withCredentials: true})
        
        localStorageServiceProvider
        .setPrefix('dev-share')
        .setStorageType('sessionStorage');
    }]);

window.app = app;