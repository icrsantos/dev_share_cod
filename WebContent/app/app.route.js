app.config(['$stateProvider', function($stateProvider) {
	$stateProvider.state('home', {
        url : '',
    	views : {
    		'uiViewHeader' : {
                templateUrl : 'header/Header.html'
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
                templateUrl : 'login/login.html'
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

    $stateProvider.state('post', {
        url : '/posts/:id',
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

    $stateProvider.state('profile', {
        url : '/profile',
    	views : {
    		'uiViewHeader' : {
                templateUrl : 'header/Header.html'
            }, 'uiViewContent' : {
                templateUrl : 'profile/Profile.html'
            }, 'uiViewPostsProfile@profile' : {
                templateUrl: 'profile/ProfileQuestions.html'
            }
        },
        ncyBreadcrumb: {
            skip: true
        }
    });

    $stateProvider.state('profile.respostas', {
        url : '/respostas',
    	views : {
    		'uiViewPostsProfile@profile' : {
                templateUrl: 'profile/ProfileReply.html'
            }
        },
        ncyBreadcrumb: {
            skip: true
        }
    });
}]);
