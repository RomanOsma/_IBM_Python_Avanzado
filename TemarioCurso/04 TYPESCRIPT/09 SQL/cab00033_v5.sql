-----------------------------------------------------------------------------------------------
-- Calibración - Creacion de tabla con de buenos acumulados PDP
-- Programa: cab00033.sql
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
-- Tablas de entrada:     DCRCALIB_DESA.BS_CAL_PDP_BUENOS
--                        dcrcalib.BS_CAL_REFINANCIADOS
--                        dcrcalib.BS_CAL_REFINANCIADOS_VIG
--                        dcrcalib.LK_CAL_PRM_MATERIALIDAD
--                        dcrcalib.LK_CAL_PRM_DESCARTADOS
--
-- Tablas Intermedias:    DCRCALIB_DESA.TR_CAL_PDP_BUENOS_ENRIQ
--
-- Tablas de salida:      DCRCALIB_DESA.TR_CAL_PDP_BUE_ACU
--                        DCRCALIB_DESA.TR_CAL_PDP_DESCARTADOS
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
-- 07/01/2014 - Se añade el or_idsituac en la tabla de buenos_acu
-- 14/02/2014 - Se elimina la titularidad en la recuperación de la marca de refinanciados
-- 05/03/2015 - Se modifica el acceso a refinanciados y las marcas
-----------------------------------------------------------------------------------------------
SET VERIFY OFF
SET HEAD OFF
SET SERVEROUTPUT ON

WHENEVER SQLERROR CONTINUE;
WHENEVER OSERROR EXIT 1;
WHENEVER SQLERROR EXIT 2;

SET SERVEROUTPUT OFF;


ALTER SESSION ENABLE PARALLEL DML;

DECLARE

   vn_numerr              NUMBER(4);
   vv_count               INTEGER;
   vv_mensaje             VARCHAR2(255);
   vv_programa            VARCHAR2(15);
   v_nFecha               NUMBER;
   vv_aplicacion          VARCHAR2(10);
   vv_cuantos_registros   NUMBER;
   nme_importe_material   NUMBER;
   v_nFecha_Ref           NUMBER;

BEGIN

   vv_programa := 'cab00033';
   vv_aplicacion := 'PDP_FINAL';
   vv_count := 0;
   vv_cuantos_registros := 0;

--  1 SELECCIONA FECHA, SI MENOR QUE 2014 DE TABLA BS_CAL_PARAMETROS_PROCESO Y LA CARGA EN V_NFECHA Y V_NFECHA_REF.
   vn_numerr:= 1;
   SELECT fec_proceso
        , CASE
             WHEN fec_proceso <= 201408 then 201408
             ELSE fec_proceso
          END
   INTO v_nFecha, v_nFecha_Ref
   FROM dcrcalib_desa.bs_cal_parametros_proceso
   WHERE proceso = vv_aplicacion;

   -- 2 SLECCIONA ME_IMORT_MATERIAL DE LK_CAL_PRM_MATERNIDAD SI CUMPLE CONDICIONES Y LA CARGA EN NME_IMPORTE_MATERIAL
   vn_numerr:= 2;
   SELECT me_import_material
   INTO nme_importe_material
   FROM dcrcalib_desa.lk_cal_prm_materialidad
   WHERE de_seccion = 'PARTICULARES'
     AND sw_tipo_poblacion = 'BUENOS'
     AND id_fch_inicio_vigencia <= v_nfecha
     AND (id_fch_fin_vigencia > v_nfecha
      OR id_fch_fin_vigencia IS NULL);

-- 3 INSERTA V_NFECHA(PASO 1), VV_APLICACION, VV_PROGRAMA EN BC_CAL_CONTROL_PROCESO
   vn_numerr:= 3;
   INSERT INTO dcrcalib_desa.bs_cal_control_proceso (fec_proceso, aplicacion, proceso, fec_ini, estado)
   VALUES (v_nFecha, vv_aplicacion, vv_programa || ' - Generación Acumulado de Buenos', SYSDATE, 'INICIADO');
   COMMIT;

-- 4 INSERTA V_NFECHA(PASO 1), VV_APLICACION, VV_PROGRAMA EN BC_CAL_CONTROL_PROCESO
   vn_numerr:= 4;
   INSERT INTO dcrcalib_desa.bs_cal_control_proceso (fec_proceso, aplicacion, proceso, fec_ini, estado)
   VALUES (v_nFecha, vv_aplicacion, vv_programa || ' - Truncate Tablas', SYSDATE, 'INICIADO');
   COMMIT;

-- 5 BORRA DE TR_CAL_PDP_DESCARTADOS LOS QUE CUMPLEN LAS CONDICIONES
   vn_numerr:= 5;
   DELETE FROM dcrcalib_desa.tr_cal_pdp_descartados
   WHERE or_idmes = v_nFecha
     AND in_tippoblacion = 'BUENOS'
     AND in_proceso = 'BUE_ACU';
   COMMIT;

-- 6 LLAMADA A FUNCIONES TRUNCATE_TABLE
   vn_numerr:= 6;
		dcrcalib.fnc_truncate_table('dcrcalib_desa.tr_cal_pdp_buenos_enriq');
		dcrcalib.fnc_truncate_table('dcrcalib_desa.tr_cal_pdp_bue_acu_comp');
		dcrcalib.fnc_truncate_table('dcrcalib_desa.tr_cal_pdp_bue_acu_aux');
		dcrcalib.fnc_truncate_table('dcrcalib_desa.tr_cal_pdp_bue_acu');

-- 7 UPDATE BS_CAL_CONTROL_PROCESO CON DATOS DE PROCESO
   vn_numerr:= 7;
   UPDATE dcrcalib_desa.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = 0
   WHERE proceso = vv_programa || ' - Truncate Tablas'
     AND estado  = 'INICIADO';
   COMMIT;

-- 8 INSERT EN BS_CAL_CONTROL_PROCESO V_NFECHA, VV_APLICACION, VV_PROGRAMA
   vn_numerr:= 8;
   INSERT INTO dcrcalib_desa.bs_cal_control_proceso (fec_proceso, aplicacion, proceso, fec_ini, estado)
   VALUES (v_nFecha, vv_aplicacion, vv_programa || ' - Insert TR_CAL_PDP_BUENOS_ENRIQ', SYSDATE, 'INICIADO');
   COMMIT;

-- 9 INSERTA EN TR_CAL_PDP_BUENOS_ENRIQ UNA SELECT ESPECIFICA DE bs_cal_pdp_buenos
   vn_numerr:= 9;
   INSERT INTO dcrcalib_desa.tr_cal_pdp_buenos_enriq c
      (or_idmes          , or_numpersona   , or_tipide        , or_nifcif       , or_segges     , or_subseg
     , id_prestamo_sibis , or_scomig       , or_mapa_de_uso   , or_dictamen_rev , or_modsco     , in_empresa_grupo
     , sw_desc_traspas   , sw_desc_migrat  , or_numsco1       , or_idsituac     , id_cat_drc    , id_cat_drc_desc
     , sw_sco            , sw_sus          , sw_long_mapa_uso , sw_sit_con      , or_modsco_old , or_substda
     , or_score          , me_imp_impagado , me_impag_expos   , sw_mat_impagado 
     , sw_particular     , sw_ccaa
     , sw_cliente
     , or_destpr
     , or_ubicfi
     , fi_eadairb
     , or_idpers
     , or_nomper
     , or_refope
     , in_fecope
     , or_conced
     , or_valtas
     , or_fecvto
     , or_tipofi
     , or_titularitat
     , sw_tipopr
     , sw_usopre
     , sw_grupo_seg
     , or_totimpume
     , in_edad_transformada
     , sw_desc_material
     --Añadimos el campo or_clunicontr para poderlo arrastrar hasta la tabla BUE_ACU
     , or_clunicontr)
   SELECT /*+ PARALLEL(aux, 4) */ or_idmes          , or_numpersona   , or_tipide        , or_nifcif       , or_segges     , or_subseg
        , id_prestamo_sibis , or_scomig       , or_mapa_de_uso   , or_dictamen_rev , or_modsco     , in_empresa_grupo
        , sw_desc_traspas   , sw_desc_migrat  , or_numsco1       , or_idsituac     , id_cat_drc    , id_cat_drc_desc
        , sw_sco            , sw_sus          , sw_long_mapa_uso 
        , max(sw_sit_con) sw_sit_con 
        , or_modsco_old 
        , MAX(or_substda) as or_substda
        , or_score          , me_imp_impagado
        , NULL AS me_impag_expos   , NULL AS sw_mat_impagado   --añadido por simetria con el insert
        , sw_particular , sw_ccaa
        , sw_cliente
        , MAX(or_destpr) AS or_destpr
        , MAX(or_ubicfi) AS or_ubicfi
        , SUM(fi_eadairb) AS fi_eadairb
        , MIN(or_idpers) AS or_idpers
        , MIN(or_nomper) AS or_nomper
        , MIN(or_refope) AS or_refope
        , MIN(in_fecope) AS in_fecope
        , MAX(or_conced) AS or_conced
        , MIN(or_valtas) AS or_valtas
        , MAX(or_fecvto) AS or_fecvto
        , MIN(or_tipofi) AS or_tipofi
        , MIN(or_titularitat) AS or_titularitat
        , MAX(CASE
                 WHEN (or_idmes < 200007) THEN or_opeteso
                 ELSE or_tipopr
              END) AS sw_tipopr
        , MAX(DECODE(or_usopre, '?', or_coisin, or_usopre)) AS sw_usopre
        , MIN(SUBSTR(or_mapa_de_uso, 1, 1)) AS sw_grupo_seg
        , SUM(or_totimpume) AS or_totimpume
		--Actualizado calculo para casos en los que pase 12 meses, edad_transformada sea 1 y no 2
		,CASE
			WHEN MIN(in_fecope)IS NULL THEN 12
			WHEN (MONTHS_BETWEEN((TO_DATE(or_idmes, 'YYYYMM')), (TO_DATE(MIN(in_fecope), 'YYYYMMDD'))) / 12) <=1 THEN 1
			WHEN TRUNC(MONTHS_BETWEEN((TO_DATE(or_idmes, 'YYYYMM')), (TO_DATE(MIN(in_fecope), 'YYYYMMDD'))) / 12)+1 >= 12 THEN 12
			ELSE TRUNC(MONTHS_BETWEEN((TO_DATE(or_idmes, 'YYYYMM')), (TO_DATE(MIN(in_fecope), 'YYYYMMDD'))) / 12)+1
		END AS in_edad_transformada
        , CASE
             WHEN SUM(or_totimpume) < 0 THEN 0
             ELSE 1
          END AS sw_desc_material
        , or_clunicontr
   FROM (SELECT 
                or_idmes       , or_numpersona     , or_tipide  , or_nifcif        , or_segges
              , or_subseg      , id_prestamo_sibis , or_destpr  , or_ubicfi        , or_scomig
              , or_mapa_de_uso , or_dictamen_rev   , or_modsco  , in_empresa_grupo , sw_desc_traspas
              , sw_desc_migrat , or_numsco1        , id_cat_drc , id_cat_drc_desc  , or_totimpume
              , or_usopre      , or_coisin         , or_tipopr  , or_opeteso       , or_titularitat
              , or_tipofi      , or_fecvto         , or_valtas  , or_conced        , in_fecope
              , or_refope      , or_nomper         , or_idpers  , sw_sit_con       , or_substda
              , or_modsco_old  , or_score          , fi_eadairb , me_imp_impagado  , me_impag_expos
              , sw_mat_impagado
              , sw_particular
              , sw_ccaa
              , sw_cliente
              , FIRST_VALUE(or_idsituac) OVER (PARTITION BY id_prestamo_sibis ORDER BY CASE
                                                                                   WHEN or_idsituac IN (2, 3, 4, 5, 6, 7) THEN 1
                                                                                   WHEN or_idsituac IN (9) THEN 2
                                                                                   WHEN or_idsituac IN (0, 1) THEN 3
                                                                                END) or_idsituac
              , SUBSTR(or_mapa_de_uso, 5, 1) AS sw_sco
              , SUBSTR(or_mapa_de_uso, 3, 2) AS sw_sus
              , CASE
                   WHEN LENGTH(or_mapa_de_uso) = 6 THEN 0
                   ELSE 1
                END AS sw_long_mapa_uso
              , or_clunicontr 
         FROM dcrcalib_desa.BS_CAL_PDP_BUENOS a
         WHERE or_idmes = v_nFecha
         GROUP BY or_idmes       , or_numpersona     , or_tipide 			, or_nifcif        	, or_segges
                , or_subseg      , id_prestamo_sibis , or_destpr 			, or_ubicfi        	, or_scomig
                , or_mapa_de_uso , or_dictamen_rev   , or_modsco 			, in_empresa_grupo 	, sw_desc_traspas
                , sw_desc_migrat , or_numsco1        , id_cat_drc			, id_cat_drc_desc  	, or_totimpume
                , or_usopre      , or_coisin         , or_tipopr 			, or_opeteso       	, or_titularitat
                , or_tipofi      , or_fecvto         , or_valtas 			, or_conced        	, in_fecope
                , or_refope      , or_nomper         , or_idpers 			, or_idsituac      	, sw_sit_con
                , or_substda     , or_modsco_old     , or_score  			, fi_eadairb       	, me_imp_impagado
                , me_impag_expos , sw_mat_impagado   , sw_particular 		, sw_ccaa      		, sw_cliente
                , SUBSTR(or_mapa_de_uso, 5, 1)
                , SUBSTR(or_mapa_de_uso, 3, 2)
                , CASE
                     WHEN LENGTH(or_mapa_de_uso) = 6 THEN 0
                     ELSE 1
                  END
                , or_clunicontr) aux
   GROUP BY or_idmes         , or_numpersona     , or_tipide       , or_nifcif      , or_segges
          , or_subseg        , id_prestamo_sibis , or_scomig       , or_mapa_de_uso , or_dictamen_rev
          , or_modsco        , in_empresa_grupo  , sw_desc_traspas , sw_desc_migrat , or_numsco1
          , or_idsituac      , id_cat_drc        , id_cat_drc_desc , sw_sco         , sw_sus
          , sw_long_mapa_uso , or_modsco_old     , or_score        , me_imp_impagado, me_impag_expos   , sw_mat_impagado --Añadido por simetria con el insert
          , sw_cliente     , sw_particular       , sw_ccaa         , or_clunicontr;
   COMMIT;

-- 10 UPDATE BS_CAL_CONTROL_PROCESO CON DATOS DEL INSERT ANTERIOR
   UPDATE dcrcalib_desa.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = vv_cuantos_registros
   WHERE proceso = vv_programa || ' - Insert TR_CAL_PDP_BUENOS_ENRIQ'
     AND estado  = 'INICIADO';
   COMMIT;

-- 11 INSERT EN BS_CAL_CONTROL_PROCESO DE DATOS DE PROCCESO
	 vn_numerr:= 10;
   INSERT INTO dcrcalib_desa.bs_cal_control_proceso (fec_proceso, aplicacion, proceso, fec_ini, estado)
   VALUES (v_nFecha, vv_aplicacion, vv_programa || ' - Insert TR_CAL_PDP_BUE_ACU_COMP', SYSDATE, 'INICIADO');
   COMMIT;

-- 12 INSERT EM TR_CAL_PDP_DESCARTADOS DE SELECT DE tr_cal_pdp_buenos_enriq Y dcrcalib.lk_cal_prm_descartados QUE CUMPLAN CONDICIONES
   INSERT INTO dcrcalib_desa.tr_cal_pdp_bue_acu_comp t_in
      (or_idmes          , or_numpersona     , or_tipide        , or_nifcif        , or_segges
     , or_subseg         , id_prestamo_sibis , or_destpr        , or_ubicfi        , or_scomig
     , or_mapa_de_uso    , or_dictamen_rev   , or_modsco        , in_empresa_grupo , sw_desc_traspas
     , sw_desc_migrat    , or_numsco1        , or_idsituac      , id_cat_drc       , id_cat_drc_desc
     , sw_sco            , sw_sus            , sw_long_mapa_uso , sw_sit_con       , or_modsco_old
     , or_substda        , or_score          , me_imp_impagado  , me_impag_expos   , sw_mat_impagado
     , fi_eadairb        , or_idpers         , or_nomper        , or_refope        , in_fecope
     , or_conced         , or_valtas         , or_fecvto        , or_tipofi        , or_titularitat
     , sw_tipopr         , sw_usopre         , sw_grupo_seg     , or_totimpume     , in_edad_transformada
     , sw_desc_material  , or_score4         , sw_cliente       , sw_particular    , sw_ccaa
     , in_prod_score
     , sw_comportamental
     --Añadimos el campo or_clunicontr para poderlo arrastrar hasta la tabla BUE_ACU
     , or_clunicontr)
   SELECT /*+ PARALLEL(a, 2)
              PARALLEL(c, 2) */
          or_idmes         , or_numpersona     , or_tipide        , or_nifcif        , or_segges
        , or_subseg        , id_prestamo_sibis , or_destpr        , or_ubicfi        , or_scomig
        , or_mapa_de_uso   , or_dictamen_rev   , or_modsco        , in_empresa_grupo , sw_desc_traspas
        , sw_desc_migrat   , or_numsco1        , or_idsituac      , id_cat_drc       , id_cat_drc_desc
        , sw_sco           , sw_sus            , sw_long_mapa_uso , sw_sit_con       , or_modsco_old
        , or_substda       , or_score          , me_imp_impagado  , me_impag_expos   , sw_mat_impagado
        , fi_eadairb       , or_idpers         , or_nomper        , or_refope        , in_fecope
        , or_conced        , or_valtas         , or_fecvto        , or_tipofi        , or_titularitat
        , sw_tipopr        , sw_usopre         , sw_grupo_seg     , or_totimpume     , in_edad_transformada
        , sw_desc_material , score4            , sw_cliente       , sw_particular    , sw_ccaa
        , CASE
             WHEN or_idmes >= 200806 THEN prod_score
             ELSE NULL
          END in_prod_score
        , CASE
             WHEN or_idmes >= 200806 THEN
                CASE
                   WHEN prod_score IS NULL THEN 0
                   ELSE 1
                END
             ELSE
                CASE
                   WHEN b.at_mapa_de_uso IS NULL AND MONTHS_BETWEEN(TO_DATE(v_nFecha, 'yyyymm'), TO_DATE(SUBSTR(in_fecope, 1, 6), 'yyyymm')) >= 6 THEN 1
                   WHEN b.at_mapa_de_uso IS NULL AND MONTHS_BETWEEN(TO_DATE(v_nFecha, 'yyyymm'), TO_DATE(SUBSTR(in_fecope, 1, 6), 'yyyymm')) < 6 THEN 0
                   WHEN b.at_mapa_de_uso IS NOT NULL THEN 0
                END
          END sw_comportamental
        , or_clunicontr
   FROM dcrcalib_desa.tr_cal_pdp_buenos_enriq a
      , dcrcalib.lk_cal_prm_mapa_uso b
      , dcrprop_mensual.bs_scores_contrato_comportamen c
   WHERE a.or_mapa_de_uso = b.at_mapa_de_uso(+)
     AND b.sw_eliminar(+) = 1
     AND a.id_prestamo_sibis = c.contrato_disp (+)
     AND a.or_idmes = c.mes_proceso (+)
     AND c.mes_proceso (+) = v_nFecha;
   COMMIT;
   -- 13 UPDATE DE BS_CAL_CONTROL_PROCESO CON DATOS DEL INSERT ANTERIOR
   UPDATE dcrcalib_desa.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = vv_cuantos_registros
   WHERE proceso = vv_programa || ' - Insert TR_CAL_PDP_BUE_ACU_COMP'
     AND estado  = 'INICIADO';
   COMMIT;

-- 14 INSERT EN BS_CAL_CONTROL_PROCESO DE DATOS DE PROCESO ANTERIOR
	vn_numerr:= 11;
   INSERT INTO dcrcalib_desa.bs_cal_control_proceso (fec_proceso, aplicacion, proceso, fec_ini, estado)
   VALUES (v_nFecha, vv_aplicacion, vv_programa || ' - Insert TR_CAL_PDP_BUE_ACU_AUX 1/2', SYSDATE, 'INICIADO');
   COMMIT;

-- 15 INSERT EN TR_CAL_PDP_BUE_ACU_COMP SELECT DE tr_cal_pdp_buenos_enriq, dcrcalib.lk_cal_prm_mapa_uso, dcrprop_mensual.bs_scores_contrato_comportamen
   INSERT INTO dcrcalib_desa.tr_cal_pdp_bue_acu_aux c
      (or_idmes          , or_titularitat   , or_numpersona   , or_tipide         , or_nifcif
     , or_idpers         , or_nomper        , or_segges       , or_subseg         , or_refope
     , id_prestamo_sibis , in_fecope        , or_fecvto       , or_tipofi         , sw_tipopr
     , sw_usopre         , or_destpr        , or_conced       , or_valtas         , or_ubicfi
     , or_scomig         , or_mapa_de_uso   , sw_sus          , sw_grupo_seg      , sw_sco
     , or_numsco1        , or_dictamen_rev  , or_totimpume    , or_modsco         , sw_sit_con
     , or_modsco_old     , or_substda       , sw_traspaso     , in_empresa_grupo  , or_idsituac
     , id_cat_drc        , id_cat_drc_desc  , min_cto_ltv_tit , in_seg_hip_new    , or_fec_tas
     , or_valtas_new     , sum_vt_ltv_tit   , or_impltv_new   , fi_eadairb        , me_imp_impagado
     , me_impag_expos    , sw_mat_impagado  , or_score        , or_score4         , in_prod_score
     , sw_comportamental , sw_cliente       , sw_particular   , sw_ccaa
     , in_edad_transformada
     , in_marca_refi
     , in_min_ver_refi
     , in_max_ver_refi_vig
     , in_marca_refi_titu
     , in_min_ver_refi_titu
     --Añadimos el campo or_clunicontr para poderlo arrastrar hasta la tabla BUE_ACU
     , or_clunicontr)
   SELECT /*+ PARALLEL(tr, 2) (hip, 2) */
          DISTINCT
          tr.or_idmes          , tr.or_titularitat   , tr.or_numpersona    , tr.or_tipide        , tr.or_nifcif
        , tr.or_idpers         , tr.or_nomper        , tr.or_segges        , tr.or_subseg        , tr.or_refope
        , tr.id_prestamo_sibis , tr.in_fecope        , tr.or_fecvto        , tr.or_tipofi        , tr.sw_tipopr
        , tr.sw_usopre         , tr.or_destpr        , tr.or_conced        , tr.or_valtas        , tr.or_ubicfi
        , tr.or_scomig         , tr.or_mapa_de_uso   , tr.sw_sus           , tr.sw_grupo_seg     , tr.sw_sco
        , tr.or_numsco1        , tr.or_dictamen_rev  , tr.or_totimpume     , tr.or_modsco        , tr.sw_sit_con
        , tr.or_modsco_old     , tr.or_substda       , tr.sw_desc_traspas  , tr.in_empresa_grupo , tr.or_idsituac
        , tr.id_cat_drc        , tr.id_cat_drc_desc  , hip.min_cto_ltv_tit , hip.in_seg_hip_new  , hip.or_fec_tas
        , hip.or_valtas_new    , hip.sum_vt_ltv_tit  , hip.or_impltv_new   , fi_eadairb          , me_imp_impagado
        , me_impag_expos       , sw_mat_impagado     , or_score            , or_score4           , in_prod_score
        , sw_comportamental    , sw_cliente          , sw_particular       , sw_ccaa
        , MAX(tr.in_edad_transformada) OVER (PARTITION BY tr.id_prestamo_sibis) AS in_edad_transformada
        , CASE
             WHEN v_nFecha_Ref <= 201408 THEN
                CASE
                   WHEN TO_NUMBER(TO_CHAR(rf.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN 1
                   ELSE 0
                END
             ELSE
               CASE
                  WHEN rf.in_max_ver_refi_vig = v_nFecha AND TO_NUMBER(TO_CHAR(rf.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN 1
                  ELSE 0
             END
          END in_marca_refi
        , CASE
            WHEN v_nFecha_Ref <= 201408 THEN
               CASE
                  WHEN TO_NUMBER(TO_CHAR(rf.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN rf.in_min_ver_refi
                  ELSE NULL
               END
            ELSE
               CASE
                  WHEN rf.in_max_ver_refi_vig = v_nFecha AND TO_NUMBER(TO_CHAR(rf.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN rf.in_min_ver_refi
                  ELSE NULL
               END
          END in_min_ver_refi
        , CASE
             WHEN rf.in_max_ver_refi_vig = v_nFecha_ref THEN rf.in_max_ver_refi_vig
             ELSE NULL
          END in_max_ver_refi_vig
        , CASE
             WHEN v_nFecha_Ref <= 201408 THEN
                CASE
                   WHEN TO_NUMBER(TO_CHAR(rft.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN 1
                   ELSE 0
                END
             ELSE
               CASE
                  WHEN rft.in_max_ver_refi_vig = v_nFecha AND
                       TO_NUMBER(TO_CHAR(rft.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN 1
                  ELSE 0
             END
          END in_marca_refi_titu
        , CASE
            WHEN v_nFecha_Ref <= 201408 THEN
               CASE
                  WHEN TO_NUMBER(TO_CHAR(rft.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN rft.in_min_ver_refi
                  ELSE NULL
               END
            ELSE
               CASE
                  WHEN rft.in_max_ver_refi_vig = v_nFecha AND TO_NUMBER(TO_CHAR(rft.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN rft.in_min_ver_refi
                  ELSE NULL
               END
          END in_min_ver_refi_titu
        --Añadimos el campo or_clunicontr para poderlo arrastrar hasta la tabla BUE_ACU
        , tr.or_clunicontr
   FROM dcrcalib_desa.tr_cal_pdp_bue_acu_comp tr
      , (SELECT id_prestamo_sibis , in_min_ver_refi , d.or_idmes in_max_ver_refi_vig
         FROM dcrcalib.BS_CAL_REFINANCIADOS_vig d
            , (SELECT prestamo id_prestamo_sibis, MIN(fecha_version) in_min_ver_refi
               FROM dcrcalib.BS_CAL_REFINANCIADOS refi
               WHERE or_idmes = v_nFecha_Ref
               GROUP BY prestamo) c
         WHERE c.id_prestamo_sibis = d.prestamo (+)
           AND d.or_idmes (+) = v_nFecha_Ref) rf
       ----- Nivel titularidad -------------------------------
      , (SELECT DISTINCT e.titularidad , e.in_min_ver_refi , f.or_idmes in_max_ver_refi_vig
         FROM dcrcalib.BS_CAL_REFINANCIADOS_VIG f
            , (SELECT titularidad, MIN(fecha_version) in_min_ver_refi
               FROM dcrcalib.BS_CAL_REFINANCIADOS refit
               WHERE or_idmes = v_nFecha_Ref
               GROUP BY titularidad) e
         WHERE e.titularidad = f.titularidad (+)
          AND nvl(e.titularidad,0) <> 0
           AND f.or_idmes (+) = v_nFecha_Ref) rft
       ------------------------------------------------------------
      , (SELECT or_valtas_new , or_clunicuent  , or_refope       , or_idmes , or_impltv_new , sum_vt_ltv_tit
              , or_fec_tas    , in_seg_hip_new , min_cto_ltv_tit
              , DENSE_RANK() OVER (PARTITION BY contr_cluniprod ORDER BY CASE
                                                                            WHEN or_cluniprod= 'PR' THEN 1
                                                                            WHEN or_cluniprod <> 'DV' THEN 2
                                                                            ELSE 3
                                                                         END) orden
         FROM dcrcalib.bs_cal_inv_unio_hip inv
         WHERE or_idmes = v_nFecha) hip
   WHERE sw_desc_migrat = 0
     AND sw_long_mapa_uso = 0
     AND sw_desc_material = 0
     AND tr.or_idmes = v_nFecha
     AND SUBSTR(tr.id_prestamo_sibis, 1, 3) = '827'
     AND tr.id_prestamo_sibis = rf.id_prestamo_sibis(+)
     AND tr.or_titularitat = rft.titularidad(+)
     AND tr.or_idmes = hip.or_idmes(+)
     AND tr.id_prestamo_sibis = CASE
                                   WHEN v_nFecha <= 201111 then hip.or_refope(+)
                                   ELSE hip.or_clunicuent(+)
                                END
     AND hip.orden(+) = 1;

   vv_cuantos_registros := SQL%ROWCOUNT;
   COMMIT;

   -- 16 UPDATE DE CONTROL DE PROCESOS
   UPDATE dcrcalib_desa.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = vv_cuantos_registros
   WHERE proceso = vv_programa || ' - Insert TR_CAL_PDP_BUE_ACU_AUX 1/2'
     AND estado  = 'INICIADO';
   COMMIT;

-- 17 INSERT DE CONTROL DE PROCESOS
		vn_numerr:= 12;
   INSERT INTO dcrcalib_desa.bs_cal_control_proceso (fec_proceso, aplicacion, proceso, fec_ini, estado)
   VALUES (v_nFecha, vv_aplicacion, vv_programa || ' - Insert TR_CAL_PDP_BUE_ACU_AUX 2/2', SYSDATE, 'INICIADO');
   COMMIT;

-- 18 INSERT EN TR_CAL_PDP_BUE_ACU DE LA SELECT DE tr_cal_pdp_bue_acu_comp()
   INSERT INTO dcrcalib_desa.tr_cal_pdp_bue_acu_aux c
      (or_idmes          , or_titularitat   , or_numpersona   , or_tipide         , or_nifcif
     , or_idpers         , or_nomper        , or_segges       , or_subseg         , or_refope
     , id_prestamo_sibis , in_fecope        , or_fecvto       , or_tipofi         , sw_tipopr
     , sw_usopre         , or_destpr        , or_conced       , or_valtas         , or_ubicfi
     , or_scomig         , or_mapa_de_uso   , sw_sus          , sw_grupo_seg      , sw_sco
     , or_numsco1        , or_dictamen_rev  , or_totimpume    , or_modsco         , sw_sit_con
     , or_modsco_old     , or_substda       , sw_traspaso     , in_empresa_grupo  , or_idsituac
     , id_cat_drc        , id_cat_drc_desc  , min_cto_ltv_tit , in_seg_hip_new    , or_fec_tas
     , or_valtas_new     , sum_vt_ltv_tit   , or_impltv_new   , fi_eadairb        , me_imp_impagado
     , me_impag_expos    , sw_mat_impagado  , or_score        , or_score4         , in_prod_score
     , sw_comportamental , sw_cliente       , sw_particular   , sw_ccaa
     , in_edad_transformada
     , in_marca_refi
     , in_min_ver_refi
     , in_max_ver_refi_vig
     , in_marca_refi_titu
     , in_min_ver_refi_titu
     --Añadimos el campo or_clunicontr para poderlo arrastrar hasta la tabla BUE_ACU
     , or_clunicontr)
   SELECT /*+ PARALLEL(tr, 2) (hip, 2) */
          DISTINCT
          tr.or_idmes          , tr.or_titularitat   , tr.or_numpersona    , tr.or_tipide        , tr.or_nifcif
        , tr.or_idpers         , tr.or_nomper        , tr.or_segges        , tr.or_subseg        , tr.or_refope
        , tr.id_prestamo_sibis , tr.in_fecope        , tr.or_fecvto        , tr.or_tipofi        , tr.sw_tipopr
        , tr.sw_usopre         , tr.or_destpr        , tr.or_conced        , tr.or_valtas        , tr.or_ubicfi
        , tr.or_scomig         , tr.or_mapa_de_uso   , tr.sw_sus           , tr.sw_grupo_seg     , tr.sw_sco
        , tr.or_numsco1        , tr.or_dictamen_rev  , tr.or_totimpume     , tr.or_modsco        , tr.sw_sit_con
        , tr.or_modsco_old     , tr.or_substda       , tr.sw_desc_traspas  , tr.in_empresa_grupo , tr.or_idsituac
        , tr.id_cat_drc        , tr.id_cat_drc_desc  , hip.min_cto_ltv_tit , hip.in_seg_hip_new  , hip.or_fec_tas
        , hip.or_valtas_new    , hip.sum_vt_ltv_tit  , hip.or_impltv_new   , fi_eadairb          , me_imp_impagado
        , me_impag_expos       , sw_mat_impagado     , or_score            , or_score4           , in_prod_score
        , sw_comportamental    , sw_cliente          , sw_particular       , sw_ccaa
        , MAX(tr.in_edad_transformada) OVER (PARTITION BY tr.id_prestamo_sibis) AS in_edad_transformada
        , CASE
             WHEN v_nFecha_Ref <= 201408 THEN
                CASE
                   WHEN TO_NUMBER(TO_CHAR(rf.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN 1
                   ELSE 0
                END
             ELSE
               CASE
                  WHEN rf.in_max_ver_refi_vig = v_nFecha AND
                       TO_NUMBER(TO_CHAR(rf.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN 1
                  ELSE 0
             END
          END in_marca_refi
        , CASE
            WHEN v_nFecha_Ref <= 201408 THEN
               CASE
                  WHEN TO_NUMBER(TO_CHAR(rf.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN rf.in_min_ver_refi
                  ELSE NULL
               END
            ELSE
               CASE
                  WHEN rf.in_max_ver_refi_vig = v_nFecha AND TO_NUMBER(TO_CHAR(rf.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN rf.in_min_ver_refi
                  ELSE NULL
               END
          END in_min_ver_refi
        , CASE
             WHEN rf.in_max_ver_refi_vig = v_nFecha_ref THEN rf.in_max_ver_refi_vig
             ELSE NULL
          END in_max_ver_refi_vig
        , CASE
             WHEN v_nFecha_Ref <= 201408 THEN
                CASE
                   WHEN TO_NUMBER(TO_CHAR(rft.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN 1
                   ELSE 0
                END
             ELSE
               CASE
                  WHEN rft.in_max_ver_refi_vig = v_nFecha AND
                       TO_NUMBER(TO_CHAR(rft.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN 1
                  ELSE 0
             END
          END in_marca_refi_titu
        , CASE
            WHEN v_nFecha_Ref <= 201408 THEN
               CASE
                  WHEN TO_NUMBER(TO_CHAR(rft.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN rft.in_min_ver_refi
                  ELSE NULL
               END
            ELSE
               CASE
                  WHEN rft.in_max_ver_refi_vig = v_nFecha AND TO_NUMBER(TO_CHAR(rft.in_min_ver_refi, 'yyyymm')) <= tr.or_idmes THEN rft.in_min_ver_refi
                  ELSE NULL
               END
          END in_min_ver_refi_titu
        --Añadimos el campo or_clunicontr para poderlo arrastrar hasta la tabla BUE_ACU
        , tr.or_clunicontr
   FROM dcrcalib_desa.tr_cal_pdp_bue_acu_comp tr
      , (SELECT id_prestamo_sibis , in_min_ver_refi , d.or_idmes in_max_ver_refi_vig
         FROM dcrcalib.BS_CAL_REFINANCIADOS_VIG d
            , (SELECT prestamo id_prestamo_sibis
                    , MIN(fecha_version) in_min_ver_refi
               FROM dcrcalib.BS_CAL_REFINANCIADOS refi
               WHERE or_idmes = v_nFecha_Ref
               GROUP BY prestamo) c
         WHERE c.id_prestamo_sibis = d.prestamo (+)
           AND d.or_idmes (+) = v_nFecha_Ref) rf
       ----- Nivel titularidad -------------------------------
       , ( SELECT distinct e.titularidad , e.in_min_ver_refi , f.or_idmes in_max_ver_refi_vig
         FROM dcrcalib.BS_CAL_REFINANCIADOS_VIG f
            , (SELECT titularidad, MIN(fecha_version) in_min_ver_refi
               FROM dcrcalib.BS_CAL_REFINANCIADOS refit
               WHERE or_idmes = v_nFecha_Ref
               GROUP BY titularidad) e
         WHERE e.titularidad = f.titularidad (+)
          AND nvl(e.titularidad,0) <> 0
           AND f.or_idmes (+) = v_nFecha_Ref) rft
       ------------------------------------------------------------
      , (SELECT inv.*
              , DENSE_RANK() OVER (PARTITION BY contr_cluniprod ORDER BY CASE
                                                                            WHEN or_cluniprod= 'PR' THEN 1
                                                                            WHEN or_cluniprod <> 'DV' THEN 2
                                                                            ELSE 3
                                                                         END) orden
         FROM dcrcalib.bs_cal_inv_unio_hip inv
         WHERE or_idmes = v_nFecha) hip
   WHERE sw_desc_migrat = 0
     AND sw_long_mapa_uso = 0
     AND sw_desc_material = 0
     AND tr.or_idmes = v_nFecha
     AND substr(tr.id_prestamo_sibis,1,3) <> '827'
     AND tr.id_prestamo_sibis = rf.id_prestamo_sibis (+)
     AND tr.or_titularitat = rft.titularidad (+)
     AND tr.or_idmes = hip.or_idmes (+)
     AND tr.id_prestamo_sibis = CASE
                                   WHEN v_nFecha <= 201111 then hip.or_refope(+)
                                   ELSE hip.or_clunicuent(+)
                                END
     AND hip.orden(+) = 1;

   vv_cuantos_registros := SQL%ROWCOUNT;
   COMMIT;

-- 19 UPDATE DE CONTROL DE PROCESSO
   UPDATE dcrcalib_desa.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = vv_cuantos_registros
   WHERE proceso = vv_programa || ' - Insert TR_CAL_PDP_BUE_ACU_AUX 2/2'
     AND estado  = 'INICIADO';
   COMMIT;

-- 21 INSERT NE TR_CAL_PDP_BUE_ACU DE LA SELECT CONTRA tr_cal_pdp_bue_acu_comp()
   INSERT INTO dcrcalib_desa.tr_cal_pdp_bue_acu c
      (or_idmes          , or_titularitat   , or_numpersona   , or_tipide         , or_nifcif
     , or_idpers         , or_nomper        , or_segges       , or_subseg         , or_refope
     , id_prestamo_sibis , in_fecope        , or_fecvto       , or_tipofi         , sw_tipopr
     , sw_usopre         , or_destpr        , or_conced       , or_valtas         , or_ubicfi
     , or_scomig         , or_mapa_de_uso   , sw_sus          , sw_grupo_seg      , sw_sco
     , or_numsco1        , or_dictamen_rev  , or_totimpume    , or_modsco         , sw_sit_con
     , or_modsco_old     , or_substda       , sw_traspaso     , in_empresa_grupo  , or_idsituac
     , id_cat_drc        , id_cat_drc_desc  , min_cto_ltv_tit , in_seg_hip_new    , or_fec_tas
     , or_valtas_new     , sum_vt_ltv_tit   , or_impltv_new   , fi_eadairb        , me_imp_impagado
     , me_impag_expos    , sw_mat_impagado  , or_score        , or_score4         , in_prod_score
     , sw_comportamental , sw_cliente       , sw_particular   , sw_ccaa
     , in_edad_transformada
     , in_marca_refi
     , in_min_ver_refi
     , in_max_ver_refi_vig
     , in_marca_refi_titu
     , in_min_ver_refi_titu
     , or_clunicontr)
   SELECT /*+parallel (aux,4)*/ or_idmes    , or_titularitat  , or_numpersona     , or_tipide         , or_nifcif
     , or_idpers         , or_nomper        , or_segges       , or_subseg         , or_refope
     , id_prestamo_sibis , in_fecope        , or_fecvto       , or_tipofi         , sw_tipopr
     , sw_usopre         , or_destpr        , or_conced       , or_valtas         , or_ubicfi
     , or_scomig         , or_mapa_de_uso   , sw_sus          , sw_grupo_seg      , sw_sco
     , or_numsco1        , or_dictamen_rev  , or_totimpume    , or_modsco         , sw_sit_con
     , or_modsco_old     , or_substda       , sw_traspaso     , in_empresa_grupo  , or_idsituac
     , id_cat_drc        , id_cat_drc_desc  , min_cto_ltv_tit , in_seg_hip_new    , or_fec_tas
     , or_valtas_new     , sum_vt_ltv_tit   , or_impltv_new   , fi_eadairb        , me_imp_impagado
     , me_impag_expos    
     , sw_mat_impagado  
     , or_score        , or_score4         , in_prod_score
     , sw_comportamental , sw_cliente       , sw_particular   , sw_ccaa
     , in_edad_transformada
     , in_marca_refi
     , in_min_ver_refi
     , in_max_ver_refi_vig
     , in_marca_refi_titu
     , in_min_ver_refi_titu
     , or_clunicontr
   FROM dcrcalib_desa.tr_cal_pdp_bue_acu_aux aux;
     
     vv_cuantos_registros := SQL%ROWCOUNT;
   COMMIT;

-- 22 UPDATE DE CONTROL DE PROCESO
   UPDATE dcrcalib_desa.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = vv_cuantos_registros
   WHERE proceso = vv_programa || ' - Insert TR_CAL_PDP_BUE_ACU '
     AND estado  = 'INICIADO';
   COMMIT;

-- 23 UPDATE DE CONTROL DE PROCESO
   vn_numerr:= 13;
   UPDATE dcrcalib_desa.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = 0
   WHERE proceso = vv_programa || ' - Generación Acumulado de Buenos'
     AND estado  = 'INICIADO';
   COMMIT;

-- 24 CONTROL DE EXCEPCIONES
EXCEPTION
   WHEN OTHERS THEN

      vv_mensaje:= SUBSTR(TO_CHAR(SQLCODE) || SQLERRM, 1, 255);

-- 25 INSERT DE CONTROL DE PROCESO 
      INSERT INTO dcrcalib_desa.bs_cal_control_proceso (fec_proceso, aplicacion, proceso, fec_ini, estado, finalizado, error_prog, num_error, error_orac, fec_fin)
      VALUES (v_nFecha, vv_aplicacion, vv_programa || ' - Generación Acumulado de Buenos', SYSDATE, 'ABORTADO', 'KO', vv_programa, vn_numerr, vv_mensaje, sysdate);
      COMMIT;

-- 26 UPDATE DINAMICO DE CONTROL DE PROCESO
   EXECUTE IMMEDIATE '
      UPDATE dcrcalib_desa.bs_cal_control_proceso
      SET estado = ''ABORTADO'',
          fec_fin = SYSDATE,
          tiempo = (current_timestamp - fec_ini),
          finalizado = ''KO''
      WHERE proceso like ''' || vv_programa || '%''
        AND finalizado IS NULL';
      COMMIT;

      vv_mensaje := to_date('19950000','YYYYMMDD');

END;
/

EXIT;