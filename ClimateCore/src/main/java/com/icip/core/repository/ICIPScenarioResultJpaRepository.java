/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.icip.core.repository;

import com.icip.core.icipresult.ICIPScenarioResult;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

/**
 *
 * @author icipmac
 */
// this repository is autowired in ClimateRecordRepositoryImpl
@Repository("iCIPScenarioResultJpaRepository")
public interface ICIPScenarioResultJpaRepository extends JpaRepository<ICIPScenarioResult, Long>{
    
}
