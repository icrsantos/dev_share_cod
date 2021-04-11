app.factory('ModalService', function() {
    return {
        open : function(modal, options) {
            if (this.modal) {
                this.modal.close('close-modal');
            }

            modal.open(options);
        },

        dismiss : function(modal) {
            if (this.modal) {
                this.modal.dismiss('close-modal');
            }
        }
    };
});
