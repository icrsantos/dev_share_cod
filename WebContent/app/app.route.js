app.config(['$stateProvider', function($stateProvider) {
	$stateProvider.state('home', {
        url : '',
    	views : {
    		'uiViewHeader' : {
                templateUrl : 'header/Header.html'
            },'uiViewCarousel' : {
                templateUrl : 'home/Carousel.html'
            }, 'uiViewContent' : {
                templateUrl : 'home/Home.html'
            }
        },
        ncyBreadcrumb: {
            skip: true
        }
    });
    
    $stateProvider.state('signup', {
        url : '/signup',
    	views : {
    		'uiViewLoginSignup' : {
                templateUrl : 'signup/SignUp.html'
            }
        },
        ncyBreadcrumb: {
            skip: true
        }
    });
    
    $stateProvider.state('login', {
        url : '/login',
    	views : {
    		'uiViewLoginSignup' : {
                templateUrl : 'login/login.component.html'
            }
        },
        ncyBreadcrumb: {
            skip: true
        }
    });

    $stateProvider.state('posts', {
        url : '/posts/:search',
    	views : {
    		'uiViewHeader' : {
                templateUrl : 'header/Header.html'
            }, 'uiViewContent' : {
                templateUrl : 'posts/Posts.html'
            }
        },
        ncyBreadcrumb: {
            skip: true
        }
    });

    $stateProvider.state('logout', {
        url : '/logout',
        views : {
            'uiViewContent@' : {
                controller: 'LogoutController',
                template: "<div ui-view></div>"
            }
        }
    });

}]);
