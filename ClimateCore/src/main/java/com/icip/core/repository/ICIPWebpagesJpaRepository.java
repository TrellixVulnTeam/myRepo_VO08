/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.icip.core.repository;

import com.icip.core.references.ICIPWebpages;
import org.springframework.stereotype.Repository;

/**
 *
 * @author icipmac
 */
@Repository("iCIPWebpagesJpaRepository")
public interface ICIPWebpagesJpaRepository extends ICIPReferenceBaseRepository<ICIPWebpages>{
    
}
