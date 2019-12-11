odoo.define('product_multi_currency.models', function (require) {
"use strict";
var models = require('point_of_sale.models');
var core = require('web.core');
var utils = require('web.utils');
var round_pr = utils.round_precision;
var rpc = require('web.rpc');

var _t = core._t;

var model_list = models.PosModel.prototype.models;
var model_product = models.Product.prototype;

var company_currency_id;

	for(var i = 0; i < model_list.length; i++)
	    {if(model_list[i].model == 'product.product'){
	        var order_model = model_list[i];
	        order_model.fields.push('currency_id','pricelist_id');
	        order_model.loaded = function(self, products){
	            self.db.add_products(_.map(products, function (product) {
	                if (product.currency_id[0] != self.company.currency_id[0] ||
	                	 product.pricelist_id[0] != self.config.pricelist_id[0]) {
	                	
	                	company_currency_id = self.company.currency_id[0];
	                	var ratio = _.filter(self.db.currencies,function(currency){
	                						if(currency.id == product.currency_id[0]){
            									//debugger;
            									return [currency.rate,currency.rounding];
            								}
	                					});
	                	product.lst_price = round_pr(product.lst_price * ratio[0].rate, ratio[0].rounding);
	                
	                }
					product.categ = _.findWhere(self.product_categories, {'id': product.categ_id[0]});
	                return new models.Product({}, product);
	            }));
	        }
	    }
	    if(model_list[i].model == 'res.currency'){
	        var currency_model = model_list[i];
	        currency_model.ids = undefined;
	        currency_model.loaded = function(self, currencies){
            	var config_currencies = _.filter(currencies,function(currency){
            		if(currency.id == self.config.currency_id[0]){
            			return true;
            		}
            	})
            	var company_currencies = _.filter(currencies,function(currency){
            		if(currency.id == self.company.currency_id[0]){
            			return true;
            		}
            	})

            	self.db.currencies = currencies;
                //debugger;

            	self.currency = config_currencies[0];
            	if (self.currency.rounding > 0 && self.currency.rounding < 1) {
            	    self.currency.decimals = Math.ceil(Math.log(1.0 / self.currency.rounding) / Math.log(10));
            	} else {
            	    self.currency.decimals = 0;
            	}
            	self.company_currency = company_currencies[1];
        	}
	    };
}
});