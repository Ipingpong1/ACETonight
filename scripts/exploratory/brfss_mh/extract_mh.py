"""Extract mental-health (+ health-care access) columns plus merge keys from one BRFSS zip.
usage: python -I extract_mh.py TAG ZIP_PATH OUTDIR TMPROOT
Unzips the single XPT member into a fresh empty dir under TMPROOT, reads it in 50k-row chunks
(pandas.read_sas format='xport'), keeps only needed columns, writes OUTDIR/extract_mh_TAG.csv, deletes the XPT."""
import sys, re, os, time, zipfile, tempfile, shutil
import pandas as pd
tag, zpath, outdir, tmproot = sys.argv[1:5]
os.makedirs(outdir, exist_ok=True)
t0 = time.time()
tmpd = tempfile.mkdtemp(prefix=f'xpt_{tag}_', dir=tmproot)
try:
    with zipfile.ZipFile(zpath) as z:
        mem = [m for m in z.infolist() if m.filename.strip().lower().endswith('.xpt')]
        assert len(mem) == 1, [m.filename for m in z.infolist()]
        xpt = os.path.join(tmpd, 'data.xpt')
        with z.open(mem[0]) as src, open(xpt, 'wb') as dst:
            shutil.copyfileobj(src, dst, 1 << 24)
    rdr = pd.read_sas(xpt, format='xport', chunksize=50000, encoding='latin1')
    names = [(f['name'].decode('latin1') if isinstance(f['name'], bytes) else str(f['name'])).strip() for f in rdr.fields]
    pat = re.compile(r'^(_STATE|SEQNO|QSTLANG|QSTVER|ADDEPEV\d?|MENTHLTH|_MENT14D|GENHLTH|POORHLTH|'
                     r'MIS(NERVS|HOPLS|RSTLS|DEPRD|EFFRT|WTLES|NOWRK|TMNT|TRHLP|PHLPF)|'
                     r'AD(PLEASR|DOWN|SLEEP|ENERGY|EAT1|FAIL|THINK|MOVE|ANXEV)|'
                     r'LSATISFY|EMTSUPRT|SDLONELY|SDHSTRE1|SDHSTRES|_PHQ\w*|'
                     r'HLTHPLN\d?|HLTHPLAN|_HLTHPLN\d?|_HLTHPL\d|PRIMINS\w*|PERSDOC\d?|MEDCOST\d?)$')
    keep = [n for n in names if pat.match(n)]
    parts = [ch[keep].copy() for ch in rdr]
    df = pd.concat(parts, ignore_index=True)
    df.to_csv(f'{outdir}/extract_mh_{tag}.csv', index=False)
    print(tag, 'rows', len(df), 'cols', ','.join(keep), 'secs', round(time.time() - t0), flush=True)
finally:
    shutil.rmtree(tmpd, ignore_errors=True)
