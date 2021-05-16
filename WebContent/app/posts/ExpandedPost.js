app.controller("PostController", function($stateParams, DevShareService) {

	this.post = null;
	this.retornoRespostas = null;

	this.$onInit = () => {
	    DevShareService.objRest.one('/postagem/' + $stateParams.id).get()
        .then((response) => {
            this.post = response.data;
        })
        .finally(()=>{
            DevShareService.objRest.one('/postagem/respostas/' + $stateParams.id).get()
            .then((response) => {
                this.retornoRespostas = response.data;
            })
        })
	}
})