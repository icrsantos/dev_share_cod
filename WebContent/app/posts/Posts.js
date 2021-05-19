app.controller("PostsController", function($stateParams, DevShareService) {
	this.pesquisa = $stateParams.search;
	this.buscar = function() {
	    let nomeRequisicao = (this.pesquisa != null)
	        ? '/pesquisar/' + this.pesquisa : '/postagem';

        DevShareService.objRest.one(nomeRequisicao).get()
        .then((response) => {
            this.retornoPesquisa = response.data;
        })
	}

	this.retornoPesquisa = ['Não foi encontrado nenhum resultado'];
	this.buscar()

	this.criarPost = function() {
        $('#cadastrarPostModal').modal('show');
    }
})