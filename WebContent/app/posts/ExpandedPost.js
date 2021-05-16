app.controller("PostController", function($stateParams, DevShareService, Auth) {

    this.user = Auth.getUser();
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

	this.giveLike = function (postId){
	    if(this.user){
	        DevShareService.objRest.one('/postagem/like/' + this.user.id + '/' + postId).post()
        }
    }

    this.giveDislike = function (postId){
	    if(this.user){
	        DevShareService.objRest.one('/postagem/dislike/' + this.user.id + '/' + postId).post()
        }
    }
})