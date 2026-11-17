defects=[("Overbroad permissions","Request only when feature is used; deny-safe fallback"),("Shared readable token","Keystore-backed key; encrypted app-private storage"),("Untrusted update","Verify package signature and trusted distribution"),("Plain HTTP","HTTPS/TLS; disable cleartext and validate certificates")]
print("4A TASK 4 - SECURENOTES SECURITY REPAIR")
for d,r in defects: print(f"DEFECT: {d} | REPAIR: {r}")
print("Attack chain: token exposed -> attacker reuses token -> HTTP traffic observed/modified -> unauthorised write")
print("First confidentiality failure: another app reads the shared token.")
print("Regression: request contact permission only on demand; denial must not block note creation.")