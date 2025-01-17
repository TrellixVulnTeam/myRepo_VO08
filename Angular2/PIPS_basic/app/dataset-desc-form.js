"use strict";
var __decorate = (this && this.__decorate) || function (decorators, target, key, desc) {
    var c = arguments.length, r = c < 3 ? target : desc === null ? desc = Object.getOwnPropertyDescriptor(target, key) : desc, d;
    if (typeof Reflect === "object" && typeof Reflect.decorate === "function") r = Reflect.decorate(decorators, target, key, desc);
    else for (var i = decorators.length - 1; i >= 0; i--) if (d = decorators[i]) r = (c < 3 ? d(r) : c > 3 ? d(target, key, r) : d(target, key)) || r;
    return c > 3 && r && Object.defineProperty(target, key, r), r;
};
var __metadata = (this && this.__metadata) || function (k, v) {
    if (typeof Reflect === "object" && typeof Reflect.metadata === "function") return Reflect.metadata(k, v);
};
var core_1 = require('@angular/core');
var pips_data_service_1 = require('./pips-data-service');
var DatasetDescForm = (function () {
    function DatasetDescForm(pipsDS) {
        this.pipsDS = pipsDS;
    }
    DatasetDescForm.prototype.putVal = function (val) {
        this.pipsDS.add(val);
        //console.log(this.pipsDS.get())
    };
    DatasetDescForm.prototype.sendVal = function () {
        this.pipsDS.submitData();
    };
    DatasetDescForm = __decorate([
        core_1.Component({
            selector: 'dataset-desc-form',
            templateUrl: 'app/dataset-desc-form.html',
        }), 
        __metadata('design:paramtypes', [pips_data_service_1.PipsDataService])
    ], DatasetDescForm);
    return DatasetDescForm;
}());
exports.DatasetDescForm = DatasetDescForm;
//# sourceMappingURL=dataset-desc-form.js.map