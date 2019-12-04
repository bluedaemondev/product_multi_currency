odoo.define('product_multi_currency.models', function (require) {
"use strict";
var models = require('point_of_sale.models');

var _t = core._t;
//Define field
var model_list = models.PosModel.prototype.models;

for(var i = 0; i < model_list.length; i++){
    if(model_list[i].model == 'product.product'){
        var order_model = model_list[i];
        order_model.fields.push('currency_id');
        
        order_model.loaded = function(self, products){
            self.db.add_products(_.map(products, function (product) {
                debugger;
                product.lst_price = round_pr(product.lst_price * product.currency_id.rate, self.currency.rounding);
                product.categ = _.findWhere(self.product_categories, {'id': product.categ_id[0]});
                return new exports.Product({}, product);
            }));
        }
        break;
    }
}
});
