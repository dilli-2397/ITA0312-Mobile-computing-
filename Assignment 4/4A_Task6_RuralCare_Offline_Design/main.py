devices=[("A Android","ART/Kotlin; Keystore; encrypted Room; WorkManager"),("B iPhone","Swift; Keychain; encrypted local database; BackgroundTasks"),("C J2ME/WML","Restricted fields; minimal queue; only if secure transport/storage supported")]
print("4A TASK 6 - RURALCARE OFFLINE-FIRST DESIGN")
for d,s in devices: print(f"{d}: {s}")
print("Record flow: validate -> UUID/sequence -> AES-GCM encrypt -> persist -> queue")
print("Sync flow: authenticate -> TLS -> send UUID -> server unique constraint -> ACK -> mark synced")
print("Offline target: retain encrypted records for a 10-hour shift.")
print("Boundary: Class C without trustworthy encryption/key storage must not hold full sensitive patient records.")
print("Recovery: revoke device credentials, quarantine invalid keys, preserve unsynced encrypted queue.")