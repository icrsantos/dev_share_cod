app.controller("PostsController", function($stateParams, DevShareService) {
	this.pesquisa = $stateParams.search;
	this.retornoPesquisa = ['iAmOK!', 'I am also OK!'];

	this.buscar = function() {
        DevShareService.objRest.one('/pesquisar/' + this.pesquisa).get()
        .then((response) => {
            this.retornoPesquisa = response.data;
            return response;
        })
	}
})