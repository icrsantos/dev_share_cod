app.config(['$stateProvider', function($stateProvider) {
	$stateProvider.state('home', {
        url : '',
    	views : {
    		'uiViewHeader' : {
                templateUrl : 'app/header/Header.html'
            },'uiViewCarousel' : {
                templateUrl : 'app/home/Carousel.html'
            }, 'uiViewContent' : {
                templateUrl : 'app/home/Home.html'
            }
        },
        ncyBreadcrumb: {
            skip: true
        }
    });
    
    $stateProvider.state('signup', {
        url : '/signup',
    	views : {
    		'uiViewHeader' : {
                templateUrl : 'app/header/Header.html'
            }, 'uiViewContent' : {
                templateUrl : 'app/signup/SignUp.html'
            }
        },
        ncyBreadcrumb: {
            skip: true
        }
    });

}]);
