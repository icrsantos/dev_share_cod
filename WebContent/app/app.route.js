app.config(['$stateProvider', function($stateProvider) {
	$stateProvider.state('home', {
        url : 'teste',
        views : {
            'uiViewContent' : {
                templateUrl : 'app/Login/login.component.html'
            }
        }, ncyBreadcrumb: {
            skip: true
        }
    });

}]);
