"use strict";
var ClsMetadata_1 = require('../models/metadata/ClsMetadata');
var CI_DateTypeCode_1 = require('../models/constant/CI_DateTypeCode');
var bool_1 = require('../models/constant/bool');
var MD_SpatialRepresentationTypeCode_1 = require('../models/constant/MD_SpatialRepresentationTypeCode');
var Singleton = (function () {
    function Singleton() {
        if (!Singleton.singleton) {
            Singleton.singleton = this;
            // ... any one time initialization goes here ...
            this.test = 'first';
            this.myMetadata = new ClsMetadata_1.ClsMetadata();
            this.CI_DateTypeCode = new CI_DateTypeCode_1.CI_DateTypeCode();
            this.my_Bool = new bool_1.Bool();
            this.MD_SpatialRepresentationTypeCode = new MD_SpatialRepresentationTypeCode_1.MD_SpatialRepresentationTypeCode();
        }
        return Singleton.singleton;
    }
    return Singleton;
}());
exports.Singleton = Singleton;
//# sourceMappingURL=Singleton.js.map