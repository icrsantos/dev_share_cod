app.controller("PostsController", function($stateParams, DevShareService, Auth) {
	this.pesquisa = $stateParams.search;
	this.retornoPesquisa = false;
	this.user = Auth.getUser();

	this.$onInit = () => {
	    let nomeRequisicao = (this.pesquisa != null)
	        ? '/pesquisar/' + this.pesquisa : '/postagem';

        DevShareService.objRest.one(nomeRequisicao).get()
        .then((response) => {
            this.retornoPesquisa = response.data;
        })
	}

	this.criarPost = function() {
        $('#createPostModal').modal('show');
    }
})