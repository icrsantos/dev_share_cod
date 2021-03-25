app.controller("HeaderController", function($stateParams, DevShareService) {
	this.pesquisa;

	this.buscar = function() {
        DevShareService.objRest.one('/pesquisar/' + this.pesquisa).get()
        .then((response) => {
            return response;
        })
	}
})