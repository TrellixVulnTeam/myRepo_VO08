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
var tidyprint_pipe_1 = require('./tidyprint-pipe');
var DatasetBasicForm = (function () {
    function DatasetBasicForm(pipsDS) {
        this.pipsDS = pipsDS;
    }
    DatasetBasicForm.prototype.putVal = function (val) {
        this.pipsDS.add(val);
        //console.log(this.pipsDS.get())
    };
    DatasetBasicForm.prototype.sendVal = function () {
        this.pipsDS.submitData();
    };
    DatasetBasicForm = __decorate([
        core_1.Component({
            selector: 'dataset-basic-form',
            templateUrl: 'app/dataset-basic-form.html',
            pipes: [tidyprint_pipe_1.TidyPrintPipe]
        }), 
        __metadata('design:paramtypes', [pips_data_service_1.PipsDataService])
    ], DatasetBasicForm);
    return DatasetBasicForm;
}());
exports.DatasetBasicForm = DatasetBasicForm;
//# sourceMappingURL=dataset-basic-form.js.map