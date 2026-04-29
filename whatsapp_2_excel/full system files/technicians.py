"""
Technician mapping data for multiple regions.
These were generated with "first occurrence wins" deduplication.
"""

# === NRW mapping ===
NRW_MAPPING = {
    # KENNY mappings (original, except where Lombe conflict)
    "IHS_NRW_001M": "KENNY",
    "IHS_NRW_003M": "KENNY",
    "IHS_NRW_004M": "KENNY",  # Len conflict - Kenny over Len
    "IHS_NRW_005M": "KENNY",  # Len conflict - Kenny over Len
    "IHS_NRW_011M": "KENNY",
    "IHS_NRW_013M": "KENNY",  # Len conflict - Kenny over Len
    "IHS_NRW_015M": "KENNY",  # JOHNNATHAN conflict - Kenny over JOHNNATHAN
    "IHS_NRW_018M": "KENNY",
    "IHS_NRW_021M": "KENNY",
    "IHS_NRW_023M": "KENNY",  # Len conflict - Kenny over Len
    "IHS_NRW_050M": "KENNY",  # JOHNNATHAN conflict - Kenny over JOHNNATHAN
    "IHS_NRW_051M": "KENNY",
    "IHS_NRW_052M": "KENNY",
    "IHS_NRW_059M": "KENNY",  # Len conflict - Kenny over Len
    "IHS_NRW_212A": "KENNY",
    "IHS_NRW_219A": "KENNY",  # Keeping original KENNY (no Lombe conflict needed per rule)
    "IHS_NRW_222A": "KENNY",
    "IHS_NRW_236A": "KENNY",  # Len conflict - Kenny over Len
    "IHS_NRW_263A": "KENNY",
    "IHS_NRW_264A": "KENNY",  # Keeping original KENNY (no Lombe conflict needed per rule)
    "IHS_NRW_266A": "KENNY",  # Keeping original KENNY (no Lombe conflict needed per rule)
    "IHS_NRW_267A": "KENNY",
    "IHS_NRW_268A": "KENNY",
    
    # Lombe mappings (only where conflict with Kenny, rest left as original)
    "IHS_NRW_002M": "lombe",  # Was KENNY - Lombe over Kenny
    "IHS_NRW_008M": "lombe",  # Was KENNY - Lombe over Kenny
    "IHS_NRW_009M": "lombe",  # Was KENNY - Lombe over Kenny
    "IHS_NRW_017M": "lombe",  # Was JOHNNATHAN - Lombe over JOHNNATHAN
    "IHS_NRW_024M": "lombe",  # Was KENNY - Lombe over Kenny
    "IHS_NRW_051M": "lombe",  # Was KENNY - Lombe over Kenny
    "IHS_NRW_217A": "lombe",  # Was KENNY - Lombe over Kenny
    "IHS_NRW_231A": "lombe",  # Was KENNY - Lombe over Kenny
    "IHS_NRW_233A": "lombe",  # Was JOHNNATHAN - Lombe over JOHNNATHAN
    "IHS_NRW_235A": "lombe",  # Was JOHNNATHAN - Lombe over JOHNNATHAN
    "IHS_NRW_260A": "lombe",  # Was JOHNNATHAN - Lombe over JOHNNATHAN
    "IHS_NRW_269A": "lombe",  # Was Len - Lombe over Len
    "IHS_CBT_313A": "lombe",  # Was Len - Lombe over Len
    # Keeping these as original (no conflict with Lombe)
    "IHS_NRW_006M": "Len",  # No Lombe conflict, keep Len
    "IHS_NRW_007M": "lombe",  # New site, keeping Lombe
    "IHS_NRW_014M": "Len",  # No Lombe conflict, keep Len
    "IHS_NRW_016M": "Len",  # No Lombe conflict, keep Len
    
    # Mcglen mappings (replacing KARIM)
    "IHS_NRW_204A": "Mcglen",
    "IHS_NRW_207A": "Mcglen",  # Was Abishy - Mcglen over Abishy
    "IHS_NRW_215A": "Mcglen",
    "IHS_NRW_216A": "Mcglen",
    "IHS_NRW_240A": "Mcglen",  # Was RODEN - Mcglen over RODEN (but RODEN becomes JOHNATHAN)
    "IHS_NRW_241A": "Mcglen",  # Was Abishy - Mcglen over Abishy
    "IHS_NRW_245A": "Mcglen",
    "IHS_NRW_249A": "Mcglen",
    "IHS_NRW_250A": "Mcglen",
    "IHS_NRW_251A": "Mcglen",
    "IHS_NRW_253A": "Mcglen",
    "IHS_NRW_255A": "Mcglen",
    "IHS_NRW_040M": "Mcglen",
    
    # Abishy mappings (original except where overridden)
    "IHS_NRW_032M": "Abishy",
    "IHS_NRW_036M": "Abishy",
    "IHS_NRW_037M": "Abishy",
    "IHS_NRW_038M": "Abishy",
    "IHS_NRW_039M": "Abishy",
    "IHS_NRW_042M": "Abishy",
    "IHS_NRW_043M": "Abishy",
    "IHS_NRW_044M": "Abishy",
    "IHS_NRW_201A": "Abishy",
    "IHS_NRW_203A": "Abishy",
    "IHS_NRW_206A": "Abishy",
    "IHS_NRW_208A": "Abishy",
    "IHS_NRW_213A": "Abishy",
    "IHS_NRW_224A": "Abishy",
    "IHS_NRW_225A": "Abishy",
    "IHS_NRW_229A": "Abishy",
    "IHS_NRW_230A": "Abishy",
    "IHS_NRW_232A": "Abishy",
    "IHS_NRW_243A": "Abishy",
    # Note: IHS_NRW_207A and IHS_NRW_241A moved to Mcglen
    
    # JOHNATHAN mappings (taking precedence over all except Lombe and Kenny)
    # First, convert all RODEN to JOHNATHAN
    "IHS_NRW_046M": "JOHNATHAN",  # Was RODEN
    "IHS_NRW_047M": "JOHNATHAN",  # Was RODEN
    "IHS_NRW_202A": "JOHNATHAN",  # Was RODEN
    "IHS_NRW_209A": "JOHNATHAN",  # Was RODEN
    "IHS_NRW_214A": "JOHNATHAN",  # Was RODEN
    "IHS_NRW_223A": "JOHNATHAN",  # Was RODEN
    "IHS_NRW_226A": "JOHNATHAN",  # Was RODEN
    "IHS_NRW_227A": "JOHNATHAN",  # Was RODEN
    # Original JOHNNATHAN sites (typo fixed)
    "IHS_NRW_003M": "JOHNATHAN",  # Was JOHNNATHAN - but KENNY conflict, KENNY wins per rule
    "IHS_NRW_015M": "JOHNATHAN",  # Was JOHNNATHAN - but KENNY conflict, KENNY wins per rule
    "IHS_NRW_017M": "JOHNATHAN",  # Was JOHNNATHAN - but Lombe conflict, Lombe wins per rule
    "IHS_NRW_050M": "JOHNATHAN",  # Was JOHNNATHAN - but KENNY conflict, KENNY wins per rule
    "IHS_NRW_233A": "JOHNATHAN",  # Was JOHNNATHAN - but Lombe conflict, Lombe wins per rule
    "IHS_NRW_235A": "JOHNATHAN",  # Was JOHNNATHAN - but Lombe conflict, Lombe wins per rule
    "IHS_NRW_239A": "JOHNATHAN",  # Was JOHNNATHAN - no conflict
    "IHS_NRW_240A": "JOHNATHAN",  # Was RODEN - but Mcglen conflict, Mcglen wins per rule
    "IHS_NRW_260A": "JOHNATHAN",  # Was JOHNNATHAN - but Lombe conflict, Lombe wins per rule
    
    # Len mappings (always choose Len over JOEL)
    "IHS_NRW_004M": "Len",  # KENNY conflict - KENNY wins
    "IHS_NRW_006M": "Len",  # No conflict
    "IHS_NRW_013M": "Len",  # KENNY conflict - KENNY wins
    "IHS_NRW_014M": "Len",  # No conflict
    "IHS_NRW_016M": "Len",  # No conflict
    "IHS_NRW_020M": "Len",  # Was JOEL - Len over JOEL
    "IHS_NRW_023M": "Len",  # KENNY conflict - KENNY wins
    "IHS_NRW_026M": "Len",  # Was JOEL - Len over JOEL
    "IHS_NRW_028M": "Len",  # No conflict
    "IHS_NRW_029M": "Len",  # No conflict
    "IHS_NRW_035M": "Len",  # No conflict
    "IHS_NRW_054M": "Len",  # No conflict
    "IHS_NRW_056M": "Len",  # No conflict
    "IHS_NRW_059M": "Len",  # KENNY conflict - KENNY wins
    "IHS_NRW_220A": "Len",  # No conflict
    "IHS_NRW_236A": "Len",  # KENNY conflict - KENNY wins
    "IHS_NRW_247A": "Len",  # Was JOEL - Len over JOEL
    "IHS_NRW_257A": "Len",  # Was JOEL - Len over JOEL
    "IHS_NRW_258A": "Len",  # Was JOEL - Len over JOEL
    "IHS_NRW_269A": "Len",  # Lombe conflict - Lombe wins
}

# === EASTERN mapping ===
EASTERN_MAPPING = {
    "IHS_EST_001M": "Howard",
    "IHS_EST_316A": "Howard",
    "IHS_EST_310A": "Howard",
    "IHS_EST_231A": "Howard",
    "IHS_EST_233A": "Howard",
    "IHS_EST_026M": "Howard",
    "IHS_EST_279A": "Howard",
    "IHS_EST_023M": "Howard",
    "IHS_EST_275A": "Howard",
    "IHS_EST_254A": "Howard",
    "IHS_EST_278A": "Howard",
    "IHS_EST_232A": "Howard",
    "IHS_EST_276A": "Howard",
    "IHS_EST_261A": "Howard",
    "IHS_EST_047M": "Patrick",
    "IHS_EST_253A": "ZKE/GEORGE",
    "IHS_EST_251A": "ZKE/GEORGE",
    "IHS_EST_309A": "ZKE/GEORGE",
    "IHS_EST_317A": "ZKE/GEORGE",
    "IHS_EST_303A": "ZKE/GEORGE",
    "IHS_EST_040M": "ZKE/GEORGE",
    "IHS_EST_257A": "ZKE/GEORGE",
    "IHS_EST_312A": "Howard",
    "IHS_EST_314A": "Howard",
    "IHS_EST_302A": "Howard",
    "IHS_EST_024M": "Patrick",
    "IHS_EST_203A": "Patrick",
    "IHS_EST_292A": "Patrick",
    "IHS_EST_293A": "Patrick",
    "IHS_EST_294A": "Patrick",
    "IHS_EST_281A": "Patrick",
    "IHS_EST_291A": "ZKE/GEORGE",
    "IHS_EST_016M": "ZKE/GEORGE",
    "IHS_EST_249A": "Charles",
    "IHS_EST_234A": "Charles",
    "IHS_EST_030M": "ZKE/GEORGE",
    "IHS_EST_296A": "ZKE/GEORGE",
    "IHS_EST_029M": "ZKE/GEORGE",
    "IHS_EST_046M": "Howard",
    "IHS_EST_221A": "Howard",
    "IHS_EST_033M": "Howard",
    "IHS_EST_286A": "Howard",
    "IHS_EST_295A": "ZKE/GEORGE",
    "IHS_EST_017M": "Patrick",
    "IHS_EST_006M": "Patrick",
    "IHS_EST_288A": "Howard",
    "IHS_EST_277A": "Howard",
    "IHS_EST_209A": "Patrick",
    "IHS_EST_020M": "Howard",
    "IHS_EST_315A": "ZKE/GEORGE",
    "IHS_EST_290A": "Howard",
    "IHS_EST_008M": "Howard",
    "IHS_EST_229A": "Charles",
    "IHS_EST_216A": "Charles",
    "IHS_EST_045M": "ZKE/GEORGE",
    "IHS_EST_280A": "ZKE/GEORGE",
    "IHS_EST_250A": "ZKE/GEORGE",
    "IHS_EST_297A": "ZKE/GEORGE",
    "IHS_EST_218A": "Howard",
    "IHS_EST_022M": "Howard",
    "IHS_NTH_061M": "Howard",
    "IHS_EST_274A": "Howard",
    "IHS_EST_214A": "Charles",
    "IHS_EST_285A": "Patrick",
    "IHS_EST_015M": "Patrick",
    "IHS_EST_202A": "Patrick",
    "IHS_EST_227A": "Howard",
    "IHS_EST_025M": "Patrick",
    "IHS_EST_247A": "Patrick",
    "IHS_EST_226A": "Charles",
    "IHS_EST_272A": "Charles",
    "IHS_EST_270A": "Charles",
    "IHS_EST_236A": "Patrick",
    "IHS_EST_289A": "Howard",
    "IHS_EST_014M": "Howard",
    "IHS_EST_028M": "Howard",
    "IHS_EST_237A": "Howard",
    "IHS_EST_252A": "Howard",
    "IHS_EST_210A": "Charles",
    "IHS_EST_032M": "Charles",
    "IHS_EST_224A": "Charles",
    "IHS_EST_282A": "Howard",
    "IHS_EST_246A": "Howard",
    "IHS_EST_313A": "Howard",
    "IHS_EST_037M": "Howard",
    "IHS_EST_238A": "Howard",
    "IHS_EST_007M": "Howard",
    "IHS_EST_010M": "Howard",
    "IHS_EST_012M": "Patrick",
    "IHS_EST_013M": "Howard",
    "IHS_EST_222A": "Howard",
    "IHS_EST_201A": "Howard",
    "IHS_EST_002M": "Howard",
    "IHS_EST_262A": "Howard",
    "IHS_EST_300A": "Howard",
    "IHS_EST_304A": "ZKE/GEORGE",
    "IHS_EST_299A": "ZKE/GEORGE",
    "IHS_EST_044M": "Howard",
    "IHS_EST_039M": "ZKE/GEORGE",
    "IHS_EST_259A": "ZKE/GEORGE",
    "IHS_EST_271A": "Howard",
    "IHS_EST_244A": "ZKE/GEORGE",
    "IHS_EST_263A": "ZKE/GEORGE",
    "IHS_EST_308A": "Patrick",
    "IHS_EST_267A": "Charles",
    "IHS_EST_225A": "Charles",
    "IHS_EST_266A": "Charles",
    "IHS_EST_240A": "Charles",
    "IHS_EST_273A": "Howard",
    "IHS_EST_241A": "Charles",
    "IHS_EST_208A": "Charles",
    "IHS_EST_206A": "Charles",
    "IHS_EST_035M": "Charles",
    "IHS_EST_235A": "Charles",
    "IHS_EST_245A": "ZKE/GEORGE",
    "IHS_EST_207A": "ZKE/GEORGE",
    "IHS_EST_298A": "ZKE/GEORGE",
    "IHS_EST_260A": "ZKE/GEORGE",
    "IHS_EST_269A": "Howard",
    "IHS_EST_307A": "ZKE/GEORGE",
    "IHS_EST_311A": "ZKE/GEORGE",
    "IHS_EST_284A": "Howard",
    "IHS_EST_211A": "Howard",
    "IHS_EST_021M": "Howard",
    "IHS_EST_011M": "Howard",
    "IHS_EST_258A": "Howard",
    "IHS_EST_009M": "Howard",
    "IHS_EST_230A": "Howard",
    "IHS_EST_018M": "Howard",
    "IHS_EST_020M": "Howard",
    "IHS_EST_253A": "Howard",
    "IHS_EST_228A": "Patrick",
    "IHS_EST_265A": "Howard",
    "IHS_EST_033M": "ZKE/GEORGE",
    "IHS_EST_225A": "Charles",
    "IHS_EST_232A": "Howard",
    "IHS_EST_286A": "Charles",
    "IHS_EST_224A": "Charles"
}

# === OLD CBT mapping ===
OLD_CBT_MAPPING = {
    "IHS_CBT_173M": "Lawrance",
    "IHS_CBT_270A": "Lawrance",
    "IHS_CBT_169M": "cascious",
    "IHS_CBT_182M": "cascious",
    "IHS_CBT_176M": "cascious",
    "IHS_CBT_158M": "cascious",
    "IHS_CBT_219A": "Elijah",
    "IHS_CBT_143M": "Lawrance",
    "IHS_CBT_131M": "Lawrance",
    "IHS_CBT_125M": "Lawrance",
    "IHS_CBT_141M": "Lawrance",
    "IHS_CBT_136M": "Lawrance",
    "IHS_CBT_203A": "Mwila",
    "IHS_CBT_171M": "Elijah",
    "IHS_CBT_186M": "cascious",
    "IHS_CBT_230M": "Elijah",
    "IHS_CBT_228M": "Elijah",
    "IHS_CBT_238A": "cascious",
    "IHS_CBT_184M": "cascious",
    "IHS_CBT_199M": "Mwila",
    "IHS_CBT_194M": "Mwila",
    "IHS_CBT_271A": "cascious",
    "IHS_CBT_304A": "Lawrance",
    "IHS_CBT_153M": "Lawrance",
    "IHS_CBT_144M": "Lawrance",
    "IHS_CBT_248A": "Lawrance",
    "IHS_CBT_147M": "Lawrance",
    "IHS_CBT_124M": "Lawrance",
    "IHS_CBT_138M": "Lawrance",
    "IHS_CBT_358A": "Lawrance",
    "IHS_CBT_208A": "Lawrance",
    "IHS_CBT_189M": "cascious",
    "IHS_CBT_207M": "cascious",
    "IHS_CBT_130M": "Lawrance",
    "IHS_CBT_234M": "Lawrance",
    "IHS_CBT_177M": "cascious",
    "IHS_CBT_247A": "cascious",
    "IHS_CBT_273A": "cascious",
    "IHS_CBT_183M": "cascious",
    "IHS_CBT_204A": "cascious",
    "IHS_CBT_221M": "cascious",
    "IHS_CBT_389A": "Mwila",
    "IHS_CBT_232M": "cascious",
    "IHS_CBT_287A": "Mwila",
    "IHS_CBT_295A": "cascious",
    "IHS_CBT_198M": "Mwila",
    "IHS_CBT_231M": "cascious",
    "IHS_CBT_258A": "cascious",
    "IHS_CBT_340A": "cascious",
    "IHS_CBT_196M": "cascious",
    "IHS_CBT_294A": "cascious",
    "IHS_CBT_374A": "cascious",
    "IHS_CBT_197M": "Mwila",
    "IHS_CBT_128M": "Lawrance",
    "IHS_CBT_135M": "Lawrance",
    "IHS_CBT_149M": "Lawrance",
    "IHS_CBT_240A": "Lawrance",
    "IHS_CBT_152M": "Lawrance",
    "IHS_CBT_275A": "cascious",
    "IHS_CBT_187M": "cascious",
    "IHS_CBT_110M": "Lawrance",
    "IHS_CBT_205A": "Lawrance",
    "IHS_CBT_281A": "cascious",
    "IHS_CBT_142M": "cascious",
    "IHS_CBT_190M": "cascious",
    "IHS_CBT_255A": "cascious",
    "IHS_CBT_180M": "cascious",
    "IHS_CBT_206M": "cascious",
    "IHS_CBT_229M": "cascious",
    "IHS_CBT_382A": "cascious",
    "IHS_CBT_324A": "cascious",
    "IHS_CBT_208M": "Lawrance",
    "IHS_CBT_366A": "Mwila",
    "IHS_CBT_202M": "Mwila",
    "IHS_CBT_303A": "cascious",
    "IHS_CBT_145M": "cascious",
    "IHS_CBT_322A": "Lawrance",
    "IHS_CBT_188M": "cascious",
    "IHS_CBT_174M": "cascious",
    "IHS_CBT_185M": "cascious",
    "IHS_CBT_213A": "Lawrance",
    "IHS_CBT_178M": "cascious",
    "IHS_CBT_212M": "cascious",
    "IHS_CBT_214M": "cascious"
}

# Helper: combined mapping by region
REGION_MAPPINGS = {
    "nrw": NRW_MAPPING,
    "eastern": EASTERN_MAPPING,
    "old_cbt": OLD_CBT_MAPPING
}