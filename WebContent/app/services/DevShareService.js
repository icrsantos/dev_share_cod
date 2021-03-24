app.factory('DevShareService', function(Restangular) {
    var service = {
        objRest: Restangular.withConfig(function(RestangularConfigurer) {
            RestangularConfigurer.setFullResponse(true);
        })
    };

    return service;
})