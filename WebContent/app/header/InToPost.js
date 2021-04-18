app.controller("PostsController", function($stateParams, DevShareService) {
	this.pesquisa = $stateParams.search;
	this.buscar = function() {
        DevShareService.objRest.one('/pesquisar/' + this.pesquisa).get()
        .then((response) => {
            this.retornoPesquisa = response.data;
            return response;
        })
	}

	this.retornoPesquisa = ['Não foi encontrado nenhum resultado'];
	this.buscar()
})