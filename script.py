// =======================================================
var idnglProfileChanged = stringIDToTypeID( "nglProfileChanged" );
    var desc1 = new ActionDescriptor();
    var iddontRecord = stringIDToTypeID( "dontRecord" );
    desc1.putBoolean( iddontRecord, true );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc1.putBoolean( idforceNotify, true );
executeAction( idnglProfileChanged, desc1, DialogModes.NO );

// =======================================================
var idhomeScreenVisibilityChanged = stringIDToTypeID( "homeScreenVisibilityChanged" );
    var desc2 = new ActionDescriptor();
    var iddontRecord = stringIDToTypeID( "dontRecord" );
    desc2.putBoolean( iddontRecord, true );
    var idforceNotify = stringIDToTypeID( "forceNotify" );
    desc2.putBoolean( idforceNotify, true );
    var idVsbl = charIDToTypeID( "Vsbl" );
    desc2.putBoolean( idVsbl, true );
executeAction( idhomeScreenVisibilityChanged, desc2, DialogModes.NO );

// =======================================================
var idinvokeCommand = stringIDToTypeID( "invokeCommand" );
    var desc3 = new ActionDescriptor();
    var idcommandID = stringIDToTypeID( "commandID" );
    desc3.putInteger( idcommandID, -683 );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc3.putBoolean( idkcanDispatchWhileModal, true );
executeAction( idinvokeCommand, desc3, DialogModes.NO );

// =======================================================
var idAdobeScriptAutomationScripts = stringIDToTypeID( "AdobeScriptAutomation Scripts" );
    var desc4 = new ActionDescriptor();
    var idjsNm = charIDToTypeID( "jsNm" );
    desc4.putString( idjsNm, """Load Files into Stack...""" );
    var idjsMs = charIDToTypeID( "jsMs" );
    desc4.putString( idjsMs, """undefined""" );
executeAction( idAdobeScriptAutomationScripts, desc4, DialogModes.NO );

// =======================================================
var idmakeFrameAnimation = stringIDToTypeID( "makeFrameAnimation" );
executeAction( idmakeFrameAnimation, undefined, DialogModes.NO );


// =======================================================
var idslct = charIDToTypeID( "slct" );
    var desc5 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref1 = new ActionReference();
        var idLyr = charIDToTypeID( "Lyr " );
        ref1.putName( idLyr, "4-1.jpg" );
    desc5.putReference( idnull, ref1 );
    var idselectionModifier = stringIDToTypeID( "selectionModifier" );
    var idselectionModifierType = stringIDToTypeID( "selectionModifierType" );
    var idaddToSelectionContinuous = stringIDToTypeID( "addToSelectionContinuous" );
    desc5.putEnumerated( idselectionModifier, idselectionModifierType, idaddToSelectionContinuous );
    var idMkVs = charIDToTypeID( "MkVs" );
    desc5.putBoolean( idMkVs, false );
    var idLyrI = charIDToTypeID( "LyrI" );
        var list1 = new ActionList();
        list1.putInteger( 3 );
        list1.putInteger( 4 );
        list1.putInteger( 5 );
        list1.putInteger( 6 );
    desc5.putList( idLyrI, list1 );
executeAction( idslct, desc5, DialogModes.NO );

// =======================================================
var idinvokeCommand = stringIDToTypeID( "invokeCommand" );
    var desc6 = new ActionDescriptor();
    var idcommandID = stringIDToTypeID( "commandID" );
    desc6.putInteger( idcommandID, 4469 );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc6.putBoolean( idkcanDispatchWhileModal, true );
executeAction( idinvokeCommand, desc6, DialogModes.NO );

// =======================================================
var idanimationFramesFromLayers = stringIDToTypeID( "animationFramesFromLayers" );
    var desc7 = new ActionDescriptor();
executeAction( idanimationFramesFromLayers, desc7, DialogModes.NO );

// =======================================================
var idslct = charIDToTypeID( "slct" );
    var desc8 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref2 = new ActionReference();
        var idanimationFrameClass = stringIDToTypeID( "animationFrameClass" );
        ref2.putIndex( idanimationFrameClass, 2 );
    desc8.putReference( idnull, ref2 );
executeAction( idslct, desc8, DialogModes.NO );

// =======================================================
var idanimationFrameExtendSelection = stringIDToTypeID( "animationFrameExtendSelection" );
    var desc9 = new ActionDescriptor();
    var idanimationToFrame = stringIDToTypeID( "animationToFrame" );
    desc9.putInteger( idanimationToFrame, 2 );
    var idanimationFramesContiguous = stringIDToTypeID( "animationFramesContiguous" );
    desc9.putBoolean( idanimationFramesContiguous, false );
executeAction( idanimationFrameExtendSelection, desc9, DialogModes.NO );

// =======================================================
var idDplc = charIDToTypeID( "Dplc" );
    var desc10 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref3 = new ActionReference();
        var idanimationFrameClass = stringIDToTypeID( "animationFrameClass" );
        var idOrdn = charIDToTypeID( "Ordn" );
        var idTrgt = charIDToTypeID( "Trgt" );
        ref3.putEnumerated( idanimationFrameClass, idOrdn, idTrgt );
    desc10.putReference( idnull, ref3 );
executeAction( idDplc, desc10, DialogModes.NO );

// =======================================================
var idmove = charIDToTypeID( "move" );
    var desc11 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref4 = new ActionReference();
        var idanimationFrameClass = stringIDToTypeID( "animationFrameClass" );
        var idOrdn = charIDToTypeID( "Ordn" );
        var idTrgt = charIDToTypeID( "Trgt" );
        ref4.putEnumerated( idanimationFrameClass, idOrdn, idTrgt );
    desc11.putReference( idnull, ref4 );
    var idT = charIDToTypeID( "T   " );
        var ref5 = new ActionReference();
        var idanimationFrameClass = stringIDToTypeID( "animationFrameClass" );
        ref5.putIndex( idanimationFrameClass, 7 );
    desc11.putReference( idT, ref5 );
executeAction( idmove, desc11, DialogModes.NO );

// =======================================================
var idslct = charIDToTypeID( "slct" );
    var desc12 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref6 = new ActionReference();
        var idanimationFrameClass = stringIDToTypeID( "animationFrameClass" );
        ref6.putIndex( idanimationFrameClass, 5 );
    desc12.putReference( idnull, ref6 );
executeAction( idslct, desc12, DialogModes.NO );

// =======================================================
var idmove = charIDToTypeID( "move" );
    var desc13 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref7 = new ActionReference();
        var idanimationFrameClass = stringIDToTypeID( "animationFrameClass" );
        var idOrdn = charIDToTypeID( "Ordn" );
        var idTrgt = charIDToTypeID( "Trgt" );
        ref7.putEnumerated( idanimationFrameClass, idOrdn, idTrgt );
    desc13.putReference( idnull, ref7 );
    var idT = charIDToTypeID( "T   " );
        var ref8 = new ActionReference();
        var idanimationFrameClass = stringIDToTypeID( "animationFrameClass" );
        ref8.putIndex( idanimationFrameClass, 7 );
    desc13.putReference( idT, ref8 );
executeAction( idmove, desc13, DialogModes.NO );

// =======================================================
var idanimationFrameExtendSelection = stringIDToTypeID( "animationFrameExtendSelection" );
    var desc14 = new ActionDescriptor();
    var idanimationToFrame = stringIDToTypeID( "animationToFrame" );
    desc14.putInteger( idanimationToFrame, 0 );
    var idanimationFramesContiguous = stringIDToTypeID( "animationFramesContiguous" );
    desc14.putBoolean( idanimationFramesContiguous, true );
executeAction( idanimationFrameExtendSelection, desc14, DialogModes.NO );

// =======================================================
var idsetd = charIDToTypeID( "setd" );
    var desc15 = new ActionDescriptor();
    var idnull = charIDToTypeID( "null" );
        var ref9 = new ActionReference();
        var idanimationFrameClass = stringIDToTypeID( "animationFrameClass" );
        var idOrdn = charIDToTypeID( "Ordn" );
        var idTrgt = charIDToTypeID( "Trgt" );
        ref9.putEnumerated( idanimationFrameClass, idOrdn, idTrgt );
    desc15.putReference( idnull, ref9 );
    var idT = charIDToTypeID( "T   " );
        var desc16 = new ActionDescriptor();
        var idanimationFrameDelay = stringIDToTypeID( "animationFrameDelay" );
        desc16.putDouble( idanimationFrameDelay, 0.200000 );
    var idanimationFrameClass = stringIDToTypeID( "animationFrameClass" );
    desc15.putObject( idT, idanimationFrameClass, desc16 );
executeAction( idsetd, desc15, DialogModes.NO );

// =======================================================
var idinvokeCommand = stringIDToTypeID( "invokeCommand" );
    var desc17 = new ActionDescriptor();
    var idcommandID = stringIDToTypeID( "commandID" );
    desc17.putInteger( idcommandID, 1695 );
    var idkcanDispatchWhileModal = stringIDToTypeID( "kcanDispatchWhileModal" );
    desc17.putBoolean( idkcanDispatchWhileModal, true );
executeAction( idinvokeCommand, desc17, DialogModes.NO );

// =======================================================
var idExpr = charIDToTypeID( "Expr" );
    var desc18 = new ActionDescriptor();
    var idUsng = charIDToTypeID( "Usng" );
        var desc19 = new ActionDescriptor();
        var idOp = charIDToTypeID( "Op  " );
        var idSWOp = charIDToTypeID( "SWOp" );
        var idOpSa = charIDToTypeID( "OpSa" );
        desc19.putEnumerated( idOp, idSWOp, idOpSa );
        var idDIDr = charIDToTypeID( "DIDr" );
        desc19.putBoolean( idDIDr, true );
        var idIn = charIDToTypeID( "In  " );
        desc19.putPath( idIn, new File( "C:\\Users\\Antoine\\Pictures\\Parallax" ) );
        var idFmt = charIDToTypeID( "Fmt " );
        var idIRFm = charIDToTypeID( "IRFm" );
        var idGIFf = charIDToTypeID( "GIFf" );
        desc19.putEnumerated( idFmt, idIRFm, idGIFf );
        var idIntr = charIDToTypeID( "Intr" );
        desc19.putBoolean( idIntr, false );
        var idRedA = charIDToTypeID( "RedA" );
        var idIRRd = charIDToTypeID( "IRRd" );
        var idSltv = charIDToTypeID( "Sltv" );
        desc19.putEnumerated( idRedA, idIRRd, idSltv );
        var idRChT = charIDToTypeID( "RChT" );
        desc19.putBoolean( idRChT, false );
        var idRChV = charIDToTypeID( "RChV" );
        desc19.putBoolean( idRChV, false );
        var idAuRd = charIDToTypeID( "AuRd" );
        desc19.putBoolean( idAuRd, false );
        var idNCol = charIDToTypeID( "NCol" );
        desc19.putInteger( idNCol, 256 );
        var idDChS = charIDToTypeID( "DChS" );
        desc19.putInteger( idDChS, 0 );
        var idDCUI = charIDToTypeID( "DCUI" );
        desc19.putInteger( idDCUI, 0 );
        var idDChT = charIDToTypeID( "DChT" );
        desc19.putBoolean( idDChT, false );
        var idDChV = charIDToTypeID( "DChV" );
        desc19.putBoolean( idDChV, false );
        var idWebS = charIDToTypeID( "WebS" );
        desc19.putInteger( idWebS, 0 );
        var idTDth = charIDToTypeID( "TDth" );
        var idIRDt = charIDToTypeID( "IRDt" );
        var idNone = charIDToTypeID( "None" );
        desc19.putEnumerated( idTDth, idIRDt, idNone );
        var idTDtA = charIDToTypeID( "TDtA" );
        desc19.putInteger( idTDtA, 100 );
        var idLoss = charIDToTypeID( "Loss" );
        desc19.putInteger( idLoss, 0 );
        var idLChS = charIDToTypeID( "LChS" );
        desc19.putInteger( idLChS, 0 );
        var idLCUI = charIDToTypeID( "LCUI" );
        desc19.putInteger( idLCUI, 100 );
        var idLChT = charIDToTypeID( "LChT" );
        desc19.putBoolean( idLChT, false );
        var idLChV = charIDToTypeID( "LChV" );
        desc19.putBoolean( idLChV, false );
        var idTrns = charIDToTypeID( "Trns" );
        desc19.putBoolean( idTrns, true );
        var idMtt = charIDToTypeID( "Mtt " );
        desc19.putBoolean( idMtt, true );
        var idDthr = charIDToTypeID( "Dthr" );
        var idIRDt = charIDToTypeID( "IRDt" );
        var idDfsn = charIDToTypeID( "Dfsn" );
        desc19.putEnumerated( idDthr, idIRDt, idDfsn );
        var idDthA = charIDToTypeID( "DthA" );
        desc19.putInteger( idDthA, 100 );
        var idMttR = charIDToTypeID( "MttR" );
        desc19.putInteger( idMttR, 255 );
        var idMttG = charIDToTypeID( "MttG" );
        desc19.putInteger( idMttG, 255 );
        var idMttB = charIDToTypeID( "MttB" );
        desc19.putInteger( idMttB, 255 );
        var idSHTM = charIDToTypeID( "SHTM" );
        desc19.putBoolean( idSHTM, false );
        var idSImg = charIDToTypeID( "SImg" );
        desc19.putBoolean( idSImg, true );
        var idSWsl = charIDToTypeID( "SWsl" );
        var idSTsl = charIDToTypeID( "STsl" );
        var idSLAl = charIDToTypeID( "SLAl" );
        desc19.putEnumerated( idSWsl, idSTsl, idSLAl );
        var idSWch = charIDToTypeID( "SWch" );
        var idSTch = charIDToTypeID( "STch" );
        var idCHsR = charIDToTypeID( "CHsR" );
        desc19.putEnumerated( idSWch, idSTch, idCHsR );
        var idSWmd = charIDToTypeID( "SWmd" );
        var idSTmd = charIDToTypeID( "STmd" );
        var idMDCC = charIDToTypeID( "MDCC" );
        desc19.putEnumerated( idSWmd, idSTmd, idMDCC );
        var idohXH = charIDToTypeID( "ohXH" );
        desc19.putBoolean( idohXH, false );
        var idohIC = charIDToTypeID( "ohIC" );
        desc19.putBoolean( idohIC, true );
        var idohAA = charIDToTypeID( "ohAA" );
        desc19.putBoolean( idohAA, true );
        var idohQA = charIDToTypeID( "ohQA" );
        desc19.putBoolean( idohQA, true );
        var idohCA = charIDToTypeID( "ohCA" );
        desc19.putBoolean( idohCA, false );
        var idohIZ = charIDToTypeID( "ohIZ" );
        desc19.putBoolean( idohIZ, true );
        var idohTC = charIDToTypeID( "ohTC" );
        var idSToc = charIDToTypeID( "SToc" );
        var idOCzerothree = charIDToTypeID( "OC03" );
        desc19.putEnumerated( idohTC, idSToc, idOCzerothree );
        var idohAC = charIDToTypeID( "ohAC" );
        var idSToc = charIDToTypeID( "SToc" );
        var idOCzerothree = charIDToTypeID( "OC03" );
        desc19.putEnumerated( idohAC, idSToc, idOCzerothree );
        var idohIn = charIDToTypeID( "ohIn" );
        desc19.putInteger( idohIn, -1 );
        var idohLE = charIDToTypeID( "ohLE" );
        var idSTle = charIDToTypeID( "STle" );
        var idLEzerothree = charIDToTypeID( "LE03" );
        desc19.putEnumerated( idohLE, idSTle, idLEzerothree );
        var idohEn = charIDToTypeID( "ohEn" );
        var idSTen = charIDToTypeID( "STen" );
        var idENzerozero = charIDToTypeID( "EN00" );
        desc19.putEnumerated( idohEn, idSTen, idENzerozero );
        var idolCS = charIDToTypeID( "olCS" );
        desc19.putBoolean( idolCS, false );
        var idolEC = charIDToTypeID( "olEC" );
        var idSTst = charIDToTypeID( "STst" );
        var idSTzerozero = charIDToTypeID( "ST00" );
        desc19.putEnumerated( idolEC, idSTst, idSTzerozero );
        var idolWH = charIDToTypeID( "olWH" );
        var idSTwh = charIDToTypeID( "STwh" );
        var idWHzeroone = charIDToTypeID( "WH01" );
        desc19.putEnumerated( idolWH, idSTwh, idWHzeroone );
        var idolSV = charIDToTypeID( "olSV" );
        var idSTsp = charIDToTypeID( "STsp" );
        var idSPzerofour = charIDToTypeID( "SP04" );
        desc19.putEnumerated( idolSV, idSTsp, idSPzerofour );
        var idolSH = charIDToTypeID( "olSH" );
        var idSTsp = charIDToTypeID( "STsp" );
        var idSPzerofour = charIDToTypeID( "SP04" );
        desc19.putEnumerated( idolSH, idSTsp, idSPzerofour );
        var idolNC = charIDToTypeID( "olNC" );
            var list2 = new ActionList();
                var desc20 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzerozero = charIDToTypeID( "NC00" );
                desc20.putEnumerated( idncTp, idSTnc, idNCzerozero );
            var idSCnc = charIDToTypeID( "SCnc" );
            list2.putObject( idSCnc, desc20 );
                var desc21 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNConenine = charIDToTypeID( "NC19" );
                desc21.putEnumerated( idncTp, idSTnc, idNConenine );
            var idSCnc = charIDToTypeID( "SCnc" );
            list2.putObject( idSCnc, desc21 );
                var desc22 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwoeight = charIDToTypeID( "NC28" );
                desc22.putEnumerated( idncTp, idSTnc, idNCtwoeight );
            var idSCnc = charIDToTypeID( "SCnc" );
            list2.putObject( idSCnc, desc22 );
                var desc23 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc23.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list2.putObject( idSCnc, desc23 );
                var desc24 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc24.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list2.putObject( idSCnc, desc24 );
                var desc25 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc25.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list2.putObject( idSCnc, desc25 );
        desc19.putList( idolNC, list2 );
        var idobIA = charIDToTypeID( "obIA" );
        desc19.putBoolean( idobIA, false );
        var idobIP = charIDToTypeID( "obIP" );
        desc19.putString( idobIP, """""" );
        var idobCS = charIDToTypeID( "obCS" );
        var idSTcs = charIDToTypeID( "STcs" );
        var idCSzeroone = charIDToTypeID( "CS01" );
        desc19.putEnumerated( idobCS, idSTcs, idCSzeroone );
        var idovNC = charIDToTypeID( "ovNC" );
            var list3 = new ActionList();
                var desc26 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzeroone = charIDToTypeID( "NC01" );
                desc26.putEnumerated( idncTp, idSTnc, idNCzeroone );
            var idSCnc = charIDToTypeID( "SCnc" );
            list3.putObject( idSCnc, desc26 );
                var desc27 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwozero = charIDToTypeID( "NC20" );
                desc27.putEnumerated( idncTp, idSTnc, idNCtwozero );
            var idSCnc = charIDToTypeID( "SCnc" );
            list3.putObject( idSCnc, desc27 );
                var desc28 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzerotwo = charIDToTypeID( "NC02" );
                desc28.putEnumerated( idncTp, idSTnc, idNCzerotwo );
            var idSCnc = charIDToTypeID( "SCnc" );
            list3.putObject( idSCnc, desc28 );
                var desc29 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNConenine = charIDToTypeID( "NC19" );
                desc29.putEnumerated( idncTp, idSTnc, idNConenine );
            var idSCnc = charIDToTypeID( "SCnc" );
            list3.putObject( idSCnc, desc29 );
                var desc30 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCzerosix = charIDToTypeID( "NC06" );
                desc30.putEnumerated( idncTp, idSTnc, idNCzerosix );
            var idSCnc = charIDToTypeID( "SCnc" );
            list3.putObject( idSCnc, desc30 );
                var desc31 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc31.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list3.putObject( idSCnc, desc31 );
                var desc32 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc32.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list3.putObject( idSCnc, desc32 );
                var desc33 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwofour = charIDToTypeID( "NC24" );
                desc33.putEnumerated( idncTp, idSTnc, idNCtwofour );
            var idSCnc = charIDToTypeID( "SCnc" );
            list3.putObject( idSCnc, desc33 );
                var desc34 = new ActionDescriptor();
                var idncTp = charIDToTypeID( "ncTp" );
                var idSTnc = charIDToTypeID( "STnc" );
                var idNCtwotwo = charIDToTypeID( "NC22" );
                desc34.putEnumerated( idncTp, idSTnc, idNCtwotwo );
            var idSCnc = charIDToTypeID( "SCnc" );
            list3.putObject( idSCnc, desc34 );
        desc19.putList( idovNC, list3 );
        var idovCM = charIDToTypeID( "ovCM" );
        desc19.putBoolean( idovCM, false );
        var idovCW = charIDToTypeID( "ovCW" );
        desc19.putBoolean( idovCW, true );
        var idovCU = charIDToTypeID( "ovCU" );
        desc19.putBoolean( idovCU, true );
        var idovSF = charIDToTypeID( "ovSF" );
        desc19.putBoolean( idovSF, true );
        var idovCB = charIDToTypeID( "ovCB" );
        desc19.putBoolean( idovCB, true );
        var idovSN = charIDToTypeID( "ovSN" );
        desc19.putString( idovSN, """images""" );
    var idSaveForWeb = stringIDToTypeID( "SaveForWeb" );
    desc18.putObject( idUsng, idSaveForWeb, desc19 );
executeAction( idExpr, desc18, DialogModes.NO );
