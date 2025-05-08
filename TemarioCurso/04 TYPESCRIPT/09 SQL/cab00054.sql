-- Calibración - Generación PDS TCR Buenos Acumulados
-- Programa: cab00054.sql
-----------------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------------
-- Tablas de entrada:     DCRCALIB.BS_CAL_PDS_TCR_PRE_ACU_BUE
--                        DCRCALIB.BS_CAL_PDS_TCR_MAL_ACU
--                        DCRCALIB.LK_CAL_PRM_DESCARTADOS
--                        DCRCALIB.BS_CAL_PE_FUNCIONES
--                        DCRCALIB.LK_CAL_PRM_PERCURA
--                        DCRCALIB.BS_CAL_PDCA_MALOS_ACU
--                        DCRCALIB.BS_CAL_PDCA_BUENOS_ACU
--                        DCRCALIB.BS_CAL_PDS_TCR_CTO_OPER_AGRUP
--                        DCRCALIB.LK_CAL_PRM_MATERIALIDAD
--
-- Tablas de trabajo      DCRCALIB.TR_CAL_PDS_TCR_PRE_ACU_BUE_1
--                        DCRCALIB.TR_CAL_PDS_TCR_BUE_ACU_1
--                        DCRCALIB.TR_CAL_PDS_TCR_BUE_ACU_2
--
-- Tablas de salida:      DCRCALIB.TR_CAL_PDS_TCR_BUE_ACU
--                        DCRCALIB.TR_CAL_PDS_TCR_BUE_ACU_DES
--
-- Tabla control proceso: DCRCALIB.BS_CAL_CONTROL_PROCESO
--                        DCRCALIB.BS_CAL_PARAMETROS_PROCESO
-----------------------------------------------------------------------------------------------
set verify off
set head off
SET SERVEROUTPUT ON

whenever oserror exit 1;
whenever sqlerror exit 3;

/* INICIO CONEXION COMO USUARIO PROPIETARIO */
start $BDD_PWD/propietaris.pwd DCRCALIB
/* FIN CONEXION COMO USUARIO PROPIETARIO */

ALTER SESSION ENABLE PARALLEL DML;

DECLARE

   vn_numerr             NUMBER(4);
   vv_count              INTEGER;
   vv_count_bue          INTEGER;
   vv_count_mal          INTEGER;
   vv_count_des          INTEGER;
   vv_mensaje            VARCHAR2(255);
   vv_programa           VARCHAR2(15);
   v_nFecha              number;
   v_nFecha_Particion    number;
   vv_aplicacion         varchar2(10);
   v_cMotivo             VARCHAR2(200);
   v_cMotivo1            VARCHAR2(200);
   v_cMotivo2            VARCHAR2(200);
   v_nmeses_ta           number;
   v_nmeses_kt           number;
   v_nMaxFecha           NUMBER(6);
   v_nMargen             NUMBER;
   v_nPercura            NUMBER;

BEGIN

   vv_programa := 'cab00054';
   vv_aplicacion := 'PDS_TCR';
   vv_count := 0;

  -- Se obtiene la fecha del pase
  --  1 SELECCIONA FECHA, SI MENOR QUE 2014 DE TABLA BS_CAL_PARAMETROS_PROCESO Y LA CARGA EN V_NFECHA Y V_NFECHA_REF.
  SELECT FEC_PROCESO
  INTO v_nFecha
  FROM DCRCALIB.BS_CAL_PARAMETROS_PROCESO
  WHERE proceso = vv_aplicacion;

-------------------------------------------------------------------------------------------------------------------------------------
--   Inicio Proceso
-- 2 INSERTA V_NFECHA(PASO 1), VV_APLICACION, VV_PROGRAMA EN BC_CAL_CONTROL_PROCESO

-------------------------------------------------------------------------------------------------------------------------------------
   vn_numerr:= 1;
   INSERT INTO DCRCALIB.BS_CAL_CONTROL_PROCESO (fec_proceso, aplicacion, PROCESO, FEC_INI, ESTADO)
   VALUES (v_nFecha, vv_aplicacion, VV_PROGRAMA||' - Generación Tratamiento BUE_ACU', SYSDATE, 'INICIADO');
   COMMIT;

-- 3 INSERTA V_NFECHA(PASO 1), VV_APLICACION, VV_PROGRAMA EN BC_CAL_CONTROL_PROCESO
   vn_numerr:= 2;
   INSERT INTO DCRCALIB.BS_CAL_CONTROL_PROCESO (fec_proceso, aplicacion,PROCESO, FEC_INI, ESTADO)
   VALUES (v_nFecha, vv_aplicacion, VV_PROGRAMA||' - Truncate Tablas Temporales', SYSDATE, 'INICIADO');
   COMMIT;

-- 4 LLAMADA A FUNCIONES TRUNCATE_TABLE
   vn_numerr:= 3;
   FNC_TRUNCATE_TABLE('DCRCALIB.TR_CAL_PDS_TCR_PRE_ACU_BUE_1');
   FNC_TRUNCATE_TABLE('DCRCALIB.TR_CAL_PDS_TCR_BUE_ACU_1');
   FNC_TRUNCATE_TABLE('DCRCALIB.TR_CAL_PDS_TCR_BUE_ACU_2');
   FNC_TRUNCATE_TABLE('DCRCALIB.TR_CAL_PDS_TCR_BUE_ACU');
   FNC_TRUNCATE_TABLE('DCRCALIB.TR_CAL_PDS_TCR_BUE_ACU_DES');

-- 5 UPDATE BS_CAL_CONTROL_PROCESO CON DATOS DE PROCESO
   vn_numerr:= 4;
   UPDATE DCRCALIB.BS_CAL_CONTROL_PROCESO
   SET ESTADO = 'FINALIZADO',
       FEC_FIN = SYSDATE,
       TIEMPO = (current_timestamp - FEC_INI),
       FINALIZADO = 'OK',
       REG_INS_OK = 0
   WHERE PROCESO = VV_PROGRAMA||' - Truncate Tablas Temporales'
     AND ESTADO  = 'INICIADO';
   COMMIT;

-------------------------------------------------------------------------------------------------------------------------------------
--   Tratamiento
-- 6 INSERT EN BS_CAL_CONTROL_PROCESO V_NFECHA, VV_APLICACION, VV_PROGRAMA

-------------------------------------------------------------------------------------------------------------------------------------
   vn_numerr:= 5;
   INSERT INTO DCRCALIB.BS_CAL_CONTROL_PROCESO (fec_proceso, aplicacion, PROCESO, FEC_INI, ESTADO)
   VALUES (v_nFecha, vv_aplicacion, VV_PROGRAMA||' - Tratamiento población BUE_ACU (proceso datos)', SYSDATE, 'INICIADO');
   COMMIT;

--7 SERIE DE SELECTS PARA DESCARTES. CARGAMOS V_CMOTIVO DESDE LK_CAL_PRM_DESCARTADOS.DE_MOTIVOS
   SELECT de_motivo
   INTO v_cMotivo
   FROM DCRCALIB.lk_cal_prm_descartados
   WHERE id_campo = 'SW_IMP_TARJETA_0';

   SELECT de_motivo
   INTO v_cMotivo1
   FROM DCRCALIB.lk_cal_prm_descartados
   WHERE id_campo = 'SW_SUPERA_PERCURA';

   SELECT de_motivo
   INTO v_cMotivo2
   FROM DCRCALIB.lk_cal_prm_descartados
   WHERE id_campo = 'SW_MAT_CONT_PERCURA';
   
-- 8 SELECT PARA CARGAR V_NPERCURA DESDE LK_CAL_PRM_PERCURA.ME_PERCURA
   SELECT me_percura
   INTO v_nPercura
   FROM DCRCALIB.LK_CAL_PRM_PERCURA
   WHERE de_seccion = 'PD_SCORING_TCR'
   AND v_nFecha >= id_fch_ini_vigencia
   AND v_nFecha < nvl(id_fch_fin_vigencia, '299901');

-- 9 INSERT EN TR_CAL_PDS_TCR_PRE_ACU_BUE_1 DE (bs_cal_pds_tcr_pre_acu_bue UNION bs_cal_pds_tcr_pre_acu_bue)
	 vn_numerr:= 6;
   INSERT /*+ PARALLEL(dcrcalib.tr_cal_pds_tcr_pre_acu_bue_1, 4)
              PARALLEL(dcrcalib.tr_cal_pds_tcr_bue_acu_des, 4) */
   FIRST
      WHEN or_cluniprod_recup IS NULL THEN
         INTO dcrcalib.tr_cal_pds_tcr_pre_acu_bue_1
            (or_idmes             , or_idpers           , or_tipide       , or_nifcif           , or_numcta
           , or_idsituac          , or_tipotit          , or_titularitat  , or_segfac           , or_proced
           , or_refope            , or_segges           , or_subseg       , in_fecope           , or_fecvto
           , or_idcnae_nuevo      , or_conced           , or_claviso      , or_fecaltblo        , at_descripcion_bloqueo
           , or_numpersona        , or_clunicontr_calc  , or_clunient     , or_cluniprod        , or_clunicontr
           , or_clunient_cuent    , or_clunicuent_cuent , or_clunicuent   , or_clunicuent_opera , or_cluniprod_opera
           , or_cluniopera        , or_fecprrev         , or_codprodo     , or_idecno           , or_tipodectavis
           , or_nifcifctavis      , or_numperctav       , or_tituctavista , or_desctavista      , or_persctavista
           , or_cnaectavis        , or_cnoctavis        , or_entctrvista  , or_prodctrvista     , or_ctavista_calc
           , or_disble            , or_dispto           , or_totimpume    , or_fec_alta         , sw_clientes_a_eliminar
           , sw_bcoatl            , sw_tarjeta_shopping , in_prod_score   , or_score4           , or_total_importe
           , or_saldo_posicion_pr , in_empresa_grupo    , id_cat_drc      , id_cat_drc_desc			, sw_tarjeta_particular
           , or_mt_modelo					, or_definitivo       , or_punt_final)
         VALUES
            (or_idmes             , or_idpers           , or_tipide       , or_nifcif           , or_numcta
           , or_idsituac          , or_tipotit          , or_titularitat  , or_segfac           , or_proced
           , or_refope            , or_segges           , or_subseg       , in_fecope           , or_fecvto
           , or_idcnae_nuevo      , or_conced           , or_claviso      , or_fecaltblo        , at_descripcion_bloqueo
           , or_numpersona        , or_clunicontr_calc  , or_clunient     , or_cluniprod        , or_clunicontr
           , or_clunient_cuent    , or_clunicuent_cuent , or_clunicuent   , or_clunicuent_opera , or_cluniprod_opera
           , or_cluniopera        , or_fecprrev         , or_codprodo     , or_idecno           , or_tipodectavis
           , or_nifcifctavis      , or_numperctav       , or_tituctavista , or_desctavista      , or_persctavista
           , or_cnaectavis        , or_cnoctavis        , or_entctrvista  , or_prodctrvista     , or_ctavista_calc
           , or_disble            , or_dispto           , or_totimpume    , or_fec_alta         , sw_clientes_a_eliminar
           , sw_bcoatl            , sw_tarjeta_shopping , in_prod_score   , or_score4           , or_total_importe
           , or_saldo_posicion_pr , in_empresa_grupo    , id_cat_drc      , id_cat_drc_desc			, sw_tarjeta_particular
           , or_mt_modelo					, or_definitivo       , or_punt_final)
      ELSE
         INTO dcrcalib.tr_cal_pds_tcr_bue_acu_des
            (or_idmes, or_idpers, or_tipide, or_nifcif, or_numcta, or_idsituac, or_tipotit, or_titularitat, or_segfac, or_proced, or_refope,
              or_segges, or_subseg, in_fecope, or_fecvto, or_idcnae_nuevo, or_conced, or_claviso, or_fecaltblo,
              at_descripcion_bloqueo, or_numpersona, or_clunicontr_calc, or_clunient, or_cluniprod, or_clunicontr,
              or_clunient_cuent, or_clunicuent_cuent, or_clunicuent, or_clunicuent_opera, or_cluniprod_opera, or_cluniopera,
              or_fecprrev, or_codprodo, or_idecno, or_tipodectavis, or_nifcifctavis, or_numperctav, or_tituctavista, or_desctavista, or_persctavista,
              or_cnaectavis, or_cnoctavis, or_entctrvista, or_prodctrvista, or_ctavista_calc, or_disble, or_dispto, or_totimpume,
              or_fec_alta, de_motivo, sw_tarjeta_particular, or_mt_modelo, or_definitivo, or_punt_final)
         VALUES
            (or_idmes, or_idpers, or_tipide, or_nifcif, or_numcta, or_idsituac, or_tipotit, or_titularitat, or_segfac, or_proced, or_refope,
             or_segges, or_subseg, in_fecope, or_fecvto, or_idcnae_nuevo, or_conced, or_claviso, or_fecaltblo,
             at_descripcion_bloqueo, or_numpersona, or_clunicontr_calc, or_clunient, or_cluniprod, or_clunicontr,
             or_clunient_cuent, or_clunicuent_cuent, or_clunicuent, or_clunicuent_opera, or_cluniprod_opera, or_cluniopera,
             or_fecprrev, or_codprodo, or_idecno, or_tipodectavis, or_nifcifctavis, or_numperctav, or_tituctavista, or_desctavista, or_persctavista,
             or_cnaectavis, or_cnoctavis, or_entctrvista, or_prodctrvista, or_ctavista_calc, or_disble, or_dispto, or_totimpume,
             or_fec_alta, de_motivo, sw_tarjeta_particular, or_mt_modelo, or_definitivo, or_punt_final)
   SELECT /*+ PARALLEL(A, 4) */
          a.or_idmes             , a.or_idpers           , a.or_tipide       , a.or_nifcif           , a.or_numcta
        , a.or_idsituac          , a.or_tipotit          , a.or_titularitat  , a.or_segfac           , a.or_proced
        , a.or_refope            , a.or_segges           , a.or_subseg       , a.in_fecope           , a.or_fecvto
        , a.or_idcnae_nuevo      , a.or_conced           , a.or_claviso      , a.or_fecaltblo        , a.at_descripcion_bloqueo
        , a.or_numpersona        , a.or_clunicontr_calc  , a.or_clunient     , a.or_cluniprod        , a.or_clunicontr
        , a.or_clunient_cuent    , a.or_clunicuent_cuent , a.or_clunicuent   , a.or_clunicuent_opera , a.or_cluniprod_opera
        , a.or_cluniopera        , a.or_fecprrev         , a.or_codprodo     , a.or_idecno           , a.or_tipodectavis
        , a.or_nifcifctavis      , a.or_numperctav       , a.or_tituctavista , a.or_desctavista      , a.or_persctavista
        , a.or_cnaectavis        , a.or_cnoctavis        , a.or_entctrvista  , a.or_prodctrvista     , a.or_ctavista_calc
        , a.or_disble            , a.or_dispto           , a.or_totimpume    , a.or_fec_alta         , a.sw_clientes_a_eliminar
        , a.sw_bcoatl            , sw_tarjeta_shopping   , a.in_prod_score   , a.or_score4           , a.or_total_importe
        , a.or_saldo_posicion_pr , a.in_empresa_grupo    , a.id_cat_drc      , a.id_cat_drc_desc     , or_cluniprod_recup
        , 'Descarte de las operaciones buenasbs_cal_pds_tcr_pre_acu_bue que se encuentran en el acumulado de malos en el mes actual de proceso' de_motivo
        , a.sw_tarjeta_particular, a.or_mt_modelo				 , a.or_definitivo    , a.or_punt_final
   FROM dcrcalib.bs_cal_pds_tcr_pre_acu_bue a,
        dcrcalib.bs_cal_pds_tcr_mal_acu c
   WHERE a.or_idmes = c.or_idmes (+)
     AND a.or_idmes = v_nFecha
     AND a.or_cluniprod = 'KT'
     AND a.or_titularitat = c.or_titularitat (+)
     AND a.or_cluniprod= c.or_cluniprod_recup (+)
   UNION
   SELECT /*+ PARALLEL(b, 4) */
          b.or_idmes             , b.or_idpers           , b.or_tipide        , b.or_nifcif           , b.or_numcta
        , b.or_idsituac          , b.or_tipotit          , b.or_titularitat   , b.or_segfac           , b.or_proced
        , b.or_refope            , b.or_segges           , b.or_subseg        , b.in_fecope           , b.or_fecvto
        , b.or_idcnae_nuevo      , b.or_conced           , b.or_claviso       , b.or_fecaltblo        , b.at_descripcion_bloqueo
        , b.or_numpersona        , b.or_clunicontr_calc  , b.or_clunient      , b.or_cluniprod        , b.or_clunicontr
        , b.or_clunient_cuent    , b.or_clunicuent_cuent , b.or_clunicuent    , b.or_clunicuent_opera , b.or_cluniprod_opera
        , b.or_cluniopera        , b.or_fecprrev         , b.or_codprodo      , b.or_idecno           , b.or_tipodectavis
        , b.or_nifcifctavis      , b.or_numperctav       , b.or_tituctavista  , b.or_desctavista      , b.or_persctavista
        , b.or_cnaectavis        , b.or_cnoctavis        , b.or_entctrvista   , b.or_prodctrvista     , b.or_ctavista_calc
        , b.or_disble            , b.or_dispto           , b.or_totimpume     , b.or_fec_alta         , b.sw_clientes_a_eliminar
        , b.sw_bcoatl            , sw_tarjeta_shopping   , b.in_prod_score    , b.or_score4           , b.or_total_importe
        , b.or_saldo_posicion_pr , b.in_empresa_grupo    , b.id_cat_drc       , b.id_cat_drc_desc     , or_cluniprod_recup
        , 'Descarte de las operaciones buenas que se encuentran en el acumulado de malos en el mes actual de proceso' de_motivo
        , b.sw_tarjeta_particular, b.or_mt_modelo				 , b.or_definitivo    , b.or_punt_final
   FROM dcrcalib.bs_cal_pds_tcr_pre_acu_bue b,
        dcrcalib.bs_cal_pds_tcr_mal_acu c
   WHERE b.or_idmes = c.or_idmes (+)
     AND b.or_idmes = v_nFecha
     AND b.or_cluniprod = 'TA'
     AND b.or_clunicontr_calc = c.or_clunicontr_recup (+);
   COMMIT;

-- 10 INSERT EN tr_cal_pds_tcr_bue_acu_1 DE UNA SELECT DE tr_cal_pds_tcr_pre_acu_bue_1
   vn_numerr:= 7;
   INSERT  /*+ PARALLEL (DCRCALIB.TR_CAL_pds_TCR_BUE_ACU_1,4) */
   FIRST
      WHEN sw_cnae = 1 AND sw_cno = 1 AND sw_segmento = 1 THEN -- de_particular = 1
         INTO dcrcalib.tr_cal_pds_tcr_bue_acu_1
            (or_idmes               , or_idpers           	, or_tipide          , or_nifcif       , or_numcta
           , or_tipotit             , or_titularitat      	, or_proced          , or_refope       , or_segges
           , or_subseg              , in_fecope           	, or_idcnae_nuevo    , or_claviso      , or_fecaltblo
           , at_descripcion_bloqueo , or_numpersona       	, or_clunicontr_calc , or_clunient     , or_cluniprod
           , or_clunicontr          , or_fecprrev         	, or_codprodo        , or_idecno       , or_tipodectavis
           , or_nifcifctavis        , or_numperctav       	, or_tituctavista    , or_desctavista  , or_persctavista
           , or_cnaectavis          , or_cnoctavis        	, or_entctrvista     , or_prodctrvista , or_ctavista_calc
           , or_disble              , or_dispto           	, or_totimpume       , or_fec_alta     , sw_clientes_a_eliminar
           , sw_bcoatl              , sw_tarjeta_shopping 	, in_prod_score      , or_score4       , or_total_importe
           , or_saldo_posicion_pr   , in_empresa_grupo    	, id_cat_drc         , id_cat_drc_desc , or_idsituac
           , de_particular					, sw_tarjeta_particular , or_mt_modelo			 , or_definitivo   , or_punt_final)
         VALUES
            (or_idmes               , or_idpers           	, or_tipide          , or_nifcif       , or_numcta
           , or_tipotit             , or_titularitat      	, or_proced          , or_refope       , or_segges
           , or_subseg              , in_fecope           	, or_idcnae_nuevo    , or_claviso      , or_fecaltblo
           , at_descripcion_bloqueo , or_numpersona       	, or_clunicontr_calc , or_clunient     , or_cluniprod
           , or_clunicontr          , or_fecprrev         	, or_codprodo        , or_idecno       , or_tipodectavis
           , or_nifcifctavis        , or_numperctav       	, or_tituctavista    , or_desctavista  , or_persctavista
           , or_cnaectavis          , or_cnoctavis        	, or_entctrvista     , or_prodctrvista , or_ctavista_calc
           , or_disble              , or_dispto           	, or_totimpume       , or_fec_alta     , sw_clientes_a_eliminar
           , sw_bcoatl              , sw_tarjeta_shopping 	, in_prod_score      , or_score4       , or_total_importe
           , or_saldo_posicion_pr   , in_empresa_grupo    	, id_cat_drc         , id_cat_drc_desc , or_idsituac
           , 1											, sw_tarjeta_particular , or_mt_modelo			 , or_definitivo   , or_punt_final)
      WHEN sw_cnae = 0 OR sw_cno = 0 OR sw_segmento = 0 then  -- de_particular = 0
         INTO dcrcalib.tr_cal_pds_tcr_bue_acu_1
            (or_idmes               , or_idpers           	, or_tipide          , or_nifcif       , or_numcta
           , or_tipotit             , or_titularitat      	, or_proced          , or_refope       , or_segges
           , or_subseg              , in_fecope           	, or_idcnae_nuevo    , or_claviso      , or_fecaltblo
           , at_descripcion_bloqueo , or_numpersona      	  , or_clunicontr_calc , or_clunient     , or_cluniprod
           , or_clunicontr          , or_fecprrev         	, or_codprodo        , or_idecno       , or_tipodectavis
           , or_nifcifctavis        , or_numperctav       	, or_tituctavista    , or_desctavista  , or_persctavista
           , or_cnaectavis          , or_cnoctavis        	, or_entctrvista     , or_prodctrvista , or_ctavista_calc
           , or_disble              , or_dispto           	, or_totimpume       , or_fec_alta     , sw_clientes_a_eliminar
           , sw_bcoatl              , sw_tarjeta_shopping 	, in_prod_score      , or_score4       , or_total_importe
           , or_saldo_posicion_pr   , in_empresa_grupo    	, id_cat_drc         , id_cat_drc_desc , or_idsituac
           , de_particular					, sw_tarjeta_particular , or_mt_modelo			 , or_definitivo   , or_punt_final)
         VALUES
            (or_idmes               , or_idpers           	, or_tipide          , or_nifcif       , or_numcta
           , or_tipotit             , or_titularitat      	, or_proced          , or_refope       , or_segges
           , or_subseg              , in_fecope           	, or_idcnae_nuevo    , or_claviso      , or_fecaltblo
           , at_descripcion_bloqueo , or_numpersona       	, or_clunicontr_calc , or_clunient     , or_cluniprod
           , or_clunicontr          , or_fecprrev         	, or_codprodo        , or_idecno       , or_tipodectavis
           , or_nifcifctavis        , or_numperctav       	, or_tituctavista    , or_desctavista  , or_persctavista
           , or_cnaectavis          , or_cnoctavis        	, or_entctrvista     , or_prodctrvista , or_ctavista_calc
           , or_disble              , or_dispto           	, or_totimpume       , or_fec_alta     , sw_clientes_a_eliminar
           , sw_bcoatl              , sw_tarjeta_shopping 	, in_prod_score      , or_score4       , or_total_importe
           , or_saldo_posicion_pr   , in_empresa_grupo    	, id_cat_drc         , id_cat_drc_desc , or_idsituac
           , 0											, sw_tarjeta_particular , or_mt_modelo			 , or_definitivo   , or_punt_final)
   SELECT /*+ PARALLEL (A,4) */
          a.or_idmes               , a.or_idpers           , a.or_tipide          , a.or_nifcif       , a.or_numcta
        , a.or_tipotit             , a.or_titularitat      , a.or_proced          , a.or_refope       , a.or_segges
        , a.or_subseg              , a.in_fecope           , a.or_idcnae_nuevo    , a.or_claviso      , a.or_fecaltblo
        , a.at_descripcion_bloqueo , a.or_numpersona       , a.or_clunicontr_calc , a.or_clunient     , a.or_cluniprod
        , a.or_clunicontr          , a.or_fecprrev         , a.or_codprodo        , a.or_idecno       , a.or_tipodectavis
        , a.or_nifcifctavis        , a.or_numperctav       , a.or_tituctavista    , a.or_desctavista  , a.or_persctavista
        , a.or_cnaectavis          , a.or_cnoctavis        , a.or_entctrvista     , a.or_prodctrvista , a.or_ctavista_calc
        , a.or_disble              , a.or_dispto           , a.or_totimpume       , a.or_fec_alta     , a.sw_clientes_a_eliminar
        , a.sw_bcoatl              , a.sw_tarjeta_shopping , a.in_prod_score      , a.or_score4       , a.or_total_importe
        , a.or_saldo_posicion_pr   , a.in_empresa_grupo    , a.id_cat_drc         , a.id_cat_drc_desc , a.or_idsituac
        , a.sw_tarjeta_particular	 , a.or_mt_modelo				 , a.or_definitivo    	, a.or_punt_final
        , MIN(CASE
                 WHEN NVL(a.or_idcnae_nuevo, 0) IN (9999,0, -1) THEN 1
                 ELSE 0
              END) sw_cnae
        , MIN(CASE
                 WHEN NVL(or_idecno,0) NOT IN (30, 201, 202, 203, 204, 205, 211, 212,221, 231, 232, 233, 234, 241, 242, 251,
                                               252, 253, 254, 255, 256, 257, 258, 259, 261, 262) THEN 1
                 ELSE 0
              END) sw_cno
        , MIN(CASE
                 WHEN or_segges = 1 THEN 1
                 ELSE 0
              END) sw_segmento
   FROM dcrcalib.tr_cal_pds_tcr_pre_acu_bue_1 A
   WHERE a.or_idmes = v_nFecha
   GROUP BY a.or_idmes               , a.or_idpers           , a.or_tipide          , a.or_nifcif       , a.or_numcta
          , a.or_tipotit             , a.or_titularitat      , a.or_proced          , a.or_refope       , a.or_segges
          , a.or_subseg              , a.in_fecope           , a.or_idcnae_nuevo    , a.or_claviso      , a.or_fecaltblo
          , a.at_descripcion_bloqueo , a.or_numpersona       , a.or_clunicontr_calc , a.or_clunient     , a.or_cluniprod
          , a.or_clunicontr          , a.or_fecprrev         , a.or_codprodo        , a.or_idecno       , a.or_tipodectavis
          , a.or_nifcifctavis        , a.or_numperctav       , a.or_tituctavista    , a.or_desctavista  , a.or_persctavista
          , a.or_cnaectavis          , a.or_cnoctavis        , a.or_entctrvista     , a.or_prodctrvista , a.or_ctavista_calc
          , a.or_disble              , a.or_dispto           , a.or_totimpume       , a.or_fec_alta     , a.sw_clientes_a_eliminar
          , a.sw_bcoatl              , a.sw_tarjeta_shopping , a.in_prod_score      , a.or_score4       , a.or_total_importe
          , a.or_saldo_posicion_pr   , a.in_empresa_grupo    , a.id_cat_drc         , a.id_cat_drc_desc , a.or_idsituac
          , a.sw_tarjeta_particular  , a.or_mt_modelo				 , a.or_definitivo      , a.or_punt_final;
   COMMIT;

-- 11 INSERT EN BS_CAL_CONTROL_PROCESO SI FECHA<=200707 DE tr_cal_pds_tcr_bue_acu_1
   --Marca PDCA (de_particular = 2)
   --Marca empleados banc sabadell(de_particular = 3)
   IF v_nFecha <= 200707 then
      v_nFecha_Particion := 200707;
   ELSE
      v_nFecha_Particion := v_nFecha;
   END IF;

   vn_numerr:= 8;
   INSERT INTO DCRCALIB.BS_CAL_CONTROL_PROCESO (fec_proceso, aplicacion, PROCESO, FEC_INI, ESTADO)
   VALUES (v_nFecha, vv_aplicacion, VV_PROGRAMA||' - INSERT en tr_cal_pds_tcr_bue_acu_2', SYSDATE, 'INICIADO');
   COMMIT;
   
   vn_numerr:= 9;
   INSERT /*+ append */INTO dcrcalib.tr_cal_pds_tcr_bue_acu_2
      (or_idmes               , or_idpers           	, or_tipide            , or_nifcif       , or_numcta
     , or_tipotit             , or_titularitat      	, or_proced            , or_refope       , or_segges
     , or_subseg              , in_fecope           	, or_idcnae_nuevo      , or_claviso      , or_fecaltblo
     , at_descripcion_bloqueo , or_numpersona       	, or_clunicontr_calc   , or_clunient     , or_cluniprod
     , or_clunicontr          , or_fecprrev         	, or_codprodo          , or_idecno       , or_tipodectavis
     , or_nifcifctavis        , or_numperctav       	, or_tituctavista      , or_desctavista  , or_persctavista
     , or_cnaectavis          , or_cnoctavis        	, or_entctrvista       , or_prodctrvista , or_ctavista_calc
     , or_disble              , or_dispto           	, or_totimpume         , or_fec_alta     , sw_clientes_a_eliminar
     , sw_bcoatl              , sw_tarjeta_shopping 	, in_prod_score        , or_score4       , or_total_importe
     , or_saldo_posicion_pr   , in_empresa_grupo    	, sw_contrato_operante , id_cat_drc      , id_cat_drc_desc
     , or_idsituac						, sw_tarjeta_particular , or_mt_modelo			 	 , or_definitivo   , or_punt_final
     , de_particular
     , sw_materialidad)
   SELECT a.or_idmes               , a.or_idpers           		, a.or_tipide            , a.or_nifcif       , a.or_numcta
        , a.or_tipotit             , a.or_titularitat      		, a.or_proced            , a.or_refope       , a.or_segges
        , a.or_subseg              , a.in_fecope           		, a.or_idcnae_nuevo      , a.or_claviso      , a.or_fecaltblo
        , a.at_descripcion_bloqueo , a.or_numpersona       		, a.or_clunicontr_calc   , a.or_clunient     , a.or_cluniprod
        , a.or_clunicontr          , a.or_fecprrev         		, a.or_codprodo          , a.or_idecno       , a.or_tipodectavis
        , a.or_nifcifctavis        , a.or_numperctav       		, a.or_tituctavista      , a.or_desctavista  , a.or_persctavista
        , a.or_cnaectavis          , a.or_cnoctavis        		, a.or_entctrvista       , a.or_prodctrvista , a.or_ctavista_calc
        , a.or_disble              , a.or_dispto           		, a.or_totimpume         , a.or_fec_alta     , a.sw_clientes_a_eliminar
        , a.sw_bcoatl              , a.sw_tarjeta_shopping 		, a.in_prod_score        , a.or_score4       , a.or_total_importe
        , a.or_saldo_posicion_pr   , a.in_empresa_grupo    		, e.sw_contrato_operante , a.id_cat_drc      , a.id_cat_drc_desc
        , a.or_idsituac						 , a.sw_tarjeta_particular	, a.or_mt_modelo				 , a.or_definitivo   , a.or_punt_final
        , CASE
             WHEN d.id_idefisc IS NOT NULL THEN 3
             WHEN b.or_titularitat IS NULL AND c.or_titularitat IS NULL THEN a.de_particular
             WHEN b.or_titularitat IS NOT NULL OR c.or_titularitat IS NOT NULL THEN 2
          END de_particular
        , CASE
             WHEN a.or_totimpume < f.me_import_material THEN 1
             ELSE 0
          END sw_materialidad
   FROM dcrcalib.tr_cal_pds_tcr_bue_acu_1 a
      , dcrcalib.bs_cal_pdca_malos_acu b
      , dcrcalib.bs_cal_pdca_buenos_acu c
      , dcrcalib.bs_cal_pe_funciones d
      , dcrcalib.bs_cal_pds_tcr_cto_oper_agrup e
      , dcrcalib.lk_cal_prm_materialidad f
   WHERE a.or_titularitat = b.or_titularitat(+)
     AND a.or_titularitat = c.or_titularitat(+)
     AND a.or_idmes = b.or_idmes(+)
     AND a.or_idmes = c.or_idmes(+)
     AND LTRIM(DECODE(SUBSTR(a.or_idpers, 1,2), '00', SUBSTR(a.or_idpers, 7), SUBSTR(a.or_idpers,4)),0) = LTRIM(d.id_idefisc(+),0)
     AND d.id_fch_datos (+) = v_nFecha_Particion
     AND a.or_clunicontr_calc = E.or_clunicontr_calc(+)
     AND a.or_cluniprod = E.or_cluniprod(+)
     AND a.or_idmes= E.or_idmes(+)
     AND a.or_idmes=v_nfecha
     AND de_seccion = 'TCR'
     AND sw_tipo_poblacion = 'BUENOS'
     AND (a.or_idmes <= f.id_fch_fin_vigencia OR f.id_fch_fin_vigencia IS NULL)
     AND a.or_idmes >= f.id_fch_inicio_vigencia;
     
     -- 12 RECUENTO DE FILAS MODIFICADAS POR EL INSERT ANTERIOR
	 vv_count := SQL%ROWCOUNT;
   COMMIT;

-- 13 UPDATE DE CONTROL DE PROCESO
   vn_numerr:= 10;
   UPDATE dcrcalib.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = 0
   WHERE proceso = vv_programa||' - INSERT en tr_cal_pds_tcr_bue_acu_2'
     AND estado  = 'INICIADO';
   COMMIT;

-- 14 INSERT DE CONTROL DE PROCESO
   vn_numerr:= 11;
   INSERT INTO DCRCALIB.BS_CAL_CONTROL_PROCESO (fec_proceso, aplicacion, PROCESO, FEC_INI, ESTADO)
   VALUES (v_nFecha, vv_aplicacion, VV_PROGRAMA||' - INSERT en tr_cal_pds_tcr_bue_acu_des', SYSDATE, 'INICIADO');
   COMMIT;
   
   -- 15 INSERT EN tr_cal_pds_tcr_bue_acu_des DE tr_cal_PDS_tcr_bue_acu_2
   vn_numerr:= 12;
   INSERT /*+ PARALLEL (B,4) */ INTO dcrcalib.tr_cal_pds_tcr_bue_acu_des b
    (OR_IDMES, OR_IDPERS, OR_TIPIDE, OR_NIFCIF, OR_NUMCTA, OR_TIPOTIT, OR_TITULARITAT, OR_PROCED, OR_REFOPE, OR_SEGGES,
     OR_SUBSEG, IN_FECOPE, OR_IDCNAE_NUEVO, OR_CLAVISO, OR_FECALTBLO, AT_DESCRIPCION_BLOQUEO, OR_NUMPERSONA,
     OR_CLUNICONTR_CALC, OR_CLUNIENT, OR_CLUNIPROD, OR_CLUNICONTR, OR_FECPRREV,
     OR_CODPRODO, OR_IDECNO, OR_TIPODECTAVIS, OR_NIFCIFCTAVIS, OR_NUMPERCTAV, OR_TITUCTAVISTA, OR_DESCTAVISTA, OR_PERSCTAVISTA,
     OR_CNAECTAVIS, OR_CNOCTAVIS, OR_ENTCTRVISTA, OR_PRODCTRVISTA, OR_CTAVISTA_calc, OR_DISBLE, OR_DISPTO,
     OR_TOTIMPUME, OR_FEC_ALTA, IN_PROD_SCORE, OR_SCORE4, OR_TOTAL_IMPORTE, OR_SALDO_POSICION_PR, de_particular,
     sw_tarjeta_shopping, SW_CONTRATO_OPERANTE, SW_CLIENTES_A_ELIMINAR, SW_BCOATL, sw_materialidad, de_motivo,
     sw_tarjeta_particular, or_mt_modelo, or_definitivo, or_punt_final
    )
   SELECT /*+ PARALLEL (A,4) */
     OR_IDMES, OR_IDPERS, OR_TIPIDE, OR_NIFCIF, OR_NUMCTA, OR_TIPOTIT, OR_TITULARITAT, OR_PROCED, OR_REFOPE, OR_SEGGES,
     OR_SUBSEG, IN_FECOPE, OR_IDCNAE_NUEVO, OR_CLAVISO, OR_FECALTBLO, AT_DESCRIPCION_BLOQUEO, OR_NUMPERSONA,
     OR_CLUNICONTR_CALC, OR_CLUNIENT, OR_CLUNIPROD, OR_CLUNICONTR, OR_FECPRREV, OR_CODPRODO, OR_IDECNO,
     OR_TIPODECTAVIS, OR_NIFCIFCTAVIS, OR_NUMPERCTAV, OR_TITUCTAVISTA, OR_DESCTAVISTA, OR_PERSCTAVISTA, OR_CNAECTAVIS, OR_CNOCTAVIS, OR_ENTCTRVISTA,
     OR_PRODCTRVISTA, OR_CTAVISTA_calc, OR_DISBLE, OR_DISPTO, OR_TOTIMPUME, OR_FEC_ALTA, IN_PROD_SCORE, OR_SCORE4,
     OR_TOTAL_IMPORTE, OR_SALDO_POSICION_PR, de_particular, sw_tarjeta_shopping, SW_CONTRATO_OPERANTE, SW_CLIENTES_A_ELIMINAR, SW_BCOATL,
     sw_materialidad, v_cMotivo, sw_tarjeta_particular, or_mt_modelo, or_definitivo, or_punt_final
   from DCRCALIB.tr_cal_PDS_tcr_bue_acu_2 A
   where OR_IDMES=v_nfecha
   and sw_materialidad=0;
   
   -- 16 RECUENTO DE FILAS MODIFICADAS POR EL INSERT ANTERIOR
	 vv_count := SQL%ROWCOUNT;
   COMMIT;

--17 UPDATE DE CONTROL DE PROCESO
   vn_numerr:= 13;
   UPDATE dcrcalib.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = vv_count
   WHERE proceso = vv_programa||' - INSERT en tr_cal_pds_tcr_bue_acu_des'
     AND estado  = 'INICIADO';
   COMMIT;

-- 18 INSERT DE CONTROL DE PROCESO
   vn_numerr:= 14;
   INSERT INTO DCRCALIB.BS_CAL_CONTROL_PROCESO (fec_proceso, aplicacion, PROCESO, FEC_INI, ESTADO)
   VALUES (v_nFecha, vv_aplicacion, VV_PROGRAMA||' - INSERT en tr_cal_pds_tcr_bue_acu', SYSDATE, 'INICIADO');
   COMMIT;
   -- 19 INSERT EN tr_cal_pds_tcr_bue_acu DE tr_cal_pds_tcr_bue_acu_2
   vn_numerr:= 15;
   INSERT /*+ PARALLEL (C,4) */ INTO dcrcalib.tr_cal_pds_tcr_bue_acu c
      (or_idmes               , or_idpers              , or_tipide            , or_nifcif        , or_numcta
     , or_tipotit             , or_titularitat         , or_proced            , or_refope        , or_segges
     , or_subseg              , in_fecope              , or_idcnae_nuevo      , or_claviso       , or_fecaltblo
     , at_descripcion_bloqueo , or_numpersona          , or_clunicontr_calc   , or_clunient      , or_cluniprod
     , or_clunicontr          , or_fecprrev            , or_codprodo          , or_idecno        , or_tipodectavis
     , or_nifcifctavis        , or_numperctav          , or_tituctavista      , or_desctavista   , or_persctavista
     , or_cnaectavis          , or_cnoctavis           , or_entctrvista       , or_prodctrvista  , or_ctavista_calc
     , or_disble              , or_dispto              , or_totimpume         , or_fec_alta      , in_prod_score
     , or_score4              , or_total_importe       , or_saldo_posicion_pr , de_particular    , sw_tarjeta_shopping
     , sw_contrato_operante   , sw_clientes_a_eliminar , sw_bcoatl            ,  sw_materialidad , de_operatividad
     , in_empresa_grupo       , id_cat_drc             , id_cat_drc_desc      , or_idsituac			 , sw_tarjeta_particular 
     , or_mt_modelo			 			, or_definitivo   			 , or_punt_final
     , de_tarjeta_shopping
     , de_tarjeta_resto)
   SELECT /*+ PARALLEL (B,4) */ DISTINCT 
          or_idmes               , or_idpers              , or_tipide            , or_nifcif       , or_numcta
        , or_tipotit             , or_titularitat         , or_proced            , or_refope       , or_segges
        , or_subseg              , in_fecope              , or_idcnae_nuevo      , or_claviso      , or_fecaltblo
        , at_descripcion_bloqueo , or_numpersona          , or_clunicontr_calc   , or_clunient     , or_cluniprod
        , or_clunicontr          , or_fecprrev            , or_codprodo          , or_idecno       , or_tipodectavis
        , or_nifcifctavis        , or_numperctav          , or_tituctavista      , or_desctavista  , or_persctavista
        , or_cnaectavis          , or_cnoctavis           , or_entctrvista       , or_prodctrvista , or_ctavista_calc
        , or_disble              , or_dispto              , or_totimpume         , or_fec_alta     , in_prod_score
        , or_score4              , or_total_importe       , or_saldo_posicion_pr , de_particular   , sw_tarjeta_shopping
        , sw_contrato_operante   , sw_clientes_a_eliminar , sw_bcoatl            , sw_materialidad , de_operatividad
        , in_empresa_grupo       , id_cat_drc             , id_cat_drc_desc      , or_idsituac		 , sw_tarjeta_particular 
     		, or_mt_modelo			 		 , or_definitivo   			  , or_punt_final
        , CASE
             WHEN de_tarjeta_shopping = 0 THEN 'NO TIENE'
             WHEN de_tarjeta_shopping = 1 THEN 'NO OPERANTE'
             WHEN de_tarjeta_shopping = 2 THEN 'OPERANTE NO FINANCIADA'
             WHEN de_tarjeta_shopping = 3 THEN 'OPERANTE FINANCIADA'
          END de_tarjeta_shopping
        , CASE
             WHEN de_tarjeta_resto = 0 THEN 'NO TIENE'
             WHEN de_tarjeta_resto = 1 THEN 'NO OPERANTE'
             WHEN de_tarjeta_resto = 2 THEN 'OPERANTE NO FINANCIADA'
             WHEN de_tarjeta_resto = 3 THEN 'OPERANTE FINANCIADA'
          END de_tarjeta_resto
   FROM (SELECT /*+ PARALLEL (A,4) */
                or_idmes, or_idpers, or_tipide, or_nifcif, or_numcta, or_tipotit, or_titularitat, or_proced, or_refope,
                or_segges, or_subseg, in_fecope, or_idcnae_nuevo, or_claviso, or_fecaltblo, at_descripcion_bloqueo,
                or_numpersona, or_clunicontr_calc, or_clunient, or_cluniprod, or_clunicontr, or_fecprrev,
                or_codprodo, or_idecno, or_tipodectavis, or_nifcifctavis, or_numperctav, or_tituctavista, or_desctavista, or_persctavista,
                or_cnaectavis, or_cnoctavis, or_entctrvista, or_prodctrvista, or_ctavista_calc, or_disble, or_dispto,
                or_totimpume, or_fec_alta, in_prod_score, or_score4, or_total_importe, or_saldo_posicion_pr, de_particular, sw_tarjeta_shopping,
                sw_contrato_operante,sw_clientes_a_eliminar, sw_bcoatl, sw_materialidad, id_cat_drc, id_cat_drc_desc, or_idsituac,
                sw_tarjeta_particular, or_mt_modelo, or_definitivo, or_punt_final,
                CASE
                   WHEN or_cluniprod = 'TA' AND sw_tarjeta_shopping = 0 THEN 0
                   WHEN or_cluniprod = 'TA' AND sw_tarjeta_shopping = 1 AND NVL (sw_contrato_operante, 0) = 0 THEN 1
                   WHEN or_cluniprod = 'TA' AND sw_tarjeta_shopping = 1 AND NVL (sw_contrato_operante, 0) = 1
                    AND (CASE
                            WHEN or_idmes >= 200801 AND NVL (or_saldo_posicion_pr, 0) <> 0 THEN 1
                            ELSE 0
                         END) = 0 THEN 2
                   WHEN or_cluniprod = 'TA' AND sw_tarjeta_shopping = 1 AND NVL (sw_contrato_operante, 0) = 1
                    AND (CASE
                            WHEN or_idmes >= 200801 AND NVL (or_saldo_posicion_pr, 0) <> 0 THEN 1
                            ELSE 0
                         END) <> 0 THEN 3
                END de_tarjeta_shopping,
                CASE
                   WHEN or_cluniprod = 'TA' AND sw_tarjeta_shopping = 1 THEN 0
                   WHEN or_cluniprod = 'TA' AND sw_tarjeta_shopping = 0 AND NVL (sw_contrato_operante, 0) = 0 THEN 1
                   WHEN or_cluniprod = 'TA' AND sw_tarjeta_shopping = 0 AND NVL (sw_contrato_operante, 0) = 1
                    AND (CASE
                            WHEN or_idmes >= 200801 AND NVL (or_saldo_posicion_pr, 0) <> 0 THEN 1
                            ELSE 0
                         END) = 0 THEN 2
                   WHEN or_cluniprod = 'TA' AND sw_tarjeta_shopping = 0 AND NVL (sw_contrato_operante, 0) = 1
                    AND (CASE
                            WHEN or_idmes >= 200801 AND NVL (or_saldo_posicion_pr, 0) <> 0 THEN 1
                            ELSE 0
                         END) <> 0 THEN 3
                END de_tarjeta_resto,
                CASE
                   WHEN or_cluniprod = 'KT' AND NVL(sw_contrato_operante, 0) = 0 THEN 'NO OPERANTE'
                   WHEN or_cluniprod = 'KT' AND NVL(sw_contrato_operante, 0) = 1 THEN 'OPERANTE'
                END de_operatividad, in_empresa_grupo
         FROM dcrcalib.tr_cal_pds_tcr_bue_acu_2 a
         WHERE or_idmes = v_nfecha) B;
         
         -- 20 RECUENTO DE FILAS MODIFICADAS POR INSERT ANTERIOR
	 vv_count := SQL%ROWCOUNT;
   COMMIT;
-- 21 UPDATE DE CONTROL DE PROCESOS
   vn_numerr:= 16;
   UPDATE dcrcalib.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = vv_count
   WHERE proceso = vv_programa||' - INSERT en tr_cal_pds_tcr_bue_acu'
     AND estado  = 'INICIADO';
   COMMIT;
   
   -- 21 UPDATE DE CONTROL DE PROCESO
   vn_numerr:= 17;
   UPDATE dcrcalib.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = 0
   WHERE proceso = vv_programa||' - Tratamiento población BUE_ACU (proceso datos)'
     AND estado  = 'INICIADO';
   COMMIT;

-- 22  UPDATE DE CONTROL DE PROCESO
   vn_numerr:= 18;
   UPDATE dcrcalib.bs_cal_control_proceso
   SET estado = 'FINALIZADO',
       fec_fin = SYSDATE,
       tiempo = (current_timestamp - fec_ini),
       finalizado = 'OK',
       reg_ins_ok = 0
   WHERE proceso = vv_programa||' - Generación Tratamiento BUE_ACU'
     AND estado = 'INICIADO';
   COMMIT;

-- 23 CONTROL DE EXCEPCIONES
EXCEPTION
   WHEN OTHERS THEN
      VV_MENSAJE:= SUBSTR(TO_CHAR(SQLCODE) || SQLERRM, 1, 255);
      INSERT INTO dcrcalib.bs_cal_control_proceso (fec_proceso, aplicacion, proceso, fec_ini, estado, finalizado, error_prog, num_error, error_orac, fec_fin)
      VALUES (v_nFecha, vv_aplicacion, vv_programa || ' - Generación Tratamiento BUE_ACU', SYSDATE, 'ABORTADO', 'KO', vv_programa, vn_numerr, vv_mensaje, sysdate);
      COMMIT;

--24  UPDATE DINAMICO DE CONTROL DE PROCESO
      EXECUTE IMMEDIATE '
      UPDATE dcrcalib.bs_cal_control_proceso
      SET estado = ''ABORTADO'',
          fec_fin = SYSDATE,
          tiempo = (current_timestamp - fec_ini),
          finalizado = ''KO''
      WHERE proceso like ''' || vv_programa || '%''
        AND finalizado IS NULL';
      COMMIT;
END;
/

EXIT;

