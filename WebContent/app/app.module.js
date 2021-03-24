var app = angular.module('dev_share', ['restangular', 'LocalStorageModule', 'ui.router'])
    .config(['RestangularProvider', 'localStorageServiceProvider', 
        function (RestangularProvider, localStorageServiceProvider) {
        
        var apiUrl = 'http://127.0.0.1:5000/api';
        RestangularProvider.setBaseUrl(apiUrl);
        RestangularProvider.setDefaultHeaders({'Content-Type': 'application/json; charset=utf-8'});
        RestangularProvider.setDefaultHttpFields({withCredentials: true})
        
        localStorageServiceProvider
        .setPrefix('dev-share')
        .setStorageType('sessionStorage');
    }]);

window.app = app;