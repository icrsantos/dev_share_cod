app.config(['$stateProvider', function($stateProvider) {
	$stateProvider.state('home', {
        url : '',
    	views : {
            'uiViewContent' : {
                templateUrl : 'app/home/Home.html'
            }
        },
        ncyBreadcrumb: {
            skip: true
        }
    });

}]);
