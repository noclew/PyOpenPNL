#!/usr/bin/env python
import openpnl

# Still broken ...

model = openpnl.pnlExCreateRndArHMM()
pArHMM = openpnl.CDBN_Create(model)
pInfEng = openpnl.C1_5SliceJtreeInfEngine_Create(pArHMM)
nTimeSeries = 500
nSlices = [0]*nTimeSeries
pEvidences = openpnl.newCEvidences(nTimeSeries)

#openpnl.pnlRand(nTimeSeries, pEvidences.front(), 3, 20)

## set up evidence ...
for i in range(0,nTimeSeries):
    ev = openpnl.mkEvidence( pArHMM, [1], [1.0] );
    openpnl.assignEvidence( pEvidences, ev, i )

evidencesOut = openpnl.pEvidencesVecVector();
#pArHMM.GenerateSamples(evidencesOut,openpnl.toIntVector(nSlices))

pDBN = openpnl.CDBN.Create(openpnl.pnlExCreateRndArHMM());
pLearn = openpnl.CEMLearningEngineDBN.Create( pDBN );
pLearn.SetData(evidencesOut)
#pLearn.Learn()
