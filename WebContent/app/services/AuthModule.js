app.factory('Auth', ['Restangular', 'localStorageService',
    function(Restangular, localStorageService) {

        var auth = {
            currentUser: null,

            hasUser: function() {
                var user = auth.getUser();
                return !_.isUndefined(user) && user != null;
            },

            setUser: function(user) {
                if (localStorageService.isSupported) {
                    if (user == null) {
                        localStorageService.remove('user');
                    } else {
                        localStorageService.set('user', user);
                    }
                } else {
                    auth.currentUser = user;
                }
            },

            getUser: function() {
                return (localStorageService.isSupported)
                    ? localStorageService.get('user')
                    : auth.currentUser;
            },
        };

        return auth;
    }
])