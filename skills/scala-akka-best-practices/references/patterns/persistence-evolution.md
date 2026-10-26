# Events, snapshots, serializers, and historical evolution

229 source-specific cases. Statements retain their historical scope and source stance. Read related PR cases for corrections or alternatives.

## Cases

- A1-0006 — OrderTableV8 new column requires ALTER TABLE ADD COLUMN
- A1-0012 — Expiry events accept optional lastUpdatedTS and use latest only if absent
- A1-0015 — Complex product acknowledgement strictly follows assessment
- A1-0021 — CustomerAdvisoryProfileEntity intentionally does not update lastUpdatedTS
- A1-0022 — Snapshot projection V2 never persists complexProductKnowledgeAttestationDate (identified in hunk)
- A1-0023 — Profile JDBC projection V2 never persists complexProductKnowledgeAttestationDate (identified in hunk)
- A1-0141 — Version subscriber event to capture targetPlanId for source plan
- A1-0218 — Document toComparable strips processing and sorts
- A1-0434 — Use ResetAll command/event with reset date and clear instructions
- A1-0444 — Include requestedBy and reason in charge reset event
- A1-0445 — Nested command field needs no Serializable marker by itself
- A1-0486 — InstrumentState.fromDto is not state deserialization
- A1-0495 — Confirm breaking benchmark DTO is never persisted
- A1-0619 — Update lastModifiedBy and lastModifiedAt
- A1-0633 — Restore deprecated SMART_BETA for persisted event replay
- A1-0643 — MStar docs effectiveDate optional only for backward compatibility
- A1-0648 — Drop benchmark V1 model; keep FE DTO compatibility as None or single 100%-style constituent
- A1-0687 — Make HK email transaction field optional for deployment ordering and replay
- A1-0768 — List remaining context types explicitly instead of case wildcard
- A1-0770 — Keep deprecated plan.initialInvestmentAmount temporarily instead of wrong fundingInstructions.amount
- A1-0823 — Financial SIP patch needs event identity or remark distinguishing system patch from reanswer
- A1-0824 — Events must preserve what happened beyond temporary logs Jira and sheets
- A1-0995 — Include sourcePlanId in recurring-transfer acknowledgement context
- A1-1024 — New acknowledgement fields optional to avoid breaking release
- A1-1026 — Include rebalanceRequestId in context
- A1-1027 — Include transferRequestId for OneTimeTransfer and RecurringTransfer
- A1-1029 — Include investmentRequestId for OneTimeInvestment and ManualInvestment
- A1-1036 — Include sourcePlanId for audit lookup
- A1-1040 — Choose between persisting transfer acks for buy-leg revalidation or SIP-only skip
- A1-1088 — Include goalId in RRT commands
- A1-1089 — Context goalId matches command goalId
- A1-1167 — Use same timestamp for all acknowledgements in request
- A1-1193 — Put PlayJsonSerializable on acknowledgement sealed trait
- A1-1194 — PlanAcknowledgementState keys recurring transfer acknowledgements by sourcePlanId
- A1-1195 — CapturePlanAcknowledgments replaces the complete matching schedule acknowledgement set
- A1-1196 — RemovePlanAcknowledgmentCmd derives removals and preserves unrelated acknowledgement state
- A1-1197 — AddPlanAcknowledgmentsCmd tops up posthoc acknowledgement without replacing existing set
- A1-1198 — Persist List of typed acknowledgement entries rather than String-keyed Map
- A1-1201 — Include sourcePlanId in ack context
- A1-1206 — Add removedAt to two removal contexts
- A1-1207 — Customer-change removals need timestamps
- A1-1208 — Include sourcePlanId for completeness
- A1-1209 — ackRemovalTime in command makes context timestamp redundant
- A1-1213 — Separate trading-action capture context from posthoc recurring add context
- A1-1216 — CapturedEvt and AddedEvt acknowledgement types follow appropriate subtrait
- A1-1218 — Add configForTypeParam for action context removal context and ack formats
- A1-1220 — Use ProcessDiscountRequestCmdV2 rather than version field
- A1-1223 — Use sortedDailyFees in AccumulatedFee for easier event inspection
- A1-1225 — Hide individual voucher constraint case-class formats
- A1-1229 — Apply DTO serialization-scope concern to internal model
- A1-1230 — Subsealed trait formats unnecessary if always serdes as root constraint DTO
- A1-1234 — idString storage does not require jsMapperOf VoucherId
- A1-1793 — Deprecate dangerous facade usage
- A1-1801 — TODO stamp approvalDetails in redemption and propagate to goal
- A1-1804 — Instrument fields may not belong V1 model
- A1-1805 — Fix updateInstrumentDetails lastModifiedBy
- A1-1847 — Use old seed if reservations same account else include account
- A1-1868 — Daily price helper need not PlayJsonSerializable
- A1-1871 — Deprecate old events but retain no-op state handlers
- A1-1882 — Stop publishing deprecated portfolio events
- A1-1908 — Expose price source in API DTO and persistence
- A1-1923 — Missing existing price source defaults MStar
- A1-2033 — Hardcoded tenant-change reason adds no event information
- A1-2034 — Tenant-name request includes requestedBy and reason
- A1-2036 — Decline tenant rename persistence PR after dynamic unblock
- A1-2142 — Goal-level entity event must include planId
- A1-2181 — Use trading.impl.logic TradingSvcException for cluster serialization
- A1-2263 — Deprecate retained obsolete document endpoint
- A1-2268 — Add Json type config
- A1-2294 — Private UserContext subformats ensure root discriminator format
- A1-2303 — Capture whole CustomerCkaCarDetailsDto from ckacar-details endpoint
- A1-2304 — Persisting advisory-api type in goal DB questionable
- A1-2340 — CHINA_FI-to-FundSmart script: goal before, after, and ordered event relationships
- A1-2341 — CHINA_FI-to-FundSmart script: rebalance before, after, and ordered event relationships
- A1-2342 — CHINA_FI-to-FundSmart script: trading before, after, and ordered event relationships
- A1-2343 — CHINA_FI-to-FundSmart script: charge before, after, and ordered event relationships
- A1-2367 — Investment service also owns timestamp-bearing fee config
- A1-2368 — Use same timestamp for all fee configs
- A1-2371 — Add optional CKA snapshot to existing format
- A1-2372 — Goal persistence owns its own CKA snapshot DTO
- A1-2430 — Replace separate events with InstructionFinished plus Submitted
- A2-0025 — package: We may decide to make it required field in DTO after successful backfill \(or adding on-the-fly lookup\), but here it must stay optional as [person] said, due to histor...
- A2-0067 — TradingRestrictionResponse: Do we need to serdes this `ErrorCategory`?
- A2-0104 — package: We cannot use DTO, especially other services' DTO in our domain event. It can feel clumsy at times, but always better and safer to redefine the model.
- A2-0123 — Goal approval events adjacent to PlanRecurringInvestmentScheduleRemovedEvt
- A2-0231 — ClientEntity: You will need to add `TenantSvcException` in tenant-impl that extends `PlayJsonSerializable` otherwise serdes will fail in cluster mode
- A2-0312 — RecurringInvestmentScheduleHistoryDataEventProcessorV3: Maybe we check w data team on this table is used? I’m not sure about adding another row to history entries when backfilli...
- A2-0347 — GoalSupportingDataTableV1: `GoalActionContext` covers `CREATION_APPROVED, MODIFICATION_APPROVED` which is initiated from goal svc
- A2-0434 — Review: I think we should:
- A2-0435 — Review: How to persist documentIds for goal? One approach could be below \(we can review again later\)
- A2-0445 — package: Just double check if we can easily delete obsolete workflows in dynamic-env, cuz these DTO will be persisted there
- A2-0698 — ServiceLogicImpl: if BENCHMARK & DIY, safe to use `currentAllocationTarget` 
- A2-0712 — PortfolioMonthlyChangesHelper: 1. Let’s not persist dummy values \(empty or last value\) on failure
- A2-0714 — PortfolioMonthlyChangesHelper: Let’s move this conditional calc to `generateMonthlyChangesAndUpsert`
- A2-0809 — ServiceClientExceptionSerializer: Move this to akka-client-common? Anyhow akka-client-common depends on silver-commons, so we can just move it there so all service client API st...
- A2-0818 — ServiceClientExceptionSerializerTest: Let’s add a positive test too?
- A2-0820 — ServiceClientExceptionSerializerTest: Shouldn’t it be `implicit val system: ActorSystem`
- A2-0929 — package: We won’t be sending this as separate payload anywhere between the actors, so shouldn’t need extend `PlayJsonSerializable`
- A2-0983 — SgComplianceChecker: Let’s just rename existing to SgComplianceCkaRestrictionViolation and add new SgComplianceTradingRestrictionViolation, both extends ComplianceViolation? Thi...
- A2-1050 — GoalBasedStatementInfoDbDto: I’m not sure if we need all these new fields in `*DbDto`. As I understand, these DTO are persisted and used to check if a statement is reprint or not.
- A2-1056 — package: Should be compatible cuz this is not persisted \(only the `*DbDto` are persisted\).
- A2-1064 — package: [person] after checking the usage of this class again, I’m convinced that
- A2-1073 — PushNotificationProviderData: In theory these should be optional \(otherwise we might break serdes of there are lagged messages in the kafka topic\), but I guess this one is ok ...
- A2-1081 — ReportApplication: Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.
- A2-1098 — Instrument JDBC processor naming: InstrumentV2JdbcEventProcessorV7
- A2-1111 — FxWalletDataHelper: Should we return more data than just the rate? Maybe at least `quotationId` and `quotedAt` ? This can be logging or actually get persisted in event too, in c...
- A2-1176 — Review: That would be next step. Need to check w PM regarding where to store, and the query requirement for it. Likely we just need to stamp in productLineAndIntent… and build h...
- A2-1194 — InvestmentEmailHelper: We don’t need this format right? It’s not serdes anywhere
- A2-1202 — HttpServerStartup: Oh we definitely want to set `rejectionHandler` for all services, especially when we extract this to common code. And in order to use a custom rejection handl...
- A2-1248 — TransactionTypes: Same here. Individual transaction should be serdes via the sealed trait `Transaction` by default. You can ref this inside the object so that we ensure it’s onl...
- A2-1249 — TransactionV3Entity: I think it’s safer to assume we only want to copy over tradeDetails from existing to new value, than to assume we only need to take new statusDetails only f...
- A2-1310 — D56 abort rejected withdrawal dividend: 187.44 switches to cash balance; 12.56 reinvestment remains unchanged
- A2-1404 — BaseAdvisoryService: Can you help to change this to `LagomCompatServiceExceptionSerializer` cuz we already migrated Advisory off Lagom
- A2-1496 — PR-description Projections table: FeeChargeRequestJdbcProjection V6
- A2-1499 — InitiateCancellationFlowCmdHandler: Alright let’s leave those as is for now. This exception will also hit the serdes issue, but ok we clean in separate PR.
- A2-1540 — FundSmartInstrument: We shouldn’t need this one, cuz the case class should be serdes without `_type` and we rely on the implicit region to match type right? Same for `FundSmartI...
- A2-1556 — SgFundSmartManagerV3: [person] can help check which NotFound that we would catch from performance svc? I remember performance svc doesn’t have service exception, so likely it’s ...
- A2-1561 — PersistentEntityRefProvider: Let’s put a scaladoc for this class, noting down all the entity names that were used in the history
- A2-1586 — TransactionTypes: Please help to mark this as deprecated with msg explaining to use V2 \+ rationale, but still keep it for old event \+ snapshot serdes
- A2-1590 — package: As in we should only serdes the individual case class via the trait `FundingInstructionsDto` only. No one should serdes `SpecifiedAccountFundingInstructionsDto` directl...
- A2-1668 — AdvisoryServiceE4s: Don’t use this one. Locale has special formatter, so we want to use the implicit one in `ParameterSerializersE4s`
- A2-1692 — common: Still need to remember to add this bit
- A3-0014 — InstrumentService region serdes: implicit def contract implemented as val for Lagom Service
- A3-0031 — package.scala: `DailyFee` before this PR is not persisted anywhere, so I just make these breaking changes directly to model and DTO
- A3-0067 — InstrumentCommands.scala: Don’t we need format for this?
- A3-0083 — TransactionV2AccountSerializerRegistry.scala: Don’t var if you can
- A3-0084 — TransactionV2AccountSerializerRegistry.scala: you have to update the field using \+\+ but still you don’t need to reassign to existing val?
- A3-0085 — common.conf: And why don’t we need for prod? Cuz you think prod doesn’t these cancelled events?
- A3-0086 — TransactionV2AccountSerializerRegistry.scala: I suppose we don’t migrate state because we only need events to move to V3?
- A3-0087 — common.conf: V2 will be thrown away soon, let’s just keep parity to avoid confusion
- A3-0101 — package.scala: Sorry I forgot… this is V1 entity, only used in SG - we’re good here
- A3-0160 — package.scala: I guess this is ok - we should ideally already move read ops to v2 before we start using these v2-only features
- A3-0173 — enums.scala: These enums, should they be in instrument-api or commons? I don’t think other services would need to persist these? If other services just need to acc
- A3-0181 — ServiceLogicImpl.scala: Just keep v1 as is, and name this v2?
- A3-0182 — ServiceLogicImpl.scala: Assuming this is just a way to validate data, not actual migration, can we move this if check out to `TransactionServiceImpl` instead? ``` def queryTr
- A3-0183 — CustomerTransactionMigrationEventProcessor.scala: Hmm I guess it’s ok, but we will lose the requestedBy and reason in these events
- A3-0192 — InvestmentTransactionV2Transformer.scala: patch will blindly copy and toV2Order will set status according to assumedAt/confirmedAt… so we will have assumed order here even if it’s still pendin
- A3-0193 — No-order rebalance migration: v1 sell/buy sums versus v2 buy-confirmed/sell fallback
- A3-0204 — DTO/domain defaults discouraged except massive legacy-v1-transaction call-site changes
- A3-0206 — CustomerTransactionMigrationEventProcessor.scala: Yea this one is purely just to capture the requestedBy/reason - which helps to explain these manual override if we have to dig in future. If we don’t 
- A3-0256 — Schedule history without key duplicates on event retry
- A3-0265 — UpdatedEvt old/new inserts and offset-commit failures: duplicate windows and PK alternatives
- A3-0284 — JdbcSchema.scala: Create V4?
- A3-0308 — PlanCommunicationV2EventProcessor.scala: Use createdAt if exist?
- A3-0309 — PlanCommunicationV2EventProcessor.scala: Fallback to event timestamp instead of now?
- A3-0313 — Old replayed events missing createdAt should use event timestamp to avoid fresh communication
- A3-0314 — PlanCommunicationV2EventProcessor.scala: Same here, let’s also fallback to event timestamp
- A3-0316 — RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala: Can we just use data from event itself?
- A3-0318 — PlanRecurringInvestmentScheduleHistory.scala: It’s a little weird to see this one Optional, but I guess it’s ok cuz even in events it’s optional. The more important field would be updatedAt
- A3-0344 — Upstream optional fee fields remain optional for V1-to-V2 migration
- A3-0345 — TransactionTypes.scala: Can we remove all these defaults? Let’s make it a habit to not use default unless for legit reason, e.g. if we add new fields in the v1 transaction th
- A3-0365 — Requested-state submission statuses: remove unused external, preserve existing internal if prod data
- A3-0366 — RebateDistributionTopicSubscriberV2.scala: If we are keeping submitted-internally in Requested state, then I suppose we can let this one be in Requested state :pray:
- A3-0388 — New updatedAt missing on old events: ele.timestamp rather than replay-now
- A3-0400 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Use `event.updatedAt` if available
- A3-0428 — package.scala: I think it’s cleaner to create new cmd, mark old one deprecated. Once we switch the usage completely, it’s simple to remove the old cmd whenever we to
- A3-0439 — ThresholdBreachTable.scala: Alright it was there in the Cassandra table too. I guess we can leave it for now.
- A3-0450 — PlanTraderEntityTestForSellFeeCharge.scala: No events mean state will not change right?
- A3-0472 — package.scala: If we are splitting to 2 optional fields for oneTime vs recurring, then it doesn’t make sense to have `RecurringInvestmentRequest` extending `Investme
- A3-0474 — package.scala: Since there is a migration, can we change caller to pass `customerAcknowledgements` properly so we don’t need this default anymore?
- A3-0477 — : Overall looks ok. But you’ll need to fix the import for play json serdes
- A3-0489 — TransactionJdbcDbHandlerV1.scala: no need to rename at all. Just leave the latest as v1\_3… otherwise we will have massive PR just to rename things when we have v1\_4…
- A3-0515 — Post-Lagom API contract exception versus actor serializer; goal internal exception pattern unresolved
- A3-0518 — ChargeServiceE4s.scala: Yup. Will use amend script for this: * we can put all the queries required in the script to do one-time backfill for old fee charges * we still can re
- A3-0519 — SgServiceLogicImpl.scala: As I type this, I can’t recall why I even created `TaxCalculationDetails` at all… so I’m thinking to drop it. Will need to clean cassandra of charge s
- A3-0520 — SgServiceLogicImpl.scala: I’ll test this backfilling logic a bit with existing fee charge request in d56, then will drop this nested field
- A3-0528 — SgTaxCalculator.scala: Placeholder logic for now. Not in-use until we add the backfill logic for old fee charges
- A3-0541 — DividendDistributionEventProcessor.scala: Old events will not have fileVersion but they are actually on V1?
- A3-0567 — BaseChargeServiceE4s.scala: After we release today, help me rebase and add these endpoints to BaseChargeService too. I know it’s not used but let’s just be consistent. In fact, w
- A3-0584 — PlanProfileJdbcRepositoryV2.scala: Ok let’s up-version this table and fix this next, after we release these open PRs :thumbsup:
- A3-0642 — : Will trading release this for HK too? If yes, we would need to handle in V2 entity?
- A3-0646 — TransactionJdbcDbHandlerV1.scala: You don’t need to rename this. Just leave it as is. When migration is completed, we can simply drop it.
- A3-0647 — TransactionTableV1.scala: Same. Don’t need to rename this
- A3-0668 — package.scala: Ok to default here, because otherwise we have to update many places
- A3-0679 — Proposed requestedUnits at AssetTransfer top level later withdrawn after L1 usage review
- A3-0683 — StatusFields V1 bridge differs from always-present AssetTransfer units
- A3-0688 — TransactionTableV1_2.scala: No change required, but just to make sure we are on same page, this is the final table we want to switch over to. It’s not “intermediary”
- A3-0704 — Historical event-handler change accepted as specific exception, supporting Jira unavailable
- A3-0730 — package.scala: Sorry I forgot to mention. I put without default initially and set in all the places required in new model. Then provide default so that we don’t need
- A3-0756 — TransactionApplication.scala: We don’t want these V1 entity for transaction in SG anymore?
- A3-0822 — Recurring failure email: actual reason, event-domain coupling and direct-publish deferral
- A3-0836 — : I guess this one we will add a sync to update existing plans?
- A3-0919 — CraManager.scala: Hmm this will emit `ExpiryDateOverriddenEvt` which is not what happening here… I think we will need another pair of cmd/event
- A3-0920 — Stale onboarding DOB can overwrite newer customer DOB: version/timestamp TODO
- A3-1040 — CustomerCraUpdatedLogic.scala: Ah I should have added the timestamp in the event :see_no_evil:
- A3-1101 — PlanCommunicationV2EventProcessor.scala: If we throw here, the event processor will get stuck. And given we can’t practically modify event, should we just log error and move on?
- A3-1109 — PlanAcknowledgementManagerEvents.scala: Cmd I guess we can merge them all in single `RemoveAcknowledgementsCmd`, but let’s not merge them in events
- A3-1119 — : Will do the following in next PR: * enrich audit payload * persist to audit repository * add internal query endpoints for audit repository
- A3-1186 — TransactionService.scala: Don’t we need V2 for this too?
- A3-1197 — PlanAcknowledgementManagerEvents.scala: Generally, we want to capture events as facts that happened, so this should be `CraCat2AckedEvt`
- A3-1208 — TradingRestrictionLogic.scala: FYi… I’ll implement this when I add the refId as part of audit
- A3-1225 — ServiceLogicImpl.scala: Shall we drop the Cassandra repository too, to avoid further wrong usage?
- A3-1292 — BuyEarmark sameID/amount idempotency validated in command, event appends only
- A3-1296 — CustomerTradingEarmarkManagerEntity.scala: the idea is we validate and reject in command handler, so that event handler can be dumb and just append
- A3-1298 — Same earmarkID+amount returns Done without event
- A3-1319 — BuyEarmark currentVersion then ID+amount branch matrix
- A3-1325 — CustomerTradingEarmarkManagerEvents.scala: Hmmm one action should only create one BuyEarmark I think. Only action that would trigger multiple earmark is modification of a multiple-plan goal. Bu
- A3-1326 — CustomerTradingEarmarkManagerEntity.scala: Ah I think the event should contain only the new earmark, and we append inside `handleEvents` instead of here
- A3-1349 — transactionTypes.scala: When would we need to do this conversion? Ideally we should only to convert from \(old/new\) domain to \(old/new\) DTO, but not between old/new DTO I 
- A3-1354 — transactionTypes.scala: so I’m saying we should convert from new entity to old/new DTO, instead of new DTO to old DTO
- A3-1355 — transactionTypes.scala: on point \(3\), it’s not about losing data. Old data is still there in events, we just want latest snapshot in State \(ideally\). From readside point 
- A3-1357 — CRA scoring/questionnaire versions evolve independently: v1.2/v1.3 versus v2.1
- A3-1359 — package.scala: I need these 2 extra fields on instrument. Ideally they should be required in HK context. Not sure how we want to proceed with this yet, I just add th
- R-3352 — Last chance to extract PlanProfile together with this ProductLine into repository populated via TopicSubscriber directly, instead of going via entity…. Onc
- R-3394 — Old reports would not have fields for currencyBought and currencySold. And I don’t want them to be optional.
- R-3407 — We are still using transitional one today. So I keep the transitional one as is, and update this directly instead.
- R-3466 — Old transitional handler not removed yet
- R-3467 — Rename from old transitional handler, hence there are 2 new columns here, instead of one. ‌
- R-3468 — Extracted `upsert` and `createTableIfNotExists` from existing `GoalJdbcRepositoryImpl`
- R-3469 — Extracted `upsert` and `createTableIfNotExists` from existing `PlanJdbcRepositoryImpl`
- R-3470 — New version of `PlanJdbcDbHandler` using new table definition `PlanTableV1`
- R-3471 — Almost identical to existing `PlanTable` except with `V1` and one new column for `preferences`
- R-3472 — Old transition event processor not removed
- R-3473 — Diff between `PlanDbHandler` \(current prod\) and `PlanDbHandlerV4` \(target state\) should only contain the new column `preferences`
- R-3474 — Renamed from existing old transitional event processor, hence contains more event changes. ‌ Diff between `PlanDbEventProcessor` \(current prod\) and `Plan
- R-3475 — Initial proposal keeps old Plan writes while a separate new Plan processor populates V1
- R-3476 — Turned out `deactivatedAt` and `rebalanceRequest` are also missing. Added them here as well
- R-3477 — Identical to `GoalTable` except for version bump. We want to ensure consistency between Goal and Plan tables, hence update them together in same JdbcEventP
- R-3478 — Initial processor split is withdrawn so Goal and Plan update together for consistency
- R-3479 — Identical to `GoalJdbcEventProcessor` except using V1 DBHandler \+ V1 readsideId
- R-3480 — We also switch to use CassandraReadSide instead of SlickReadSide for the offsetstore for more reliability.
- R-3514 — Deployed to `staging` together with actual Factors changes. Created new goal / modified goal / invested new funding source, and observe no serdes error \(r
- R-3517 — Added `Deleted` to the cases in `deleteRelatedTransaction` I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state
- R-3522 — Migration transactionDate pdd.createdAt differs from subscriber payoutDate at SGD start of day
- R-3526 — As I understand that field `settlementConfirmation` was introduced only in Income P1 and we didn’t patch old dividends that were auto-reinvested by uobkh
- R-3527 — I mark this deprecated, and will remove after we verify everything is fixed in prod. For same reason, I will reuse existing `DividendReinvestedEvt` since t
- R-3531 — Hypothetical V0/V1/V2 optional-to-mandatory dividend field migration paths
- R-3533 — That’s right, but event processor would still retry \(and fail\) until all pods are successfully deployed.
- R-3538 — Final optional event fields defer optional-forever versus mandatory-plus-migration choice

## Full source cases

## A1-0006 — OrderTableV8 new column requires ALTER TABLE ADD COLUMN

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/db/trade/jdbc/OrderTableV8.scala; operation: [INV-5640] feat(broker, trading, investment, transaction): add settlement date; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Don’t we need to add `ALTER TABLE <> ADD COLUMN` somewhere for this new column?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:6 · comment 823466209 · PR 13813 · 2026-07-08

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/db/trade/jdbc/OrderTableV8.scala`

**Explicit source context (pr_title):**

> [INV-5640] feat(broker, trading, investment, transaction): add settlement date

**Evidence:** anon-1.jsonl:6 · comment 823466209 · PR 13813 · 2026-07-08

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/db/trade/jdbc/OrderTableV8.scala`

**Explicit source context (hunk):**

> def isOfflineOrder = column[Option[Boolean]]("is_offline_order")
>  
>    def transactionFee = column[Option[TransactionFee]]("transaction_fee")
> +  def contractNoteSettlementDate = column[Option[LocalDate]]("contract_note_settlement_date")
>  
>    def pk = primaryKey(OrderTableV8.pkName, orderId)

## A1-0012 — Expiry events accept optional lastUpdatedTS and use latest only if absent

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Add optional lastUpdatedTS to Expiry events. If exist then match, else use latest

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:12 · comment 823006415 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:12 · comment 823006415 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (hunk):**

> +  ): Future[Unit] = {
> +    val latestAssessment = customerAdvisoryProfileAssessments
> +      .filter(_.customerId === customerId)
> +      .filterOpt(assessmentUpdatedTS)(_.lastUpdatedTS === _)
> +      .sortBy(_.lastUpdatedTS.desc)
> +      .take(1)
> +
> +    val updateAction = latestAssessment.result.headOption.flatMap {
> +      case Some(data) =>

## A1-0015 — Complex product acknowledgement strictly follows assessment

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yes, complex product ack strictly comes after assessment

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:15 · comment 823084645 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:15 · comment 823084645 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala`

**Explicit source context (hunk):**

> +          data.maybeRiskProfileExpiryDate,
> +        )
> +
> +      case None =>
> +        customerAdvisoryProfiles += data
> +    }
> +
> +    validateUpdatedRows("upsertAssessment", database.run(updateAction.transactionally))
> +  }

## A1-0021 — CustomerAdvisoryProfileEntity intentionally does not update lastUpdatedTS

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> That is intended. No changes here, only added comment to explain the lack-of updating the `lastUpdatedTS`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:21 · comment 823070586 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileEntity.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

## A1-0022 — Snapshot projection V2 never persists complexProductKnowledgeAttestationDate (identified in hunk)

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileSnapshotJdbcProjectionV2.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yes, V2 never persists this field. Already added in the comment to explain it as well

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Field not named in comment; hunk needed to identify.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.
- V2 field identity comes only from the hunk comment.

**Evidence:** anon-1.jsonl:22 · comment 823071036 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileSnapshotJdbcProjectionV2.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:22 · comment 823071036 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileSnapshotJdbcProjectionV2.scala`

**Explicit source context (hunk):**

> private def handleCraSubmittedEvt(entityId: String, event: CraSubmittedEvt): Future[Unit] = {
> -    val data = CustomerAdvisoryProfileDataV2.fromCraSubmittedEvt(UUID.fromString(entityId), event)
> -    dbHandler.upsert(data)
> +    val data = CustomerAdvisoryProfileAssessmentData.fromCraSubmittedEvt(UUID.fromString(entityId), event)
> +    dbHandler.upsert(CustomerAdvisoryProfileAssessmentData.toAdvisoryProfileDataWithoutProductKnowledge(data)) // V2 do not persist complexProductKnowledgeAttestationDate
>    }
>  
>    private def handleVulnerableCustomerProfileResultOverriddenEvt(entityId: String, event: VulnerableCustomerProfileResultOverriddenEvt): Future[Unit] = {

**Evidence:** anon-1.jsonl:22 · comment 823071036 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileSnapshotJdbcProjectionV2.scala`

**Explicit source context (hunk):**

> complexProductKnowledgeAttestationDate

## A1-0023 — Profile JDBC projection V2 never persists complexProductKnowledgeAttestationDate (identified in hunk)

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcProjectionV2.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yes, V2 never persists this field. Already added in the comment to explain it as well

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Field not named in comment; hunk needed to identify.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.
- V2 field identity comes only from the hunk comment.

**Evidence:** anon-1.jsonl:23 · comment 823071938 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcProjectionV2.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:23 · comment 823071938 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcProjectionV2.scala`

**Explicit source context (hunk):**

> private def handleCraSubmittedEvt(entityId: String, event: CraSubmittedEvt): Future[Unit] = {
> -    val data = CustomerAdvisoryProfileDataV2.fromCraSubmittedEvt(UUID.fromString(entityId), event)
> -    dbHandler.upsert(data)
> +    val data = CustomerAdvisoryProfileAssessmentData.fromCraSubmittedEvt(UUID.fromString(entityId), event)
> +    dbHandler.upsert(CustomerAdvisoryProfileAssessmentData.toAdvisoryProfileDataWithoutProductKnowledge(data)) // V2 do not persist complexProductKnowledgeAttestationDate
>    }
>  
>    private def handleVulnerableCustomerProfileResultOverriddenEvt(entityId: String, event: VulnerableCustomerProfileResultOverriddenEvt): Future[Unit] = {

**Evidence:** anon-1.jsonl:23 · comment 823071938 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcProjectionV2.scala`

**Explicit source context (hunk):**

> complexProductKnowledgeAttestationDate

## A1-0141 — Version subscriber event to capture targetPlanId for source plan

**Source stance:** open-question

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/PlanTopicSubscriber.scala; operation: [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Hmmm looks like we need to v2 this one to capture targetPlanId if source plan?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:145 · comment 819052030 · PR 13979 · 2026-06-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/PlanTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [INV-5597] feat(advisory compliance goal instrument investment rebalance trading): add etf and car ack

**Evidence:** anon-1.jsonl:145 · comment 819052030 · PR 13979 · 2026-06-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/PlanTopicSubscriber.scala`

**Explicit source context (hunk):**

> +          Seq(msg.removedSchedule.targetPlanProfile.planId, msg.removedSchedule.sourcePlanProfile.planId),
> +          PlanRecurringTransferScheduleRemovedV2(
>              scheduleId = msg.removedSchedule.transferScheduleId,
> -            sourcePlanId = msg.removedSchedule.sourcePlanProfile.planId
> +            sourcePlanId = msg.removedSchedule.sourcePlanProfile.planId,
> +            targetPlanId = msg.removedSchedule.targetPlanProfile.planId,
>            ),
>            msg.removedAt.toInstant
>          )

## A1-0218 — Document toComparable strips processing and sorts

**Source stance:** requested-change

**Context:**

> component: report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/idempotency/IdempotencyUtils.scala; operation: [INV-5212] adds balance movements; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> The theme is the same for all these `toComparable`: to strip away processing, and sort
> 
> I think let’s put this somewhere. Either in scaladoc of `IdempotencyUtils`, or even in each individual `toComparable` that has logic

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:225 · comment 803130701 · PR 13925 · 2026-06-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statementv3/logic/idempotency/IdempotencyUtils.scala`

**Explicit source context (pr_title):**

> [INV-5212] adds balance movements

## A1-0434 — Use ResetAll command/event with reset date and clear instructions

**Source stance:** suggestion

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala; operation: Resolve INV-5291: Eam profile validation integrations, fix up table name; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid multiple deleted events

**Source-preserving request, proposal, or question:**

> I’m thinking if it’s better to rename this cmd & event to “ResetAll” or sth along that line. The event would only have reset date, and its event handler will simply change the instructions to empty, instead of emitting multiple deleted events

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:441 · comment 793446614 · PR 13798 · 2026-05-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (pr_title):**

> Resolve INV-5291: Eam profile validation integrations, fix up table name

## A1-0444 — Include requestedBy and reason in charge reset event

**Source stance:** requested-change

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/EamProfileManager.scala; operation: Resolve INV-5291: Eam profile validation integrations, fix up table name; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> can we pass requestedBy and reason so we have them in event

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:451 · comment 794061279 · PR 13798 · 2026-05-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/EamProfileManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-5291: Eam profile validation integrations, fix up table name

**Evidence:** anon-1.jsonl:451 · comment 794061279 · PR 13798 · 2026-05-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/EamProfileManager.scala`

**Explicit source context (hunk):**

> +      _ <- Source(plans)
> +        .mapAsync(parallelism = 1) { plan =>
> +          refProvider
> +            .getPlanFeeInstructionEntity(plan.planId)
> +            .ask(ResetPlanFeeInstructionsCmd(_, resetDate = dateTimeProvider.localDateNow, requestedBy = requestedBy, reason = s"Unlinking customer from EAM [$profileId]"))
> +        }
> +        .runWith(Sink.ignore)
> +    } yield Done
> +  }

## A1-0445 — Nested command field needs no Serializable marker by itself

**Source stance:** explanation

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/commons/models/CustomerProfileChargeContext.scala; operation: Resolve INV-5291: Eam profile validation integrations, fix up table name; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** If standalone marker needed it is PlayJsonSerializable

**Source-preserving request, proposal, or question:**

> It should be `PlayJsonSerializable`, but actually we don’t need it because we don’t use it alone. It’s a field within the cmds, so no need to extend this

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:452 · comment 794058193 · PR 13798 · 2026-05-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/commons/models/CustomerProfileChargeContext.scala`

**Explicit source context (pr_title):**

> Resolve INV-5291: Eam profile validation integrations, fix up table name

## A1-0486 — InstrumentState.fromDto is not state deserialization

**Source stance:** explanation

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala; operation: fix(instrument): Move amount regulation validation to impl; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `InstrumentState.fromDto` is not part to state deserialization

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:493 · comment 790209886 · PR 13796 · 2026-04-29

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala`

**Explicit source context (pr_title):**

> fix(instrument): Move amount regulation validation to impl

**Evidence:** anon-1.jsonl:493 · comment 790209886 · PR 13796 · 2026-04-29

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala`

**Explicit source context (hunk):**

> -  )
> +  def fromDto(id: String, dto: SubscriptionDetailsDto): SubscriptionDetails = {
> +    val regulationErrors = dto.regulation.map(AmountRegulationDto.validationErrors).getOrElse(Nil)
> +    if (regulationErrors.nonEmpty) {
> +      throw BadRequest(s"Found data errors for instrument $id subscriptionDetails: $regulationErrors")
> +    }
>  
> -  def toDto(data: SubscriptionDetails): SubscriptionDetailsDto = SubscriptionDetailsDto(
> -    regulation = data.regulation.map(AmountRegulation.toDto),

## A1-0495 — Confirm breaking benchmark DTO is never persisted

**Source stance:** open-question

**Context:**

> component: instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/mstar/package.scala; operation: Resolve INV-5219: Changes for benchmark retrieval logic; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Confirm this is not persisted anywhere yeah, cuz it’s a breaking DTO change

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:502 · comment 740492288 · PR 13204 · 2026-01-19

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/mstar/package.scala`

**Explicit source context (pr_title):**

> Resolve INV-5219: Changes for benchmark retrieval logic

**Evidence:** anon-1.jsonl:502 · comment 740492288 · PR 13204 · 2026-01-19

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/mstar/package.scala`

**Explicit source context (hunk):**

> idMap: Map[InstrumentIdType, String],
>      fundBasicInfo: MstarFundShareClassBasicInfoDto,
>      fundAttributes: MstarFundAttributesDto,
> -    fundBenchmarkDetails: MStarFundBenchmarkDetailsDto,
> +    fundBenchmarkDetails: Option[MStarFundBenchmarkDetailsDto],
>      fundPurchaseDetails: MstarFundPurchaseDetailsDto,
>      fundLevelNetAssets: Option[MstarFundLevelNetAssetsDto]
>    ) extends MStarInfoRetrievalResultDto

## A1-0619 — Update lastModifiedBy and lastModifiedAt

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/handlers/InstrumentCmdHandler.scala; operation: Feat/INV-5489 update stitch details endpoint; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can we also update the `lastModifiedBy` and `lastModifiedAt`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:626 · comment 774417317 · PR 13571 · 2026-03-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/handlers/InstrumentCmdHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-5489 update stitch details endpoint

**Evidence:** anon-1.jsonl:626 · comment 774417317 · PR 13571 · 2026-03-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/handlers/InstrumentCmdHandler.scala`

**Explicit source context (hunk):**

> +    } else if (cmd.updatedBy.isEmpty) {
> +      Effect.reply(cmd.replyTo)(s"updatedBy is empty".error)
> +    } else {
> +      val updatedInstrument = instrument.copy(
> +        endowusDetails = instrument.endowusDetails.copy(benchmarkV2 = cmd.newBenchmarkV2.orElse(instrument.endowusDetails.benchmarkV2)),
> +        fundDetails = instrument.fundDetails.copy(
> +          oldestShareClassStitchDetails = cmd.newOldestShareClassStitchDetails.orElse(instrument.fundDetails.oldestShareClassStitchDetails),
> +          oldestShareClassDifferentVehicleStitchDetails =
> +            cmd.newOldestShareClassDifferentVehicleStitchDetails.orElse(instrument.fundDetails.oldestShareClassDifferentVehicleStitchDetails),

## A1-0633 — Restore deprecated SMART_BETA for persisted event replay

**Source stance:** requested-change

**Context:**

> component: None; operation: Fix/noise logs; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> advisory in SG Dev stuck on old events using SMART\_BETA
> 
> ```
> Restarting stream due to failure [2354]: java.util.NoSuchElementException: No value found for 'SMART_BETA'
> java.util.NoSuchElementException: No value found for 'SMART_BETA'
> 	at scala.Enumeration.$anonfun$withName$1(Enumeration.scala:159)
> 	at scala.collection.immutable.HashMap.getOrElse(HashMap.scala:717)
> 	at scala.Enumeration.withName(Enumeration.scala:159)
> 	at com.endowus.silver.advisory.impl.entities.portfolio.models.package$ProductPortfolio$.$anonfun$advisoryTagToMetaData$2(package.scala:83)
> ```
> 
> → To keep things clean, add back the enum value and mark it as deprecated
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Multiple independent fixes retained in exact source; obsolete enum stalls replay, scale 40 causes noise, nonexistent customer stalls dev projection.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:641 · comment 765990137 · PR 13531 · 2026-03-11

**Explicit source context (pr_title):**

> Fix/noise logs

## A1-0643 — MStar docs effectiveDate optional only for backward compatibility

**Source stance:** explanation

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala; operation: [INV-4814] feat(instrument): MStar fund docs enhancements; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Manual URL/file docs have document date; first postrelease sync fills effectiveDate on MStar docs

**Source-preserving request, proposal, or question:**

> All MStar docs will have effectiveDate. All manual url/file docs will only have document date. This ordering is only for the MStar ones - which no one should put anything manually.
> 
> Existing data has no effectiveDate, and after 1st sync post release, they will all have. So it should be ok. We put effectiveDate optional only because of backward compatibility.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:650 · comment 766404156 · PR 13460 · 2026-03-12

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala`

**Explicit source context (pr_title):**

> [INV-4814] feat(instrument): MStar fund docs enhancements

## A1-0648 — Drop benchmark V1 model; keep FE DTO compatibility as None or single 100%-style constituent

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; operation: Feat/INV-5338 v2 benchmark model; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Blind headOption unsafe for multiple constituents; commenter sees no value setting it

**Source-preserving request, proposal, or question:**

> V1 should be obsolete. We should get rid of from model, and only retain in DTO for backward compatibility with FE.
> 
> So here, either we force setting to None, or if we want to set anything at all, we should only set if primary benchmark has only 1 item \(instead of blind headOption\). But I dont see any value of setting it

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:655 · comment 752070450 · PR 13358 · 2026-02-10

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (pr_title):**

> Feat/INV-5338 v2 benchmark model

## A1-0687 — Make HK email transaction field optional for deployment ordering and replay

**Source stance:** open-question

**Context:**

> component: communication-api/src/main/scala/com/endowus/silver/communication/api/v2/email/EmailProviderData.scala; operation: [INV-5271] feat(communication, investment, rebalance, redemption): Send fund order transaction details into HK emails; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Should this be optional? Otherwise we need to be very careful with deployment ordering and message replay

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:697 · comment 758033321 · PR 13316 · 2026-02-23

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/v2/email/EmailProviderData.scala`

**Explicit source context (pr_title):**

> [INV-5271] feat(communication, investment, rebalance, redemption): Send fund order transaction details into HK emails

## A1-0768 — List remaining context types explicitly instead of case wildcard

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/database/PlanAcknowledgementsSnapshotProjection.scala; operation: [INV-5258] feat(compliance): Create SIP acknowledgement readside table; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** New context addition should prompt conscious handling

**Source-preserving request, proposal, or question:**

> I think let’s list out the remaining context types here, so that we dont need to put logic on `case _`
> 
> Next time someone adds new context, they will be reminded to handle here. Even if it’s just upsert again, it would be conscious decision

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:780 · comment 745908670 · PR 13285 · 2026-01-28

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/database/PlanAcknowledgementsSnapshotProjection.scala`

**Explicit source context (pr_title):**

> [INV-5258] feat(compliance): Create SIP acknowledgement readside table

## A1-0770 — Keep deprecated plan.initialInvestmentAmount temporarily instead of wrong fundingInstructions.amount

**Source stance:** requested-change

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala; operation: Feat/INV-5010 multi system rrt; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Deprecated usage must remain visible for later removal

**Source-preserving request, proposal, or question:**

> Probably stick to old code using deprecated field `plan.initialInvestmentAmount`
> 
> It shouldn’t be used and it will help us find the deprecated usage and remove later. Using `fundingInstructions.amount` is still wrong here but this won’t flag deprecated usage

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:782 · comment 738476671 · PR 13145 · 2026-01-14

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/RRTHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-5010 multi system rrt

## A1-0823 — Financial SIP patch needs event identity or remark distinguishing system patch from reanswer

**Source stance:** suggestion

**Context:**

> component: customer-impl/src/main/scala/com/endowus/silver/customer/impl/customer/handlers/impls/PatchFinancialSIPQuestionsCmdHandler.scala; operation: feat(PG-1759): Add patch endpoint for financial SIP questions; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Latest timestamp in same event hides history

**Source-preserving request, proposal, or question:**

> I think PM already discussed in the incident channel that it’s ok to resend the trading restriction comms, if any.
> 
> Just some thoughts on this patch event,
> 
> * We are using the same event with latest timestamp here. That means a few months from now, if someone looks at the customer entity inspect, it would be pretty tough to know if this was a re-answer by customer, or it was a system patch.
> * I’m wondering if we should still go with a new event type, or at minimum with some optional remark field just to capture the Jira for context of this patch.
> * We might also consider taking the previous `updatedAt` as input and use it here, so that it can be considered as a “pure revert”. This might add a side benefit of not resending comms too \(since communication id would be the same\), if customer doesn’t have any schedule changes compared to their last failure, but we have established that we don’t have to worry about this.
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Could reuse previous updatedAt as pure revert and communication-ID dedup; resend already acceptable.

**Evidence:** anon-1.jsonl:835 · comment 744273143 · PR 13270 · 2026-01-26

Source path: `customer-impl/src/main/scala/com/endowus/silver/customer/impl/customer/handlers/impls/PatchFinancialSIPQuestionsCmdHandler.scala`

**Explicit source context (pr_title):**

> feat(PG-1759): Add patch endpoint for financial SIP questions

## A1-0824 — Events must preserve what happened beyond temporary logs Jira and sheets

**Source stance:** explanation

**Context:**

> component: customer-impl/src/main/scala/com/endowus/silver/customer/impl/customer/handlers/impls/PatchFinancialSIPQuestionsCmdHandler.scala; operation: feat(PG-1759): Add patch endpoint for financial SIP questions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> There’s only one thing in our system that will stand the test of time, events. It’s much better to capture what-happened in events, than logs/jira/gsheet. This is the whole point of event sourcing.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:836 · comment 744275087 · PR 13270 · 2026-01-26

Source path: `customer-impl/src/main/scala/com/endowus/silver/customer/impl/customer/handlers/impls/PatchFinancialSIPQuestionsCmdHandler.scala`

**Explicit source context (pr_title):**

> feat(PG-1759): Add patch endpoint for financial SIP questions

## A1-0995 — Include sourcePlanId in recurring-transfer acknowledgement context

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala; operation: [INV-5045] feat(compliance): implement state changes for sip ack; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Removed schedule cannot later resolve from snapshot or entity; target is current plan

**Source-preserving request, proposal, or question:**

> Ideally this should contain sourcePlanId as well
> 
> I know we key by scheduleId, and itself will be sufficiently unique. Just thinking when we have the audit readside for these ack events, if anyone looks at the scheduleId alone, they will immediately want to know about sourcePlanId \(targetPlanId is already the current plan\). And here’s the “problem”, existing readside in goal/trading svc is latest snapshot only, even in entity we also don’t keep old schedules. Once a schedule is removed, it gets tricky to lookup their info again.
> 
> This is why I keep asking to at least include sourcePlanId in all these contexts.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1011 · comment 728906471 · PR 13004 · 2025-12-18

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (pr_title):**

> [INV-5045] feat(compliance): implement state changes for sip ack

## A1-1024 — New acknowledgement fields optional to avoid breaking release

**Source stance:** suggestion

**Context:**

> component: compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/sg/tradingRestriction/TradingRestrictionRequest.scala; operation: [INV-5014] feat(compliance): implement trading restriction for all the actions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Maybe make these optional? Otherwise we will have breaking change when we release

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1040 · comment 720719672 · PR 12948 · 2025-12-02

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/sg/tradingRestriction/TradingRestrictionRequest.scala`

**Explicit source context (pr_title):**

> [INV-5014] feat(compliance): implement trading restriction for all the actions

**Evidence:** anon-1.jsonl:1040 · comment 720719672 · PR 12948 · 2025-12-02

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/sg/tradingRestriction/TradingRestrictionRequest.scala`

**Explicit source context (hunk):**

> recurringInvestmentAmount: Option[BigDecimal],
>    riskTolerance: BigDecimal,
>    tradingAccountType: TradingAccountType,
> +  acknowledgements: Option[Set[TradingAcknowledgementDto]],
>  ) extends GoalCreationIntention
>      with TradingRestrictionRequest

## A1-1026 — Include rebalanceRequestId in context

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala; operation: [INV-5014] feat(compliance): implement trading restriction for all the actions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Include `rebalanceRequestId`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1042 · comment 720724031 · PR 12948 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (pr_title):**

> [INV-5014] feat(compliance): implement trading restriction for all the actions

**Evidence:** anon-1.jsonl:1042 · comment 720724031 · PR 12948 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (hunk):**

> +case object PlanRecurringInvestmentUpsert extends TradingRestrictionAcknowledgementActionContext
> +case class OneTimeInvestment(investmentRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class ManualInvestment(investmentRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class GoalModification(rebalanceRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class PlanRecurringTransferUpsert(sourcePlanId: UUID, scheduleId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class OneTimeTransfer(sourcePlanId: UUID, transferRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
>  
>  sealed trait PosthocRecurringScheduleAcknowledgementActionContext extends AcknowledgementActionContext
>  case object PosthocRecurringInvestmentSchedule extends PosthocRecurringScheduleAcknowledgementActionContext

## A1-1027 — Include transferRequestId for OneTimeTransfer and RecurringTransfer

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala; operation: [INV-5014] feat(compliance): implement trading restriction for all the actions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Include `transferRequestId` in OneTimeTransfer / RecurringTransfer

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1043 · comment 720724559 · PR 12948 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (pr_title):**

> [INV-5014] feat(compliance): implement trading restriction for all the actions

**Evidence:** anon-1.jsonl:1043 · comment 720724559 · PR 12948 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (hunk):**

> +case class GoalModification(rebalanceRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class PlanRecurringTransferUpsert(sourcePlanId: UUID, scheduleId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class OneTimeTransfer(sourcePlanId: UUID, transferRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
>  
>  sealed trait PosthocRecurringScheduleAcknowledgementActionContext extends AcknowledgementActionContext
>  case object PosthocRecurringInvestmentSchedule extends PosthocRecurringScheduleAcknowledgementActionContext

## A1-1029 — Include investmentRequestId for OneTimeInvestment and ManualInvestment

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala; operation: [INV-5014] feat(compliance): implement trading restriction for all the actions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Include `investmentRequestId` for OneTimeInvestment / ManualInvestment

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1045 · comment 720723818 · PR 12948 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (pr_title):**

> [INV-5014] feat(compliance): implement trading restriction for all the actions

**Evidence:** anon-1.jsonl:1045 · comment 720723818 · PR 12948 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (hunk):**

> -// action contexts corresponding to TradingRestrictionRequest go here, extending TradingRestrictionAcknowledgementActionContext
> +case class GoalCreation(hasRecurringSchedule: Boolean) extends TradingRestrictionAcknowledgementActionContext
> +case class PlanCreation(hasRecurringSchedule: Boolean) extends TradingRestrictionAcknowledgementActionContext
> +case object PlanRecurringInvestmentUpsert extends TradingRestrictionAcknowledgementActionContext
> +case class OneTimeInvestment(investmentRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class ManualInvestment(investmentRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class GoalModification(rebalanceRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class PlanRecurringTransferUpsert(sourcePlanId: UUID, scheduleId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class OneTimeTransfer(sourcePlanId: UUID, transferRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext

## A1-1036 — Include sourcePlanId for audit lookup

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala; operation: [INV-5014] feat(compliance): implement trading restriction for all the actions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s include sourcePlanId as well, just to make it easy to lookup if needed

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1052 · comment 724157964 · PR 12948 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (pr_title):**

> [INV-5014] feat(compliance): implement trading restriction for all the actions

**Evidence:** anon-1.jsonl:1052 · comment 724157964 · PR 12948 · 2025-12-08

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (hunk):**

> +case class OneTimeInvestment(investmentRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class ManualInvestment(investmentRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class GoalModification(rebalanceRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class PlanRecurringTransferUpsert(sourcePlanId: UUID, scheduleId: UUID) extends TradingRestrictionAcknowledgementActionContext
> +case class OneTimeTransfer(sourcePlanId: UUID, transferRequestId: UUID) extends TradingRestrictionAcknowledgementActionContext
>  
>  sealed trait PosthocRecurringScheduleAcknowledgementActionContext extends AcknowledgementActionContext
>  case object PosthocRecurringInvestmentSchedule extends PosthocRecurringScheduleAcknowledgementActionContext

## A1-1040 — Choose between persisting transfer acks for buy-leg revalidation or SIP-only skip

**Source stance:** explanation

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/utils/SgComplianceChecker.scala; operation: [INV-5014] feat(compliance): implement trading restriction for all the actions; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** If rechecking, pass TransferRequest acks via InvestmentTransferProjection; if prior validation authoritative, identify investmentTransferRequestId and skip SIP only

**Source-preserving request, proposal, or question:**

> If we want to perform the compliance check again \(potentially to block investment if SIP status changes in between the sell and buy leg\), we have to persist the acks in trading svc `TransferRequest` and pass it down when we call investment svc in `InvestmentTransferProjection#handleRedemptionCompletedEvt`.
> 
> If we accept that we have already validated before we trigger the redemption, and we can ignore if anything changes in between the 2 legs, we will need to skip the checks in investOnce call. The skip must be specific to SIP only, and we should continue to perform existing checks we do today. We can identify these investment request by checking existence of `investmentTransferRequestId`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1056 · comment 724804787 · PR 12948 · 2025-12-09

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/utils/SgComplianceChecker.scala`

**Explicit source context (pr_title):**

> [INV-5014] feat(compliance): implement trading restriction for all the actions

## A1-1088 — Include goalId in RRT commands

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We can put goalId for these cmd

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1105 · comment 705808712 · PR 12767 · 2025-10-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1089 — Context goalId matches command goalId

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/GoalEdgeLogicImpl.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Set goalId since we also set in cmd

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1106 · comment 705809119 · PR 12767 · 2025-10-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/GoalEdgeLogicImpl.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

**Evidence:** anon-1.jsonl:1106 · comment 705809119 · PR 12767 · 2025-10-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/GoalEdgeLogicImpl.scala`

**Explicit source context (hunk):**

> +          includePlans = true
> +        )
> +        goal = maybeGoal.getOrElse(throw NotFound(s"Can not find given goalId $goalId"))
>        } yield
>          (
>            goal.productLineAndIntent.map(_.productLine),

## A1-1167 — Use same timestamp for all acknowledgements in request

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala; operation: [INV-5022] feat(compliance): create api for financial situation ack; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Better to use same timestamp for all the these acks

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1184 · comment 721224617 · PR 12917 · 2025-12-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-5022] feat(compliance): create api for financial situation ack

**Evidence:** anon-1.jsonl:1184 · comment 721224617 · PR 12917 · 2025-12-03

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/sg/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      .mapAsync(3) {
> +        case PlanRecurringInvestment(planId) =>
> +          val cmd = AddPlanAcknowledgmentsCmd(
> +            _,
> +            ack = ack,
> +            actionContext = PosthocRecurringInvestmentSchedule,
> +            ackTime = ackTime,
> +          )
> +          refProvider.getSgPlanAcknowledgementManagerEntity(planId).ask(cmd)

## A1-1193 — Put PlayJsonSerializable on acknowledgement sealed trait

**Source stance:** open-question

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/models/PlanAcknowledgement.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `PlayJsonSerializable` at sealed trait level?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1210 · comment 718808548 · PR 12925 · 2025-11-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/models/PlanAcknowledgement.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1194 — PlanAcknowledgementState keys recurring transfer acknowledgements by sourcePlanId

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Actually on 2nd thought, we can’t keep track of acks in State by relying on actionContext:
> 
> * Both get/removal use case would be per recurring investment/transfer, but regardless of which actionContext triggers the acks \(either during schedule creation / update / posthoc\)
> * For removal, we might be able to map for all possible combination, but it doesn’t make sense for get
> 
> ‌
> 
> Maybe we should go with explicit acks per recurring schedules
> 
> ```scala
> case class PlanAcknowledgementState(
>   recurringInvestmentScheduleAcks: Set[PlanAcknowledgement],
>   recurringTransferScheduleAcks: Map[SourcePlanId, Set[PlanAcknowledgement]]
> )
> ```
> 
> * Note we key using sourcePlanId for the recurring schedules. If scheduleId changes, we still override at sourcePlanId level.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Replace on capture, derive specific removals in cmd, preserve unrelated acks in evt, top up on separate Add cmd; transfer keyed by sourcePlanId despite scheduleId changes.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:1211 · comment 718849319 · PR 12925 · 2025-11-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1195 — CapturePlanAcknowledgments replaces the complete matching schedule acknowledgement set

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> * For `CapturePlanAcknowledgmentsCmd(actionContext, acks)` flow:
> 
>     * we keep event as is `PlanAcknowledgmentsCapturedEvt(actionContext, acks)`
>     * in event handler
>     
>         * again we have mapper logic from `actionContext` to update the State accordingly, if required
>         * the new acks should replace the existing set completely

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Replace on capture, derive specific removals in cmd, preserve unrelated acks in evt, top up on separate Add cmd; transfer keyed by sourcePlanId despite scheduleId changes.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:1211 · comment 718849319 · PR 12925 · 2025-11-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1196 — RemovePlanAcknowledgmentCmd derives removals and preserves unrelated acknowledgement state

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> * For `RemovePlanAcknowledgmentCmd(ackRemovalContext)` flow:
> 
>     * in cmd handler
>     
>         * the caller should only provide the removal context, and cmd handler would derive which persisted ack\(s\) to remove, e.g. AI status / SIP result upgrade would remove only SIP ack, but schedule removal should remove all acks
>         * hence the removal event\(s\) can’t be generic as we design before, it would have to follow the State fields, e.g. `PlanAcknowledgementRemovedEvt(ackRemovalContext, removedRecurringInvestmentScheduleAcks, removedRecurringTransferScheduleAcks)` 
>         
>     * in event handler
>     
>         * update the State accordingly, should only remove the matching ack while keeping others intact

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Replace on capture, derive specific removals in cmd, preserve unrelated acks in evt, top up on separate Add cmd; transfer keyed by sourcePlanId despite scheduleId changes.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:1211 · comment 718849319 · PR 12925 · 2025-11-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1197 — AddPlanAcknowledgmentsCmd tops up posthoc acknowledgement without replacing existing set

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> * For additional ack flow, we need new cmd, e.g. `AddPlanAcknowledgmentsCmd(actionContext, ack)`
> 
>     * new event `PlanAcknowledgmentsAddedEvt(actionContext, ack)`
>     * in event handler
>     
>         * unlike the capture flow, we want to top up the ack, not replacing the existing set
>         
>     
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Replace on capture, derive specific removals in cmd, preserve unrelated acks in evt, top up on separate Add cmd; transfer keyed by sourcePlanId despite scheduleId changes.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:1211 · comment 718849319 · PR 12925 · 2025-11-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1198 — Persist List of typed acknowledgement entries rather than String-keyed Map

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Sealed actionContext evolves; convert to typed Map in memory

**Source-preserving request, proposal, or question:**

> Seeing this format makes me second-guess using Map for state. Feels dangerous to use String, especially when actionContext is a sealed trait that can evolve in the future.
> 
> Maybe we keep it as List in State, and convert to Map in memory for cmd/evtHandler?
> 
> ```scala
> case class PlanAcknowledgementEntry(actionContext, acks)
> case class PlanAcknowledgementState(ackEntries)
> ```
> 
> ‌
> 
> Once state is loaded, we can convert `ackEntries` from/to `Map[AcknowledgementActionContext, Set[PlanAcknowledgement]]` again

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1212 · comment 718804805 · PR 12925 · 2025-11-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/entities/ces/PlanAcknowledgementState.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1201 — Include sourcePlanId in ack context

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/models/AcknowledgementActionContext.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> include the sourcePlanId here too

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1215 · comment 718806169 · PR 12925 · 2025-11-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/planAcks/models/AcknowledgementActionContext.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1206 — Add removedAt to two removal contexts

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementRemovalContext.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We need to add `removedAt` timestamp for these 2 removal contexts

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1220 · comment 719903907 · PR 12925 · 2025-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementRemovalContext.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

**Evidence:** anon-1.jsonl:1220 · comment 719903907 · PR 12925 · 2025-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementRemovalContext.scala`

**Explicit source context (hunk):**

> +
> +import java.util.UUID
> +
> +sealed trait AcknowledgementRemovalContext
> +
> +case object CustomerInvestorStatusUpgradedFromRetailToAi extends AcknowledgementRemovalContext
> +case object CustomerSipQuestionnairePassed extends AcknowledgementRemovalContext
> +case object PlanRecurringInvestmentScheduleRemoved extends AcknowledgementRemovalContext
> +case class PlanRecurringTransferScheduleRemoved(sourcePlanId: UUID, scheduleId: UUID) extends AcknowledgementRemovalContext

## A1-1207 — Customer-change removals need timestamps

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementRemovalContext.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Delayed pass event can delete fresh ack after pass-fail-ack sequence

**Source-preserving request, proposal, or question:**

> We will also need timestamps for these 2 customer state change contexts.
> 
> For example, in theory, it’s possible that customer manages to pass SIP questionnaire → fail SIP questionnaire → provide acks, and then the projection only now process the 1st pass event leading to removal of freshly capture acks.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1221 · comment 719904862 · PR 12925 · 2025-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementRemovalContext.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1208 — Include sourcePlanId for completeness

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementRemovalContext.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Just for completeness, let’s add sourcePlanId here too

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1222 · comment 719943127 · PR 12925 · 2025-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementRemovalContext.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

**Evidence:** anon-1.jsonl:1222 · comment 719943127 · PR 12925 · 2025-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementRemovalContext.scala`

**Explicit source context (hunk):**

> +
> +sealed trait AcknowledgementRemovalContext
> +
> +case object CustomerInvestorStatusUpgradedFromRetailToAi extends AcknowledgementRemovalContext
> +case object CustomerSipQuestionnairePassed extends AcknowledgementRemovalContext
> +case object PlanRecurringInvestmentScheduleRemoved extends AcknowledgementRemovalContext
> +case class PlanRecurringTransferScheduleRemoved(sourcePlanId: UUID, scheduleId: UUID) extends AcknowledgementRemovalContext
> +
> +object AcknowledgementRemovalContext {

## A1-1209 — ackRemovalTime in command makes context timestamp redundant

**Source stance:** explanation

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Sorry if we have `ackRemovalTime` in cmd already, then we dont need the timestamp in removal context :pray:

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1223 · comment 719946936 · PR 12925 · 2025-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/SgPlanAcknowledgementManagerEntity.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1213 — Separate trading-action capture context from posthoc recurring add context

**Source stance:** suggestion

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> ```scala
> sealed trait AcknowledgementActionContext
> 
> sealed trait TradingRestrictionAcknowledgementActionContext extends AcknowledgementActionContext
> // action contexts corresponding to TradingRestrictionRequest go here, extending TradingRestrictionAcknowledgementActionContext
> 
> sealed trait PosthocRecurringScheduleAcknowledgementActionContext extends AcknowledgementActionContext
> case object PosthocRecurringInvestmentSchedule extends PosthocRecurringScheduleAcknowledgementActionContext
> case class PosthocRecurringTransferSchedule(sourcePlanId: UUID, scheduleId: UUID) extends PosthocRecurringScheduleAcknowledgementActionContext
> 
> ---
> 
> // Capture cmd/event expects only TradingRestrictionAcknowledgementActionContext, e.g.
> CapturePlanAcknowledgmentsCmd(actionContext: TradingRestrictionAcknowledgementActionContext)
> 
> // Add cmd/event expects only PosthocRecurringScheduleAcknowledgementActionContext, e.g.
> AddPlanAcknowledgmentsCmd(actionContext: PosthocRecurringScheduleAcknowledgementActionContext)
> 
> ---
> 
> We add typed Format for TradingRestrictionAcknowledgementActionContext / PosthocRecurringScheduleAcknowledgementActionContext
> -> to be used in cmd/events
> 
> We also add typed Format for AcknowledgementActionContext
> -> to be used in jdbc formatter in audit table (at this point we treat them as generic acks)
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Typed formats for cmd/event subtraits; broad AcknowledgementActionContext format only audit JDBC.

**Evidence:** anon-1.jsonl:1227 · comment 719962734 · PR 12925 · 2025-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

## A1-1216 — CapturedEvt and AddedEvt acknowledgement types follow appropriate subtrait

**Source stance:** requested-change

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/ces/PlanAcknowledgmentEvents.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> The acks in CapturedEvt and AddedEvt should also follow the sub-sealed trait

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1230 · comment 720715738 · PR 12925 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/ces/PlanAcknowledgmentEvents.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

**Evidence:** anon-1.jsonl:1230 · comment 720715738 · PR 12925 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/entities/ces/PlanAcknowledgmentEvents.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  case class PlanAcknowledgmentsCapturedEvt(
> +    actionContext: TradingRestrictionAcknowledgementActionContext,
> +    acks: Set[PlanAcknowledgement],
> +    ackTime: Instant,
> +  ) extends PlanAcknowledgmentEvent
> +
> +  object PlanAcknowledgmentsCapturedEvt {

## A1-1218 — Add configForTypeParam for action context removal context and ack formats

**Source stance:** open-question

**Context:**

> component: compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala; operation: [INV-5047] feat(compliance): create entity for customer acks; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Missing the configForTypeParam? Same for removal context & ack

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1232 · comment 720717312 · PR 12925 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (pr_title):**

> [INV-5047] feat(compliance): create entity for customer acks

**Evidence:** anon-1.jsonl:1232 · comment 720717312 · PR 12925 · 2025-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/sgPlanAcknowledgement/models/AcknowledgementActionContext.scala`

**Explicit source context (hunk):**

> +case class PosthocRecurringTransferSchedule(sourcePlanId: UUID, scheduleId: UUID) extends PosthocRecurringScheduleAcknowledgementActionContext
> +
> +object AcknowledgementActionContext {
> +  implicit private val cfg: Aux[MacroOptions] = JsonUtils.configForTypeParameter()
> +
> +  implicit private val goalCreationFormat: Format[GoalCreation.type] = Json.format
> +  implicit private val posthocRecurringInvestmentScheduleFormat: Format[PosthocRecurringInvestmentSchedule.type] = Json.format
> +  implicit private val posthocRecurringTransferScheduleFormat: Format[PosthocRecurringTransferSchedule] = Json.format
> +

## A1-1220 — Use ProcessDiscountRequestCmdV2 rather than version field

**Source stance:** open-question

**Context:**

> component: voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucherWallet/ces/commands/package.scala; operation: Feat/PG-1205 daily fee discount calculator; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Why are we using `version` field instead of adding proper `ProcessDiscountRequestCmdV2`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1234 · comment 716572639 · PR 12828 · 2025-11-21

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucherWallet/ces/commands/package.scala`

**Explicit source context (pr_title):**

> Feat/PG-1205 daily fee discount calculator

## A1-1223 — Use sortedDailyFees in AccumulatedFee for easier event inspection

**Source stance:** requested-change

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/ChargeHelpers.scala; operation: Feat/PG-1205 daily fee discount calculator; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s rename this as `sortedDailyFees` and use this in `AccumulatedFee` instead of unsorted one. It shouldn’t matter but it would be a bit more convenient when we inspect the events

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1237 · comment 716569682 · PR 12828 · 2025-11-21

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/ChargeHelpers.scala`

**Explicit source context (pr_title):**

> Feat/PG-1205 daily fee discount calculator

## A1-1225 — Hide individual voucher constraint case-class formats

**Source stance:** requested-change

**Context:**

> component: voucher-api/src/main/scala/com/endowus/silver/voucher/api/models/package.scala; operation: Feat/PG-1205 daily fee discount calculator; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Serialize through sealed parent, including RewardedVoucherConstraintDto

**Source-preserving request, proposal, or question:**

> The format of these individual case classes shouldn’t be public. We don’t them to be serdes as standalone case class.
> 
> Same for `RewardedVoucherConstraintDto`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1239 · comment 719916896 · PR 12828 · 2025-12-01

Source path: `voucher-api/src/main/scala/com/endowus/silver/voucher/api/models/package.scala`

**Explicit source context (pr_title):**

> Feat/PG-1205 daily fee discount calculator

## A1-1229 — Apply DTO serialization-scope concern to internal model

**Source stance:** requested-change

**Context:**

> component: voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucher/ces/state/package.scala; operation: Feat/PG-1205 daily fee discount calculator; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Similar concerns as format of the DTO

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1243 · comment 719922067 · PR 12828 · 2025-12-01

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucher/ces/state/package.scala`

**Explicit source context (pr_title):**

> Feat/PG-1205 daily fee discount calculator

**Evidence:** anon-1.jsonl:1243 · comment 719922067 · PR 12828 · 2025-12-01

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/entities/voucher/ces/state/package.scala`

**Explicit source context (hunk):**

> +    def fromDto(constraintDto: VoucherConstraintDto): VoucherConstraint = constraintDto match {
> +      case c: TradingAccountApplicabilityDto => TradingAccountApplicability.fromDto(c)
> +      case c: DurationApplicabilityDto       => DurationApplicability.fromDto(c)
> +      case c: InstrumentApplicabilityDto     => InstrumentApplicability.fromDto(c)
> +    }
> +  }
> +
> +  case class TradingAccountApplicability(
> +    tradingAccountTypes: List[TradingAccountType]

## A1-1230 — Subsealed trait formats unnecessary if always serdes as root constraint DTO

**Source stance:** open-question

**Context:**

> component: voucher-api/src/main/scala/com/endowus/silver/voucher/api/models/package.scala; operation: Feat/PG-1205 daily fee discount calculator; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> These sub sealed trait also shouldn’t have format? They are here just for basic runtime hierarchy, but we always want to serdes as `VoucherConstraintDto`?
> 
> Same for `RewardedVoucherConstraintDto`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1244 · comment 719917170 · PR 12828 · 2025-12-01

Source path: `voucher-api/src/main/scala/com/endowus/silver/voucher/api/models/package.scala`

**Explicit source context (pr_title):**

> Feat/PG-1205 daily fee discount calculator

## A1-1234 — idString storage does not require jsMapperOf VoucherId

**Source stance:** open-question

**Context:**

> component: voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/db/altsFundsDiscountConfigs/AltsFundDiscountConfigTable.scala; operation: Feat/PG-1205 daily fee discount calculator; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> If we’re storing the `idString` , why do we need to add `jsMapperOf[VoucherId]`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1248 · comment 719921655 · PR 12828 · 2025-12-01

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/db/altsFundsDiscountConfigs/AltsFundDiscountConfigTable.scala`

**Explicit source context (pr_title):**

> Feat/PG-1205 daily fee discount calculator

**Evidence:** anon-1.jsonl:1248 · comment 719921655 · PR 12828 · 2025-12-01

Source path: `voucher-impl/src/main/scala/com/endowus/silver/voucher/impl/db/altsFundsDiscountConfigs/AltsFundDiscountConfigTable.scala`

**Explicit source context (hunk):**

> +class AltsFundDiscountConfigTable(tag: Tag) extends Table[AltsFundDiscountConfigurationDb](tag, Some(AltsFundDiscountConfigTable.SchemaName), AltsFundDiscountConfigTable.TableName){
> +
> +  def instrumentId = column[String]("instrument_id")
> +
> +  def voucherId = column[String]("voucher_id")
> +
> +  def updatedAt = column[Instant]("updated_at")
> +
> +  def updatedBy = column[String]("updated_by")

## A1-1793 — Deprecate dangerous facade usage

**Source stance:** requested-change

**Context:**

> component: goal-api/src/main/scala/com/endowus/silver/goal/api/client/BaseGoalService.scala; operation: [NE-337] replace service client api implementations with general facades; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can you do me a favor and mark this one as deprecated? We will need to get rid of these dangerous usages

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1812 · comment 673968514 · PR 12278 · 2025-08-25

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/client/BaseGoalService.scala`

**Explicit source context (pr_title):**

> [NE-337] replace service client api implementations with general facades

## A1-1801 — TODO stamp approvalDetails in redemption and propagate to goal

**Source stance:** requested-change

**Context:**

> component: redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/edge/RedeemOnceEdgeLogic.scala; operation: Feature/BB-2625 approve and summary api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s make a TODO to stamp the approvalDetails in redemption request, and then propagate it to goal svc \(similar to Invest flow\)

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1820 · comment 640927784 · PR 11878 · 2025-06-04

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/edge/RedeemOnceEdgeLogic.scala`

**Explicit source context (pr_title):**

> Feature/BB-2625 approve and summary api

## A1-1804 — Instrument fields may not belong V1 model

**Source stance:** open-question

**Context:**

> component: instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/package.scala; operation: Feat/INV-4366 instrument data modelling; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need these fields in V1 model?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1823 · comment 639862799 · PR 11937 · 2025-06-02

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/package.scala`

**Explicit source context (pr_title):**

> Feat/INV-4366 instrument data modelling

## A1-1805 — Fix updateInstrumentDetails lastModifiedBy

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala; operation: Feat/INV-4366 instrument data modelling; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can you help to fix the bug in `updateInstrumentDetails` in which the instrument’s `lastModifiedBy` is not updated correctly

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1824 · comment 639867681 · PR 11937 · 2025-06-02

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/managers/v2/InstrumentDataUpdateManagerV2.scala`

**Explicit source context (pr_title):**

> Feat/INV-4366 instrument data modelling

## A1-1847 — Use old seed if reservations same account else include account

**Source stance:** suggestion

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/subscribers/RedemptionRequestTopicSubscriber.scala; operation: TT-6669 Collect CPF/SRS fees in cash; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid time cutoff V1/V2

**Source-preserving request, proposal, or question:**

> Also looks like we don’t need to split V1 V2 using timing cutoff.
> 
> We can consider just check if `cashReservations` all have same account, then use previous idSeed logic \(id \+ amount\), otherwise split and add account to idSeed. Everything else stays the same?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1867 · comment 664093453 · PR 12320 · 2025-07-31

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/subscribers/RedemptionRequestTopicSubscriber.scala`

**Explicit source context (pr_title):**

> TT-6669 Collect CPF/SRS fees in cash

## A1-1868 — Daily price helper need not PlayJsonSerializable

**Source stance:** open-question

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/common/package.scala; operation: Feat/INV-4001 daily nav and performance; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Doesnt need to extend `PlayJsonSerializable` right?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1888 · comment 632688765 · PR 11805 · 2025-05-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/common/package.scala`

**Explicit source context (pr_title):**

> Feat/INV-4001 daily nav and performance

**Evidence:** anon-1.jsonl:1888 · comment 632688765 · PR 11805 · 2025-05-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/common/package.scala`

**Explicit source context (hunk):**

> implicit val format: Format[PortfolioMonthlyChanges] = Json.format
>    }
>  
> +  case class DailyReturnIndex(date: LocalDate, value: BigDecimal)
> +
> +  object DailyReturnIndex {
> +    implicit val format: Format[DailyReturnIndex] = Json.format
> +  }

## A1-1871 — Deprecate old events but retain no-op state handlers

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s mark these events deprecated, but we will need to provide evt handler for them. Just that we return the state as in in those handlers

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1891 · comment 632602018 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/ModelPortfolioEntity.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

## A1-1882 — Stop publishing deprecated portfolio events

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/producers/PortfolioTopicProducer.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s stop publishing for these deprecated event as well?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1902 · comment 632759905 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/producers/PortfolioTopicProducer.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

**Evidence:** anon-1.jsonl:1902 · comment 632759905 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/producers/PortfolioTopicProducer.scala`

**Explicit source context (hunk):**

> -          updatedAllocationTable = AllocationTargetTable.toDto(evt.updatedAllocationTable),
> -        )
> -        Future.successful(msg)
> -
> -      case BasicEventEnvelope(entityId, evt: PortfolioProjectedReturnUpdatedEvt, offset) =>
> -        val portfolioId = UUID.fromString(entityId)
> -        val msg = PortfolioProjectedReturnUpdatedMsg(
> -          portfolioId = portfolioId,
> -          effectiveDate = evt.currentEffectiveDate,

## A1-1908 — Expose price source in API DTO and persistence

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/common/package.scala; operation: [INV-4569] feat(marketdata): support source of price update; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s move this to api and add to DTO as well so that we can tell when querying prices.
> 
> Should be ok to use this in both DTO and persistence in this case I think

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1928 · comment 664708148 · PR 12355 · 2025-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/common/package.scala`

**Explicit source context (pr_title):**

> [INV-4569] feat(marketdata): support source of price update

## A1-1923 — Missing existing price source defaults MStar

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; operation: [INV-4569] feat(marketdata): support source of price update; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s also default source to MStar if `existingSource` is None?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1943 · comment 665712153 · PR 12355 · 2025-08-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4569] feat(marketdata): support source of price update

**Evidence:** anon-1.jsonl:1943 · comment 665712153 · PR 12355 · 2025-08-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      existingPriceInfo = existingDailyPrices.map(p => p.dailyPrice.priceDate -> (p.dailyPrice.value, p.dailyPrice.priceSource.getOrElse(Mstar))).toMap
> +      businessDate = request.maybeBusinessDate.getOrElse(dateTimeProvider.localDateNow)
> +      prices = request.prices.map { case (date, price) =>
> +        val priceSource = existingPriceInfo.get(date) match {
> +          case Some((existingValue, existingSource)) if existingValue == price => existingSource
> +          case _ => Manual // Different value or new priceDate, treat as Manual
> +        }
> +        DailyPrice(
> +          businessDate = businessDate,

## A1-2033 — Hardcoded tenant-change reason adds no event information

**Source stance:** explanation

**Context:**

> component: tenant-impl/src/main/scala/com/endowus/silver/tenant/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-4271] feat(tenant): create api to update tenant name; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Accepted only temporary dynamic-data repair context

**Source-preserving request, proposal, or question:**

> Oh I realize you were following this pattern :sweat_smile: Ok I guess it’s ok for the current purpose \(to fix invalid tenant data in dynamic\), but essentially this hardcode string adds zero useful info into the event

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2053 · comment 623184147 · PR 11665 · 2025-04-23

Source path: `tenant-impl/src/main/scala/com/endowus/silver/tenant/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4271] feat(tenant): create api to update tenant name

## A1-2034 — Tenant-name request includes requestedBy and reason

**Source stance:** requested-change

**Context:**

> component: tenant-api/src/main/scala/com/endowus/silver/tenant/api/request/UpdateTenantNameRequest.scala; operation: [INV-4271] feat(tenant): create api to update tenant name; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add `requestedBy` and `reason` in the request as well, so that we can pass them to the cmd

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2054 · comment 623183477 · PR 11665 · 2025-04-23

Source path: `tenant-api/src/main/scala/com/endowus/silver/tenant/api/request/UpdateTenantNameRequest.scala`

**Explicit source context (pr_title):**

> [INV-4271] feat(tenant): create api to update tenant name

**Evidence:** anon-1.jsonl:2054 · comment 623183477 · PR 11665 · 2025-04-23

Source path: `tenant-api/src/main/scala/com/endowus/silver/tenant/api/request/UpdateTenantNameRequest.scala`

**Explicit source context (hunk):**

> +import com.endowus.silver.commons.endpoints4s.SchemaGenerator
> +import play.api.libs.json.{Format, Json}
> +
> +case class UpdateTenantNameRequest(
> +  name: String,
> +  requestedBy: String,
> +  reason: String
> +)
> +

## A1-2036 — Decline tenant rename persistence PR after dynamic unblock

**Source stance:** requested-change

**Context:**

> component: None; operation: [INV-4271] feat(tenant): create api to update tenant name; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Prod event permanence implications; revisit resetting/recreating dynamic tenant

**Source-preserving request, proposal, or question:**

> for now, d56 is unblocked since we fixed the tenant data using this branch, so our FE and QA guys are unblocked. However, there are more implications for this event to be permanently persisted for prod
> 
> Let’s decline this PR for now. We will revisit on how we can fix d56 by reseting tenant data & recreating the tenants with correct name again. CC

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2056 · comment 623257556 · PR 11665 · 2025-04-23

**Explicit source context (pr_title):**

> [INV-4271] feat(tenant): create api to update tenant name

## A1-2142 — Goal-level entity event must include planId

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/ces/events/package.scala; operation: [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Entity is at goal level, so we would need `planId` in these event as well.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:2159 · comment 572113955 · PR 10480 · 2024-12-02

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/ces/events/package.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, workflowengine, advisory, goal, investment): Create subsequent investment for existing goal

## A1-2181 — Use trading.impl.logic TradingSvcException for cluster serialization

**Source stance:** requested-change

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/PlanTraderEntity.scala; operation: [INV-4109] fix(investment): trigger cancel investment request endpoint.; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Need to use `TradingSvcException` under `com.endowus.silver.trading.impl.logic` so that it can be serdes correctly within the cluster

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2198 · comment 610733251 · PR 11420 · 2025-03-19

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/PlanTraderEntity.scala`

**Explicit source context (pr_title):**

> [INV-4109] fix(investment): trigger cancel investment request endpoint.

## A1-2263 — Deprecate retained obsolete document endpoint

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala; operation: [INV-3507] feat(instrument): create api to sync mstar instrument documents; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s mark this as deprecated if we are not removing it yet in this PR

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2280 · comment 599638277 · PR 10854 · 2025-02-25

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala`

**Explicit source context (pr_title):**

> [INV-3507] feat(instrument): create api to sync mstar instrument documents

**Evidence:** anon-1.jsonl:2280 · comment 599638277 · PR 10854 · 2025-02-25

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/commons/v2/models.scala`

**Explicit source context (hunk):**

> +}
> +
> +// todo:- remove from event in d56 before deleting this from the code
> +@Deprecated
> +case class MstarFileFundDocument(
> +  mstarDocumentId: String,
> +  documentId: UUID,
> +  documentType: FundDocumentType,
> +  documentName: String,

## A1-2268 — Add Json type config

**Source stance:** requested-change

**Context:**

> component: communication-api/src/main/scala/com/endowus/silver/communication/api/common/OtpTemplateRequest.scala; operation: otp changes; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s just add the Json config for type?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2285 · comment 599580587 · PR 11043 · 2025-02-25

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/common/OtpTemplateRequest.scala`

**Explicit source context (pr_title):**

> otp changes

**Evidence:** anon-1.jsonl:2285 · comment 599580587 · PR 11043 · 2025-02-25

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/common/OtpTemplateRequest.scala`

**Explicit source context (hunk):**

> +object InvestmentAmountRequest {
> +  implicit private val cfg: Aux[MacroOptions] = JsonUtils.configForTypeParameter()
> +  implicit private lazy val investmentAmountRequestFormat: Format[PlanAccountInvestmentRequest] = Json.format
> +  implicit private lazy val specifiedAccountInvestmentRequestFormat: Format[SpecifiedAccountInvestmentRequest] = Json.format
> +  implicit lazy val format: Format[InvestmentAmountRequest] = Json.format
> +
> +  trait Schema extends BankAccountDetails.Schema with TradingAccountType.Schema { this: SchemaGenerator =>
> +    implicit lazy val investmentAmountRequestSchema: JsonSchema[InvestmentAmountRequest] = genericJsonSchema[InvestmentAmountRequest]
> +  }

## A1-2294 — Private UserContext subformats ensure root discriminator format

**Source stance:** requested-change

**Context:**

> component: communication-api/src/main/scala/com/endowus/silver/communication/api/localization/TranslatableData.scala; operation: [INV-3765] feat(adviosry): create apis for b2b approval notifcations; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We need these to be private, so that `Format[UserContext]` is used with discriminator?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2311 · comment 598611812 · PR 11000 · 2025-02-21

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/localization/TranslatableData.scala`

**Explicit source context (pr_title):**

> [INV-3765] feat(adviosry): create apis for b2b approval notifcations

**Evidence:** anon-1.jsonl:2311 · comment 598611812 · PR 11000 · 2025-02-21

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/localization/TranslatableData.scala`

**Explicit source context (hunk):**

> +
> +final case class B2bEmployeeContext(tenantId: UUID) extends UserContext
> +
> +object B2bEmployeeContext {
> +  implicit val format: Format[B2bEmployeeContext] = Json.format
> +}
> +
> +final case class B2bCustomerContext(tenantId: UUID) extends UserContext
> +

## A1-2303 — Capture whole CustomerCkaCarDetailsDto from ckacar-details endpoint

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateApprovalActionBehaviour.scala; operation: Resolve INV-3819: Detach CKA checks for B2B goals; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s capture the whole `CustomerCkaCarDetailsDto`returned from
> 
> ```
>     val getCustomerCkaCarDetails: EndpointDef[CustomerCkaCarDetailsType] = {
>       val customerId = segment[UUID]("customerId")
>       endpoint(
>         request(Get, path / "api" / "v1" / "customer" / customerId / "ckacar-details", emptyRequest),
>         withStatus(ok(jsonResponse[CustomerCkaCarDetailsType#Out]))
>       )
>     } 
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2320 · comment 599620621 · PR 11140 · 2025-02-25

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/sg/SgGoalCreateApprovalActionBehaviour.scala`

**Explicit source context (pr_title):**

> Resolve INV-3819: Detach CKA checks for B2B goals

## A1-2304 — Persisting advisory-api type in goal DB questionable

**Source stance:** open-question

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/GoalSupportingDataVo.scala; operation: Resolve INV-3819: Detach CKA checks for B2B goals; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I’m not sure about storing this advisory-api in goal svc DB

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2321 · comment 599621075 · PR 11140 · 2025-02-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/GoalSupportingDataVo.scala`

**Explicit source context (pr_title):**

> Resolve INV-3819: Detach CKA checks for B2B goals

**Evidence:** anon-1.jsonl:2321 · comment 599621075 · PR 11140 · 2025-02-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/GoalSupportingDataVo.scala`

**Explicit source context (hunk):**

> +case class ApprovalPayloadAwareActionApprovedDetailsData(
> +  documentIds: List[UUID],
> +  taskApprovalDetails: TaskApprovalDetails,
> +  approvalPayload: GoalCreationApprovalPayload
> +) extends GoalSupportingData
> +
>  object GoalSupportingData {
>    implicit private val cfg: Aux[MacroOptions] = JsonUtils.configForTypeParameter()

## A1-2340 — CHINA_FI-to-FundSmart script: goal before, after, and ordered event relationships

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Reported d56 verification. Shared source caveats: * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact
> 
> Selected fields with original nesting. The stage keys below are editorial labels for the source headings “Existing entity data” and “Entity state & events after running the script”. The event array retains the source event order. UUID role labels distinguish old/new portfolio identity without exporting literal identifiers.
> 
> ```json
> {
>   "before_script": {
>     "maybeGoal": {
>       "name": "Satellite - Technology",
>       "marketRiskToleranceLevel": "CONTROLLER_GROWTH",
>       "marketRiskToleranceValue": 0.3,
>       "targetStockRatio": 0,
>       "targetStockRatioSelfSelected": false,
>       "productLineAndIntent": {
>         "_type": "SatelliteProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "satelliteType": "CHINA_FI",
>         "ackRiskAdvisoryOverride": true,
>         "ackCustomerInformationAccurate": true
>       }
>     },
>     "plans": [
>       {
>         "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>         "planCcy": "SGD",
>         "initialInvestmentAmount": 0,
>         "recurringInvestmentSchedule": {
>           "interval": "MONTHLY",
>           "startingFrom": "2023-07-02",
>           "investmentAmount": 100,
>           "fundingInstructions": {
>             "_type": "PlanAccountFundingInstructions",
>             "amount": 100
>           }
>         },
>         "targetAssetAllocation": {
>           "modelPortfolioId": "[old portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "targetStockRatio": 0,
>           "targetBondRatio": 1,
>           "fundLevelFee": 0.000115,
>           "trailerFeeRebateRatio": 3.28e-05,
>           "fundLevelFeeAfterRebate": 8.22e-05,
>           "targetInstrumentWeights": {
>             "IE00BHXGRN56": {
>               "id": "IE00BHXGRN56",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.3
>             },
>             "LU1847653497": {
>               "id": "LU1847653497",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.7
>             }
>           }
>         }
>       }
>     ]
>   },
>   "after_script": {
>     "maybeGoal": {
>       "name": "Satellite - Technology",
>       "marketRiskToleranceLevel": "CONTROLLER_GROWTH",
>       "marketRiskToleranceValue": 0.3,
>       "targetStockRatio": 0,
>       "targetStockRatioSelfSelected": true,
>       "productLineAndIntent": {
>         "_type": "FundSmartProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgments": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       }
>     },
>     "plans": [
>       {
>         "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>         "planCcy": "SGD",
>         "initialInvestmentAmount": 0,
>         "recurringInvestmentSchedule": {
>           "interval": "MONTHLY",
>           "startingFrom": "2023-07-02",
>           "investmentAmount": 100,
>           "fundingInstructions": {
>             "_type": "PlanAccountFundingInstructions",
>             "amount": 100
>           }
>         },
>         "targetAssetAllocation": {
>           "modelPortfolioId": "[new portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "targetStockRatio": 0,
>           "targetBondRatio": 1,
>           "fundLevelFee": 0.000115,
>           "trailerFeeRebateRatio": 3.28e-05,
>           "fundLevelFeeAfterRebate": 8.22e-05,
>           "targetInstrumentWeights": {
>             "IE00BHXGRN56": {
>               "id": "IE00BHXGRN56",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.3
>             },
>             "LU1847653497": {
>               "id": "LU1847653497",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.7
>             }
>           }
>         }
>       }
>     ]
>   },
>   "events_after_script_in_source_order": [
>     {
>       "eventName": "package$PlanTargetAssetAllocationUpdatedEvt",
>       "event": {
>         "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>         "currentTaa": {
>           "modelPortfolioId": "[old portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "targetStockRatio": 0,
>           "targetBondRatio": 1,
>           "fundLevelFee": 0.000115,
>           "trailerFeeRebateRatio": 3.28e-05,
>           "fundLevelFeeAfterRebate": 8.22e-05,
>           "targetInstrumentWeights": {
>             "IE00BHXGRN56": {
>               "id": "IE00BHXGRN56",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.3
>             },
>             "LU1847653497": {
>               "id": "LU1847653497",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.7
>             }
>           }
>         },
>         "newTaa": {
>           "modelPortfolioId": "[new portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "targetStockRatio": 0,
>           "targetBondRatio": 1,
>           "fundLevelFee": 0.000115,
>           "trailerFeeRebateRatio": 3.28e-05,
>           "fundLevelFeeAfterRebate": 8.22e-05,
>           "targetInstrumentWeights": {
>             "IE00BHXGRN56": {
>               "id": "IE00BHXGRN56",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.3
>             },
>             "LU1847653497": {
>               "id": "LU1847653497",
>               "instrumentCcy": "SGD",
>               "targetWeight": 0.7
>             }
>           }
>         },
>         "requestedBy": "[identity omitted]",
>         "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>       }
>     },
>     {
>       "eventName": "package$GoalProductLineAndIntentModifiedEvt",
>       "event": {
>         "previousProductLineAndIntent": {
>           "_type": "SatelliteProduct",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "satelliteType": "CHINA_FI",
>           "ackRiskAdvisoryOverride": true,
>           "ackCustomerInformationAccurate": true
>         },
>         "newProductLineAndIntent": {
>           "_type": "FundSmartProduct",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "riskToleranceValue": 0.3,
>           "acknowledgments": {
>             "fundSmartNoAdvice": true,
>             "fundSmartCustomerInformationStillAccurate": true
>           }
>         }
>       }
>     },
>     {
>       "eventName": "package$GoalProductLineAndIntentModifiedEvt",
>       "event": {
>         "previousProductLineAndIntent": {
>           "_type": "FundSmartProduct",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "riskToleranceValue": 0.3,
>           "acknowledgments": {
>             "fundSmartNoAdvice": true,
>             "fundSmartCustomerInformationStillAccurate": true
>           }
>         },
>         "newProductLineAndIntent": {
>           "_type": "FundSmartProduct",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "riskToleranceValue": 0.3,
>           "acknowledgments": {
>             "fundSmartNoAdvice": true,
>             "fundSmartCustomerInformationStillAccurate": true
>           }
>         },
>         "requestedBy": "[identity omitted]",
>         "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>       }
>     },
>     {
>       "eventName": "package$GoalTargetStockRatioUpdatedEvt",
>       "event": {
>         "newTargetStockRatio": 0,
>         "newTargetStockRatioSelfSelected": true,
>         "newTargetStockRatioDescription": "Fund Smart portfolio for [identity omitted] for Satellite - Technology (GENERAL_WEALTH_ACCUMULATION)",
>         "newMarketRiskToleranceLevel": "CONTROLLER_GROWTH",
>         "newMarketRiskToleranceValue": 0.3,
>         "requestedBy": "[identity omitted]",
>         "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>       }
>     }
>   ]
> }
> ```

**Conditions and limits:**

- Historical reported verification in d56; the displayed JSON is an editorial selected-field view, not a verbatim complete dump and not a recommended current migration procedure.
- The source effective date differs from prod because this d56 fixture was created later. Its goal name remained Satellite - Technology after a Technology-to-ChineFI modification; the source explicitly keeps that misleading name intact.
- before_script and after_script correspond to source headings Existing entity data and Entity state & events after running the script. The events_after_script_in_source_order array preserves the source event order and each event payload nesting, including previous/current/new object roles.
- Old/new portfolio identity labels are editorial replacements for incidental UUID values. The same old and new identities recur across goal, rebalance, trading and charge; no literal entity/customer/account UUID is exported.
- The effectiveDate2023-02-16, IE00BHXGRN56 weight0.3, LU1847653497 weight0.7, risk values, acknowledgement fields and recurring100 values remain source-specific. Unchanged repetitive state and descriptive fund metadata are omitted from the selected view.
- Exact coherent source member/event spans support the selected view; excerpt_scope is an editorial source-section locator and is not quoted source wording.

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "marketRiskToleranceValue": 0.3

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "targetStockRatioSelfSelected": false

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "productLineAndIntent": {
>                 "_type": "SatelliteProduct",
>                 "goalType": "GENERAL_WEALTH_ACCUMULATION",
>                 "investmentHorizonInYears": 30,
>                 "riskToleranceLevel": "CONTROLLER_GROWTH",
>                 "satelliteType": "CHINA_FI",
>                 "ackRiskAdvisoryOverride": true,
>                 "ackCustomerInformationAccurate": true
>             }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "recurringInvestmentSchedule": {
>                     "interval": "MONTHLY",
>                     "startingFrom": "2023-07-02",
>                     "investmentAmount": 100,
>                     "fundingInstructions": {
>                         "_type": "PlanAccountFundingInstructions",
>                         "amount": 100
>                     }
>                 }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "targetAssetAllocation": {
>                     "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                     "modelPortfolioName": "China Fixed Income",
>                     "effectiveDate": "2023-02-16",
>                     "targetStockRatio": 0,
>                     "targetBondRatio": 1,
>                     "fundLevelFee": 0.000115,
>                     "trailerFeeRebateRatio": 0.0000328,
>                     "fundLevelFeeAfterRebate": 0.0000822,
>                     "targetInstrumentWeights": {
>                         "IE00BHXGRN56": {
>                             "id": "IE00BHXGRN56",
>                             "name": "Neuberger Berman China Bond Fund",
>                             "instrumentType": "FIXED_INCOME_FUND",
>                             "instrumentCcy": "SGD",
>                             "description": "The Fund aims to achieve a target average return of 3% over the benchmark before fees over a market cycle by primarily investing in fixed income instruments issued in the Chinese local currency markets.",
>                             "trailerFeeRebateRatio": 0.000065,
>                             "expenseRatio": 0.00015,
>                             "targetStockRatio": 0,
>                             "targetBondRatio": 1,
>                             "targetWeight": 0.3
>                         },
>                         "LU1847653497": {
>                             "id": "LU1847653497",
>                             "name": "BlackRock BGF China Bond Fund",
>                             "instrumentType": "FIXED_INCOME_FUND",
>                             "instrumentCcy": "SGD",
>                             "description": "The Fund seeks to maximise total return by investing at least 70% of its total assets in fixed income transferable securities denominated in Renminbi or other non-Chinese domestic currencies issued by entities exercising the predominant part of their economic activity in the PRC.",
>                             "trailerFeeRebateRatio": 0.000019,
>                             "expenseRatio": 0.0001,
>                             "targetStockRatio": 0,
>                             "targetBondRatio": 1,
>                             "targetWeight": 0.7
>                         }
>                     }
>                 }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "marketRiskToleranceValue": 0.3

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "targetStockRatioSelfSelected": true

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "productLineAndIntent": {
>                 "_type": "FundSmartProduct",
>                 "goalType": "GENERAL_WEALTH_ACCUMULATION",
>                 "investmentHorizonInYears": 30,
>                 "riskToleranceLevel": "CONTROLLER_GROWTH",
>                 "riskToleranceValue": 0.3,
>                 "acknowledgments": {
>                     "fundSmartNoAdvice": true,
>                     "fundSmartCustomerInformationStillAccurate": true
>                 }
>             }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "recurringInvestmentSchedule": {
>                     "interval": "MONTHLY",
>                     "startingFrom": "2023-07-02",
>                     "investmentAmount": 100,
>                     "fundingInstructions": {
>                         "_type": "PlanAccountFundingInstructions",
>                         "amount": 100
>                     }
>                 }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "targetAssetAllocation": {
>                     "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                     "modelPortfolioName": "Fund Smart portfolio for

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> for goal Satellite - Technology (seed

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> )",
>                     "effectiveDate": "2023-02-16",
>                     "targetStockRatio": 0,
>                     "targetBondRatio": 1,
>                     "fundLevelFee": 0.000115,
>                     "trailerFeeRebateRatio": 0.0000328,
>                     "fundLevelFeeAfterRebate": 0.0000822,
>                     "targetInstrumentWeights": {
>                         "IE00BHXGRN56": {
>                             "id": "IE00BHXGRN56",
>                             "name": "Neuberger Berman China Bond Fund",
>                             "instrumentType": "FIXED_INCOME_FUND",
>                             "instrumentCcy": "SGD",
>                             "description": "The Fund aims to achieve a target average return of 3% over the benchmark before fees over a market cycle by primarily investing in fixed income instruments issued in the Chinese local currency markets.",
>                             "trailerFeeRebateRatio": 0.000065,
>                             "expenseRatio": 0.00015,
>                             "targetStockRatio": 0,
>                             "targetBondRatio": 1,
>                             "targetWeight": 0.3
>                         },
>                         "LU1847653497": {
>                             "id": "LU1847653497",
>                             "name": "BlackRock BGF China Bond Fund",
>                             "instrumentType": "FIXED_INCOME_FUND",
>                             "instrumentCcy": "SGD",
>                             "description": "The Fund seeks to maximise total return by investing at least 70% of its total assets in fixed income transferable securities denominated in Renminbi or other non-Chinese domestic currencies issued by entities exercising the predominant part of their economic activity in the PRC.",
>                             "trailerFeeRebateRatio": 0.000019,
>                             "expenseRatio": 0.0001,
>                             "targetStockRatio": 0,
>                             "targetBondRatio": 1,
>                             "targetWeight": 0.7
>                         }
>                     }
>                 }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$PlanTargetAssetAllocationUpdatedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "currentTaa": {
>         "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "modelPortfolioName": "China Fixed Income",
>         "effectiveDate": "2023-02-16",
>         "targetStockRatio": 0,
>         "targetBondRatio": 1,
>         "fundLevelFee": 0.000115,
>         "trailerFeeRebateRatio": 0.0000328,
>         "fundLevelFeeAfterRebate": 0.0000822,
>         "targetInstrumentWeights": {
>           "IE00BHXGRN56": {
>             "id": "IE00BHXGRN56",
>             "name": "Neuberger Berman China Bond Fund",
>             "instrumentType": "FIXED_INCOME_FUND",
>             "instrumentCcy": "SGD",
>             "description": "The Fund aims to achieve a target average return of 3% over the benchmark before fees over a market cycle by primarily investing in fixed income instruments issued in the Chinese local currency markets.",
>             "trailerFeeRebateRatio": 0.000065,
>             "expenseRatio": 0.00015,
>             "targetStockRatio": 0,
>             "targetBondRatio": 1,
>             "targetWeight": 0.3
>           },
>           "LU1847653497": {
>             "id": "LU1847653497",
>             "name": "BlackRock BGF China Bond Fund",
>             "instrumentType": "FIXED_INCOME_FUND",
>             "instrumentCcy": "SGD",
>             "description": "The Fund seeks to maximise total return by investing at least 70% of its total assets in fixed income transferable securities denominated in Renminbi or other non-Chinese domestic currencies issued by entities exercising the predominant part of their economic activity in the PRC.",
>             "trailerFeeRebateRatio": 0.000019,
>             "expenseRatio": 0.0001,
>             "targetStockRatio": 0,
>             "targetBondRatio": 1,
>             "targetWeight": 0.7
>           }
>         }
>       },
>       "newTaa": {
>         "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "modelPortfolioName": "Fund Smart portfolio for

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> for goal Satellite - Technology (seed

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> )",
>         "effectiveDate": "2023-02-16",
>         "targetStockRatio": 0,
>         "targetBondRatio": 1,
>         "fundLevelFee": 0.000115,
>         "trailerFeeRebateRatio": 0.0000328,
>         "fundLevelFeeAfterRebate": 0.0000822,
>         "targetInstrumentWeights": {
>           "IE00BHXGRN56": {
>             "id": "IE00BHXGRN56",
>             "name": "Neuberger Berman China Bond Fund",
>             "instrumentType": "FIXED_INCOME_FUND",
>             "instrumentCcy": "SGD",
>             "description": "The Fund aims to achieve a target average return of 3% over the benchmark before fees over a market cycle by primarily investing in fixed income instruments issued in the Chinese local currency markets.",
>             "trailerFeeRebateRatio": 0.000065,
>             "expenseRatio": 0.00015,
>             "targetStockRatio": 0,
>             "targetBondRatio": 1,
>             "targetWeight": 0.3
>           },
>           "LU1847653497": {
>             "id": "LU1847653497",
>             "name": "BlackRock BGF China Bond Fund",
>             "instrumentType": "FIXED_INCOME_FUND",
>             "instrumentCcy": "SGD",
>             "description": "The Fund seeks to maximise total return by investing at least 70% of its total assets in fixed income transferable securities denominated in Renminbi or other non-Chinese domestic currencies issued by entities exercising the predominant part of their economic activity in the PRC.",
>             "trailerFeeRebateRatio": 0.000019,
>             "expenseRatio": 0.0001,
>             "targetStockRatio": 0,
>             "targetBondRatio": 1,
>             "targetWeight": 0.7
>           }
>         }
>       },
>       "requestedBy": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$GoalProductLineAndIntentModifiedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "planIds": [
>         "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "
>       ],
>       "previousProductLineAndIntent": {
>         "_type": "SatelliteProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "satelliteType": "CHINA_FI",
>         "ackRiskAdvisoryOverride": true,
>         "ackCustomerInformationAccurate": true
>       },
>       "newProductLineAndIntent": {
>         "_type": "FundSmartProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgments": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       },
>       "modifiedAt": "2025-03-04T16:38:47.366712412+08:00[Asia/Singapore]"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$GoalProductLineAndIntentModifiedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "planIds": [
>         "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "
>       ],
>       "previousProductLineAndIntent": {
>         "_type": "FundSmartProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgments": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       },
>       "newProductLineAndIntent": {
>         "_type": "FundSmartProduct",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgments": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       },
>       "modifiedAt": "2025-03-04T16:38:47.438340959+08:00[Asia/Singapore]",
>       "requestedBy": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$GoalTargetStockRatioUpdatedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "newTargetStockRatio": 0,
>       "newTargetStockRatioSelfSelected": true,
>       "newTargetStockRatioDescription": "Fund Smart portfolio for

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> for Satellite - Technology (GENERAL_WEALTH_ACCUMULATION)",
>       "newMarketRiskToleranceLevel": "CONTROLLER_GROWTH",
>       "newMarketRiskToleranceValue": 0.3,
>       "requestedBy": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "reason": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

**Explicit source context (pr_title):**

> [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script

## A1-2341 — CHINA_FI-to-FundSmart script: rebalance before, after, and ordered event relationships

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Reported d56 verification. Shared source caveats: * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact
> 
> Selected fields with original nesting. The stage keys below are editorial labels for the source headings “Existing entity data” and “Entity state & events after running the script”. The event array retains the source event order. UUID role labels distinguish old/new portfolio identity without exporting literal identifiers.
> 
> ```json
> {
>   "before_script": {
>     "plan": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "currentTaa": {
>         "portfolioId": "[old portfolio identity omitted]",
>         "effectiveDate": "2023-02-16",
>         "instrumentWeights": {
>           "IE00BHXGRN56": 0.3,
>           "LU1847653497": 0.7
>         }
>       },
>       "config": {
>         "rebalancingEnabled": true,
>         "strategy": "THRESHOLD_BASED_STRATEGY"
>       },
>       "isDiscretionaryPortfolio": false
>     }
>   },
>   "after_script": {
>     "plan": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "currentTaa": {
>         "portfolioId": "[new portfolio identity omitted]",
>         "effectiveDate": "2023-02-16",
>         "instrumentWeights": {
>           "IE00BHXGRN56": 0.3,
>           "LU1847653497": 0.7
>         }
>       },
>       "config": {
>         "rebalancingEnabled": true,
>         "strategy": "THRESHOLD_BASED_STRATEGY"
>       },
>       "isDiscretionaryPortfolio": false
>     }
>   },
>   "events_after_script_in_source_order": [
>     {
>       "eventName": "package$PlanTargetAssetAllocationChangedEvt",
>       "event": {
>         "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>         "previousTaa": {
>           "portfolioId": "[old portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "instrumentWeights": {
>             "IE00BHXGRN56": 0.3,
>             "LU1847653497": 0.7
>           }
>         },
>         "newTaa": {
>           "portfolioId": "[new portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "instrumentWeights": {
>             "IE00BHXGRN56": 0.3,
>             "LU1847653497": 0.7
>           }
>         },
>         "reasonForChange": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart",
>         "reason": "PORTFOLIO_CHANGE"
>       }
>     }
>   ]
> }
> ```

**Conditions and limits:**

- Historical reported verification in d56; the displayed JSON is an editorial selected-field view, not a verbatim complete dump and not a recommended current migration procedure.
- The source effective date differs from prod because this d56 fixture was created later. Its goal name remained Satellite - Technology after a Technology-to-ChineFI modification; the source explicitly keeps that misleading name intact.
- before_script and after_script correspond to source headings Existing entity data and Entity state & events after running the script. The events_after_script_in_source_order array preserves the source event order and each event payload nesting, including previous/current/new object roles.
- Old/new portfolio identity labels are editorial replacements for incidental UUID values. The same old and new identities recur across goal, rebalance, trading and charge; no literal entity/customer/account UUID is exported.
- The effectiveDate2023-02-16, IE00BHXGRN56 weight0.3, LU1847653497 weight0.7, risk values, acknowledgement fields and recurring100 values remain source-specific. Unchanged repetitive state and descriptive fund metadata are omitted from the selected view.
- Exact coherent source member/event spans support the selected view; excerpt_scope is an editorial source-section locator and is not quoted source wording.

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "plan": {
>             "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>             "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "planCcy": "SGD",
>             "currentTaa": {
>                 "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                 "effectiveDate": "2023-02-16",
>                 "note": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                 "instrumentWeights": {
>                     "IE00BHXGRN56": 0.3,
>                     "LU1847653497": 0.7
>                 }
>             },
>             "config": {
>                 "rebalancingEnabled": true,
>                 "strategy": "THRESHOLD_BASED_STRATEGY"
>             },
>             "isDiscretionaryPortfolio": false
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "plan": {
>             "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>             "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "planCcy": "SGD",
>             "currentTaa": {
>                 "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                 "effectiveDate": "2023-02-16",
>                 "note": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart",
>                 "instrumentWeights": {
>                     "IE00BHXGRN56": 0.3,
>                     "LU1847653497": 0.7
>                 }
>             },
>             "config": {
>                 "rebalancingEnabled": true,
>                 "strategy": "THRESHOLD_BASED_STRATEGY"
>             },
>             "isDiscretionaryPortfolio": false
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$PlanTargetAssetAllocationChangedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "planCcy": "SGD",
>       "previousTaa": {
>         "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "effectiveDate": "2023-02-16",
>         "note": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "instrumentWeights": {
>           "IE00BHXGRN56": 0.3,
>           "LU1847653497": 0.7
>         }
>       },
>       "newTaa": {
>         "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "effectiveDate": "2023-02-16",
>         "note": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart",
>         "instrumentWeights": {
>           "IE00BHXGRN56": 0.3,
>           "LU1847653497": 0.7
>         }
>       },
>       "reasonForChange": "INV-4049: Switch discontinued CHINA_FI Satellite goals to FundSmart",
>       "reason": "PORTFOLIO_CHANGE",
>       "changedAt": "2025-03-04T16:38:55.48368178+08:00[Asia/Singapore]"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

**Explicit source context (pr_title):**

> [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script

## A1-2342 — CHINA_FI-to-FundSmart script: trading before, after, and ordered event relationships

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Reported d56 verification. Shared source caveats: * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact
> 
> Selected fields with original nesting. The stage keys below are editorial labels for the source headings “Existing entity data” and “Entity state & events after running the script”. The event array retains the source event order. UUID role labels distinguish old/new portfolio identity without exporting literal identifiers.
> 
> ```json
> {
>   "before_script": {
>     "maybeProfile": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD"
>     },
>     "maybeTaa": {
>       "modelPortfolioId": "[old portfolio identity omitted]",
>       "effectiveDate": "2023-02-16",
>       "targetWeights": {
>         "IE00BHXGRN56": 0.3,
>         "LU1847653497": 0.7
>       }
>     }
>   },
>   "after_script": {
>     "maybeProfile": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD"
>     },
>     "maybeTaa": {
>       "modelPortfolioId": "[new portfolio identity omitted]",
>       "effectiveDate": "2023-02-16",
>       "targetWeights": {
>         "IE00BHXGRN56": 0.3,
>         "LU1847653497": 0.7
>       }
>     }
>   },
>   "events_after_script_in_source_order": [
>     {
>       "eventName": "package$PlanTraderTaaUpdatedEvt",
>       "event": {
>         "planProfile": {
>           "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>           "planCcy": "SGD"
>         },
>         "taa": {
>           "modelPortfolioId": "[new portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "targetWeights": {
>             "IE00BHXGRN56": 0.3,
>             "LU1847653497": 0.7
>           }
>         }
>       }
>     }
>   ]
> }
> ```

**Conditions and limits:**

- Historical reported verification in d56; the displayed JSON is an editorial selected-field view, not a verbatim complete dump and not a recommended current migration procedure.
- The source effective date differs from prod because this d56 fixture was created later. Its goal name remained Satellite - Technology after a Technology-to-ChineFI modification; the source explicitly keeps that misleading name intact.
- before_script and after_script correspond to source headings Existing entity data and Entity state & events after running the script. The events_after_script_in_source_order array preserves the source event order and each event payload nesting, including previous/current/new object roles.
- Old/new portfolio identity labels are editorial replacements for incidental UUID values. The same old and new identities recur across goal, rebalance, trading and charge; no literal entity/customer/account UUID is exported.
- The effectiveDate2023-02-16, IE00BHXGRN56 weight0.3, LU1847653497 weight0.7, risk values, acknowledgement fields and recurring100 values remain source-specific. Unchanged repetitive state and descriptive fund metadata are omitted from the selected view.
- Exact coherent source member/event spans support the selected view; excerpt_scope is an editorial source-section locator and is not quoted source wording.

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "maybeProfile": {
>             "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>             "planCcy": "SGD"
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "maybeTaa": {
>             "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "effectiveDate": "2023-02-16",
>             "targetWeights": {
>                 "IE00BHXGRN56": 0.3,
>                 "LU1847653497": 0.7
>             }
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "maybeProfile": {
>       "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "maybeTaa": {
>       "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>       "effectiveDate": "2023-02-16",
>       "targetWeights": {
>         "IE00BHXGRN56": 0.3,
>         "LU1847653497": 0.7
>       }
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "package$PlanTraderTaaUpdatedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "planProfile": {
>         "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>         "planCcy": "SGD"
>       },
>       "taa": {
>         "modelPortfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "effectiveDate": "2023-02-16",
>         "targetWeights": {
>           "IE00BHXGRN56": 0.3,
>           "LU1847653497": 0.7
>         }
>       }
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

**Explicit source context (pr_title):**

> [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script

## A1-2343 — CHINA_FI-to-FundSmart script: charge before, after, and ordered event relationships

**Source stance:** reported-verification

**Context:**

> component: None; operation: [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Reported d56 verification. Shared source caveats: * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact
> 
> Selected fields with original nesting. The stage keys below are editorial labels for the source headings “Existing entity data” and “Entity state & events after running the script”. The event array retains the source event order. UUID role labels distinguish old/new portfolio identity without exporting literal identifiers.
> 
> ```json
> {
>   "before_script": {
>     "profile": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "goalType": "GENERAL_WEALTH_ACCUMULATION",
>       "productLineAndIntent": {
>         "_type": "SatelliteProductDto",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "satelliteType": "CHINA_FI",
>         "ackRiskAdvisoryOverride": true,
>         "ackCustomerInformationAccurate": true
>       },
>       "targetPortfolio": {
>         "portfolioId": "[old portfolio identity omitted]",
>         "effectiveDate": "2023-02-16",
>         "isDiyPortfolio": false
>       }
>     }
>   },
>   "after_script": {
>     "profile": {
>       "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>       "planCcy": "SGD",
>       "goalType": "GENERAL_WEALTH_ACCUMULATION",
>       "productLineAndIntent": {
>         "_type": "FundSmartProductDto",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgements": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       },
>       "targetPortfolio": {
>         "portfolioId": "[new portfolio identity omitted]",
>         "effectiveDate": "2023-02-16",
>         "isDiyPortfolio": true
>       }
>     }
>   },
>   "events_after_script_in_source_order": [
>     {
>       "eventName": "FeePlanProductLineModifiedEvt",
>       "event": {
>         "previousProductLine": {
>           "_type": "SatelliteProductDto",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "satelliteType": "CHINA_FI",
>           "ackRiskAdvisoryOverride": true,
>           "ackCustomerInformationAccurate": true
>         },
>         "newProductLine": {
>           "_type": "FundSmartProductDto",
>           "goalType": "GENERAL_WEALTH_ACCUMULATION",
>           "investmentHorizonInYears": 30,
>           "riskToleranceLevel": "CONTROLLER_GROWTH",
>           "riskToleranceValue": 0.3,
>           "acknowledgements": {
>             "fundSmartNoAdvice": true,
>             "fundSmartCustomerInformationStillAccurate": true
>           }
>         }
>       }
>     },
>     {
>       "eventName": "TargetPortfolioUpdatedEvt",
>       "event": {
>         "targetPortfolio": {
>           "portfolioId": "[new portfolio identity omitted]",
>           "effectiveDate": "2023-02-16",
>           "isDiyPortfolio": true
>         }
>       }
>     }
>   ]
> }
> ```

**Conditions and limits:**

- Historical reported verification in d56; the displayed JSON is an editorial selected-field view, not a verbatim complete dump and not a recommended current migration procedure.
- The source effective date differs from prod because this d56 fixture was created later. Its goal name remained Satellite - Technology after a Technology-to-ChineFI modification; the source explicitly keeps that misleading name intact.
- before_script and after_script correspond to source headings Existing entity data and Entity state & events after running the script. The events_after_script_in_source_order array preserves the source event order and each event payload nesting, including previous/current/new object roles.
- Old/new portfolio identity labels are editorial replacements for incidental UUID values. The same old and new identities recur across goal, rebalance, trading and charge; no literal entity/customer/account UUID is exported.
- The effectiveDate2023-02-16, IE00BHXGRN56 weight0.3, LU1847653497 weight0.7, risk values, acknowledgement fields and recurring100 values remain source-specific. Unchanged repetitive state and descriptive fund metadata are omitted from the selected view.
- Exact coherent source member/event spans support the selected view; excerpt_scope is an editorial source-section locator and is not quoted source wording.

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> * effective date is different from prod, since we created it much later for d56
> * goalName is little misleading, but it was Technology first then modified to ChineFI without updating name - keeping this intact

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "profile": {
>             "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>             "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "goalType": "GENERAL_WEALTH_ACCUMULATION",
>             "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "planCcy": "SGD",
>             "targetPortfolio": {
>                 "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                 "effectiveDate": "2023-02-16",
>                 "isDiyPortfolio": false
>             },
>             "productLineAndIntent": {
>                 "_type": "SatelliteProductDto",
>                 "goalType": "GENERAL_WEALTH_ACCUMULATION",
>                 "investmentHorizonInYears": 30,
>                 "riskToleranceLevel": "CONTROLLER_GROWTH",
>                 "satelliteType": "CHINA_FI",
>                 "ackRiskAdvisoryOverride": true,
>                 "ackCustomerInformationAccurate": true
>             }
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "profile": {
>             "customerId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "tradingAccountType": "SINGAPORE_SGD_CASH_ACCOUNT",
>             "goalId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "goalType": "GENERAL_WEALTH_ACCUMULATION",
>             "planId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>             "planCcy": "SGD",
>             "targetPortfolio": {
>                 "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>                 "effectiveDate": "2023-02-16",
>                 "isDiyPortfolio": true
>             },
>             "productLineAndIntent": {
>                 "_type": "FundSmartProductDto",
>                 "goalType": "GENERAL_WEALTH_ACCUMULATION",
>                 "investmentHorizonInYears": 30,
>                 "riskToleranceLevel": "CONTROLLER_GROWTH",
>                 "riskToleranceValue": 0.3,
>                 "acknowledgements": {
>                     "fundSmartNoAdvice": true,
>                     "fundSmartCustomerInformationStillAccurate": true
>                 }
>             }
>         }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "FeePlanProductLineModifiedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "previousProductLine": {
>         "_type": "SatelliteProductDto",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "satelliteType": "CHINA_FI",
>         "ackRiskAdvisoryOverride": true,
>         "ackCustomerInformationAccurate": true
>       },
>       "newProductLine": {
>         "_type": "FundSmartProductDto",
>         "goalType": "GENERAL_WEALTH_ACCUMULATION",
>         "investmentHorizonInYears": 30,
>         "riskToleranceLevel": "CONTROLLER_GROWTH",
>         "riskToleranceValue": 0.3,
>         "acknowledgements": {
>           "fundSmartNoAdvice": true,
>           "fundSmartCustomerInformationStillAccurate": true
>         }
>       },
>       "modifiedAt": "2025-03-04T16:38:47.366712412+08:00[Asia/Singapore]"
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "eventName": "TargetPortfolioUpdatedEvt"

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> "event": {
>       "targetPortfolio": {
>         "portfolioId": "

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

> ",
>         "effectiveDate": "2023-02-16",
>         "isDiyPortfolio": true
>       }
>     }

**Evidence:** anon-1.jsonl:2358 · comment 601837814 · PR 11287 · 2025-03-04

**Explicit source context (pr_title):**

> [INV-4049] feat(amend-scripts): Add SwitchAdvisedToFundSmart script

## A1-2367 — Investment service also owns timestamp-bearing fee config

**Source stance:** explanation

**Context:**

> component: investment-impl/src/main/scala/com/endowus/silver/investment/impl/logic/service/impl/ServiceLogicImpl.scala; operation: Resolve INV-3808: Enhance investment requests to use sales fee config request; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Urgh, investment svc also has its own Config with TS field

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2382 · comment 582766822 · PR 10740 · 2025-01-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Resolve INV-3808: Enhance investment requests to use sales fee config request

**Evidence:** anon-1.jsonl:2382 · comment 582766822 · PR 10740 · 2025-01-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> cashReservations = request.cashReservations.map(CashReservation.apply)
>  
> -      maybeTransactionFee <- calculateTransactionFee(request.requestedAmount, request.transactionFeeConfig.map(TransactionFeeConfig.fromDto))
> +      transactionFeeConfig = request.transactionFeeConfig.map(TransactionFeeConfig.fromGoalRequest(_, dateTimeProvider.now))
> +      maybeTransactionFee <- calculateTransactionFee(request.requestedAmount, transactionFeeConfig)
>  
>        maybeFinancialAdvisorId <- getFinancialAdvisorIdByCustomerId(request.customerId)

## A1-2368 — Use same timestamp for all fee configs

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; operation: Resolve INV-3808: Enhance investment requests to use sales fee config request; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Use same TS for all these

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2383 · comment 582767718 · PR 10740 · 2025-01-06

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Resolve INV-3808: Enhance investment requests to use sales fee config request

**Evidence:** anon-1.jsonl:2383 · comment 582767718 · PR 10740 · 2025-01-06

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> val getPortfolioFut = portfolioService.getPortfolioById(request.modelPortfolioId).invoke()
>      val getGoalFut = refProvider.getGoalEntityRef(request.goalId).ask(GetGoalCmd(_))
>      val planIdToUse: UUID = mkPlanId(request.customerId, request.goalId, request.tradingAccountType)
> +    val now = dateTimeProvider.now

## A1-2371 — Add optional CKA snapshot to existing format

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/GoalSupportingDataVo.scala; operation: INV-3900: Changes to persist customer cka snapshot on approval; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s keep this optional and add to existing one

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2387 · comment 608503392 · PR 11332 · 2025-03-13

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/GoalSupportingDataVo.scala`

**Explicit source context (pr_title):**

> INV-3900: Changes to persist customer cka snapshot on approval

**Evidence:** anon-1.jsonl:2387 · comment 608503392 · PR 11332 · 2025-03-13

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/GoalSupportingDataVo.scala`

**Explicit source context (hunk):**

> ) extends GoalSupportingData
>  
>  object GoalSupportingData {
>    implicit private val cfg: Aux[MacroOptions] = JsonUtils.configForTypeParameter()
>  
> -  private implicit val actionApprovedDetailsDataFormat: Format[ActionApprovedDetailsData] = Json.format
> +  implicit private val actionApprovedDetailsDataFormat: Format[ActionApprovedDetailsData] = Json.format
>  
>    implicit val format: Format[GoalSupportingData] = Json.format

## A1-2372 — Goal persistence owns its own CKA snapshot DTO

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/GoalSupportingDataVo.scala; operation: INV-3900: Changes to persist customer cka snapshot on approval; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s make our own DTO since we are persisting in goal

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:2388 · comment 608504790 · PR 11332 · 2025-03-13

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/GoalSupportingDataVo.scala`

**Explicit source context (pr_title):**

> INV-3900: Changes to persist customer cka snapshot on approval

**Evidence:** anon-1.jsonl:2388 · comment 608504790 · PR 11332 · 2025-03-13

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/GoalSupportingDataVo.scala`

**Explicit source context (hunk):**

> +    expiryDate: Option[LocalDate],
> +    ckaMethod: Option[String]
> +  )
> +  object Qualification {
> +    implicit val customerCkaSnapshotDetailsQualificationFormat: Format[Qualification] = Json.format
> +  }
> +
> +  implicit val customerCkaSnapshotDetailsFormat: Format[CustomerCkaSnapshotDetails] = Json.format
> +

## A1-2430 — Replace separate events with InstructionFinished plus Submitted

**Source stance:** open-question

**Context:**

> component: trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/ces/events/package.scala; operation: [INV-3710] feat(inter plan transfer): handle comms for transfer instructions; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We’re removing these events, and changing them to single `InstrumentTransferInstructionFinishedEvt`, together with `InstrumentTransferInstructionSubmittedEvt`?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2451 · comment 578061626 · PR 10435 · 2024-12-16

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/ces/events/package.scala`

**Explicit source context (pr_title):**

> [INV-3710] feat(inter plan transfer): handle comms for transfer instructions

## A2-0025 — package: We may decide to make it required field in DTO after successful backfill \(or adding on-the-fly lookup\), but here it must stay optional as [person] said, due to histor...

**Source stance:** explanation

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala; original row 25.

**Concern stated in the source:** Historical events and snapshots can lack tenantId.

**Source-preserving request, proposal, or question:**

> We may decide to make it required field in DTO after successful backfill \(or adding on-the-fly lookup\), but here it must stay optional as [person] said, due to historical events & snapshots

**Conditions and limits:**

- The DTO may become required after successful backfill or on-the-fly lookup; historical events/snapshots must remain optional.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:25 · comment 609023920 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

> We may decide to make it required field in DTO after successful backfill \(or adding on-the-fly lookup\), but here it must stay optional as

**Evidence:** anon-2.jsonl:25 · comment 609023920 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

> said, due to historical events & snapshots

**Evidence:** anon-2.jsonl:25 · comment 609023920 · PR 11333 · 2025-03-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0067 — TradingRestrictionResponse: Do we need to serdes this `ErrorCategory`?

**Source stance:** open-question

**Context:**

> PR 5423 (Refactor (compliance/investment): Refactor RestrictionError/RestrictionWarning to include categories.), compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionResponse.scala; original row 67.

**Source-preserving request, proposal, or question:**

> Do we need to serdes this `ErrorCategory`?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:67 · comment 377379925 · PR 5423 · 2023-03-13

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionResponse.scala`

**Evidence:** anon-2.jsonl:67 · comment 377379925 · PR 5423 · 2023-03-13

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/tradingRestriction/TradingRestrictionResponse.scala`

**Explicit source context (pr_title):**

> Refactor (compliance/investment): Refactor RestrictionError/RestrictionWarning to include categories.

## A2-0104 — package: We cannot use DTO, especially other services' DTO in our domain event. It can feel clumsy at times, but always better and safer to redefine the model.

**Source stance:** explanation

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/events/package.scala; original row 104.

**Concern stated in the source:** Persisted domain events must not embed service DTOs, especially DTOs owned by other services.

**Source-preserving request, proposal, or question:**

> We cannot use DTO, especially other services' DTO in our domain event. It can feel clumsy at times, but always better and safer to redefine the model.

**Conditions and limits:**

- Do not infer that every API DTO is forbidden everywhere: this comment is specifically about DTOs inside domain events.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:104 · comment 587730434 · PR 10896 · 2025-01-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/events/package.scala`

**Evidence:** anon-2.jsonl:104 · comment 587730434 · PR 10896 · 2025-01-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/ces/events/package.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0123 — Goal approval events adjacent to PlanRecurringInvestmentScheduleRemovedEvt

**Source stance:** requested-change

**Context:**

> PR 10896 ([INV-3426] feat(bff, advisory, goal, investment): Approval flow), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/ces/events/package.scala; original row 123.

**Source-preserving request, proposal, or question:**

> Let’s keep these near to their counterpart, e.g. `PlanRecurringInvestmentScheduleRemovedEvt`
> 
> ‌

**Conditions and limits:**

- Keep approval-related event declarations near their counterparts, with PlanRecurringInvestmentScheduleRemovedEvt as the explicit example. The particular declarations meant by these are not named.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:123 · comment 587732733 · PR 10896 · 2025-01-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/ces/events/package.scala`

**Evidence:** anon-2.jsonl:123 · comment 587732733 · PR 10896 · 2025-01-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/ces/events/package.scala`

**Explicit source context (pr_title):**

> [INV-3426] feat(bff, advisory, goal, investment): Approval flow

## A2-0231 — ClientEntity: You will need to add `TenantSvcException` in tenant-impl that extends `PlayJsonSerializable` otherwise serdes will fail in cluster mode

**Source stance:** explanation

**Context:**

> PR 10576 ([ONB-4302][ONB-4308] B2C tenantId fallback and Not Found error for getClientById), tenant-impl/src/main/scala/com/endowus/silver/tenant/impl/client/entities/ClientEntity.scala; original row 231.

**Concern stated in the source:** TenantSvcException in tenant-impl must extend PlayJsonSerializable for cluster-mode serialization.

**Source-preserving request, proposal, or question:**

> You will need to add `TenantSvcException` in tenant-impl that extends `PlayJsonSerializable` otherwise serdes will fail in cluster mode

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:231 · comment 576372484 · PR 10576 · 2024-12-10

Source path: `tenant-impl/src/main/scala/com/endowus/silver/tenant/impl/client/entities/ClientEntity.scala`

**Evidence:** anon-2.jsonl:231 · comment 576372484 · PR 10576 · 2024-12-10

Source path: `tenant-impl/src/main/scala/com/endowus/silver/tenant/impl/client/entities/ClientEntity.scala`

**Explicit source context (pr_title):**

> [ONB-4302][ONB-4308] B2C tenantId fallback and Not Found error for getClientById

## A2-0312 — RecurringInvestmentScheduleHistoryDataEventProcessorV3: Maybe we check w data team on this table is used? I’m not sure about adding another row to history entries when backfilli...

**Source stance:** open-question

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessorV3.scala; original row 312.

**Concern stated in the source:** A backfill row in history may surprise consumers; V3 already maps missing fundingInstructions from investmentAmount.

**Source-preserving request, proposal, or question:**

> Maybe we check w data team on this table is used? I’m not sure about adding another row to history entries when backfilling is what they would expect.
> 
> * `PlanRecurringInvestmentScheduleHistoryTable` persists only `investmentAmount`, so we don’t really care
> * `PlanRecurringInvestmentScheduleHistoryTableV3` has the default logic to map `investmentAmount` to `fundingInstructions`, if `fundingInstructions` is not set already - which is exactly the purpose of this backfill evt
> 
> ‌

**Conditions and limits:**

- The history-table consumer expectation is an open question, and the two history versions differ.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:312 · comment 570859873 · PR 10417 · 2024-11-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessorV3.scala`

**Evidence:** anon-2.jsonl:312 · comment 570859873 · PR 10417 · 2024-11-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessorV3.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0347 — GoalSupportingDataTableV1: `GoalActionContext` covers `CREATION_APPROVED, MODIFICATION_APPROVED` which is initiated from goal svc

**Source stance:** suggestion

**Context:**

> PR 10335 (Feat/INV-3508 goal create projections), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala; original row 347.

**Source-preserving request, proposal, or question:**

> `GoalActionContext` covers `CREATION_APPROVED, MODIFICATION_APPROVED` which is initiated from goal svc
> 
> ‌
> 
> Then later for investment/redemption flow:
> 
> * add INVESTMENT\_APPROVED / REDEMPTION\_APPROVED to this enum
> * how to populate:
> 
>     * projection on investment/redemption will endpoint on goal svc to upsert this table
>     * OR emit kafka message from investment/redemption, and goal subscribe and upsert this table
>     
> 
> ‌
> 
> Then later, if ever, for adhoc documents upload to a goal:
> 
> * endpoint to persist event to goal, which go thru projection to upsert this table
> 
> ‌
> 
> How to upversion this table?
> 
> * table design is already as flexible as possible
> * if really to upversion, we just need new projection in goal & sync from investment/redemption
> 
> ‌

**Conditions and limits:**

- Investment/redemption may later upsert via goal endpoint or Kafka; both are alternatives, not a settled implementation. Adhoc upload can persist an event; table upversion can use a new goal projection and sync.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:347 · comment 564025013 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala`

**Evidence:** anon-2.jsonl:347 · comment 564025013 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create projections

## A2-0434 — Review: I think we should:

**Source stance:** suggestion

**Context:**

> PR 10262 (Feat/INV-3637 bff endpoint upload document), no inline path; original row 434.

**Concern stated in the source:** Document upload has no customer context, whereas GET must verify customer/context ownership in the domain edge service.

**Source-preserving request, proposal, or question:**

> I think we should:
> 
> * create new endpoint in document svc `/api/v1/document/upload` with this UploadDocumentRequest type \(maybe optional documentId if there is need to control this id from caller\), and its logic calls `createDocumentWithBinaries` providing the OTHERS value for the deprecated enums
> * create authenticated endpoint in BFF proxy to above endpoint in document svc, for advisor portal, ~~which requires \(CUSTOMER:DOCUMENT resource & Create permission\)~~
> * do not allow for client portal for now, since there is no planned flow that requires this yet
> 
> ‌
> 
> Later on when we add GET endpoints, then it will be applicable for both advisor portal and client portal, ~~both require \(CUSTOMER:DOCUMENT resource & Read permission\)~~
> 
> Unlike the POST upload endpoint which doesn’t care about the context of document, the GET ones must care and validate the document indeed belongs to the customer \+ context. Hence these GET endpoints will have to be edge in the context service, e.g. goal/customer svc instead of direct document svc. This means these services would be responsible to capture the generated documentId from the upload endpoint.
> 
> ‌
> 
> Example for add goal flow:
> 
> * FA uploads document in advisor-portal → calls BFF to proxy to document svc → advisor-portal captures generated documentId
> * FA confirms to create the add-goal approval request in advisor-portal → calls BFF to proxy to advisory svc, which eventually creates workflow in workflow-engine
> 
>     * The workflow request must contain all the documentIds associated with this add-goal request
>     
> * When workflow request is fully approved → workflow-engine calls advisory svc which calls goal svc to create goal
> 
>     * We need to somehow persist these documentIds to the goalId
>     
> * When customer retrieves suitability doc from goal page in client-portal → calls BFF to proxy to goal svc `GET /api/v1/goal/:goalId/document` or `GET /api/v1/goal/:goalId/document/:documentId`
> 
>     * BFF validates goalId belongs to customerId
>     * goal svc validates documentId belongs to goalId
>     
> 
> ‌

**Conditions and limits:**

- The CUSTOMER:DOCUMENT RBAC suggestions in this source comment are struck through and clarified in row 436; do not revive them as requirements for bare upload.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:434 · comment 559277045 · PR 10262 · 2024-10-30

**Evidence:** anon-2.jsonl:434 · comment 559277045 · PR 10262 · 2024-10-30

**Explicit source context (pr_title):**

> Feat/INV-3637 bff endpoint upload document

## A2-0435 — Review: How to persist documentIds for goal? One approach could be below \(we can review again later\)

**Source stance:** suggestion

**Context:**

> PR 10262 (Feat/INV-3637 bff endpoint upload document), no inline path; original row 435.

**Source-preserving request, proposal, or question:**

> How to persist documentIds for goal? One approach could be below \(we can review again later\)
> 
> * projection on `GoalCreationApprovedEvt`
> 
>     * take approved workflowId, calls workflow-engine to query associated request payload
>     * extract documentIds \(goal-impl depends on advisory-api \+ workflow-engine-api\) and persist to CRUD table for \(goalId \+ context\) → documentIds\[\]
>     
> * if we ever have adhoc docs upload per goal
> 
>     * if there is event, persist to CRUD table via projection
>     * if there is no event, persist to CRUD table directly
>     
> 
> ‌
> 
> If we ever have docs for other flow, e.g. investment/redemption/etc
> 
> * follow same approach as goal svc
> * `GET /api/v1/goal/:goalId/document` must compose from all underlying sources including goal \+ investment/redemption/etc
> 
> ‌

**Conditions and limits:**

- Document persistence via GoalCreationApprovedEvt projection is explicitly one possible design for later review; event/no-event adhoc paths are alternatives.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:435 · comment 559297294 · PR 10262 · 2024-10-30

**Evidence:** anon-2.jsonl:435 · comment 559297294 · PR 10262 · 2024-10-30

**Explicit source context (pr_title):**

> Feat/INV-3637 bff endpoint upload document

## A2-0445 — package: Just double check if we can easily delete obsolete workflows in dynamic-env, cuz these DTO will be persisted there

**Source stance:** open-question

**Context:**

> PR 10281 (Feat/INV-3508 b2b goal create dtos), advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/fee/package.scala; original row 445.

**Concern stated in the source:** Persisted dynamic-env DTOs may require obsolete workflow deletion while evolving shape.

**Source-preserving request, proposal, or question:**

> Just double check if we can easily delete obsolete workflows in dynamic-env, cuz these DTO will be persisted there

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:445 · comment 561611494 · PR 10281 · 2024-11-06

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/fee/package.scala`

**Evidence:** anon-2.jsonl:445 · comment 561611494 · PR 10281 · 2024-11-06

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/fee/package.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 b2b goal create dtos

## A2-0698 — ServiceLogicImpl: if BENCHMARK & DIY, safe to use `currentAllocationTarget` 

**Source stance:** explanation

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; original row 698.

**Concern stated in the source:** if BENCHMARK & DIY, safe to use `currentAllocationTarget` 

if ADVISED, use `getPortfolioVersions` and persist for all versions

‌

**Source-preserving request, proposal, or question:**

> if BENCHMARK & DIY, safe to use `currentAllocationTarget` 
> 
> if ADVISED, use `getPortfolioVersions` and persist for all versions
> 
> ‌

**Conditions and limits:**

- BENCHMARK/DIY use currentAllocationTarget, while ADVISED requires all getPortfolioVersions.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:698 · comment 524636610 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:698 · comment 524636610 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0712 — PortfolioMonthlyChangesHelper: 1. Let’s not persist dummy values \(empty or last value\) on failure

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala; original row 712.

**Concern stated in the source:** 1. Let’s not persist dummy values \(empty or last value\) on failure
2. Maybe we can validate instrument mc → log error at instrument, then can we log warn with it’s instrument mc issue. Otherwise we log error if portfolio mc calculation issue. That would require `generatePortfolioMonthlyChanges` to throw more specific exception

‌

**Source-preserving request, proposal, or question:**

> 1. Let’s not persist dummy values \(empty or last value\) on failure
> 2. Maybe we can validate instrument mc → log error at instrument, then can we log warn with it’s instrument mc issue. Otherwise we log error if portfolio mc calculation issue. That would require `generatePortfolioMonthlyChanges` to throw more specific exception
> 
> ‌

**Conditions and limits:**

- Do not persist empty/last dummy values after failure. Distinguish instrument-MC validation errors (instrument error, portfolio warning) from portfolio-calculation errors, requiring more specific exceptions.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:712 · comment 524619598 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Evidence:** anon-2.jsonl:712 · comment 524619598 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0714 — PortfolioMonthlyChangesHelper: Let’s move this conditional calc to `generateMonthlyChangesAndUpsert`

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala; original row 714.

**Concern stated in the source:** Let’s move this conditional calc to `generateMonthlyChangesAndUpsert`

```
// lookup instrument mc
// top up if has maybeInstrumentOverride

// find latest YM of each instrument in instrumentMonthlyChanges
// if all same AND >= existing portfolio latest YM (if any)
// calculate

// else if forceSync
// calculate

// else
// just persist latest YM of each instrument
```

‌

**Source-preserving request, proposal, or question:**

> Let’s move this conditional calc to `generateMonthlyChangesAndUpsert`
> 
> ```
> // lookup instrument mc
> // top up if has maybeInstrumentOverride
> 
> // find latest YM of each instrument in instrumentMonthlyChanges
> // if all same AND >= existing portfolio latest YM (if any)
> // calculate
> 
> // else if forceSync
> // calculate
> 
> // else
> // just persist latest YM of each instrument
> ```
> 
> ‌

**Conditions and limits:**

- Only calculate if all latest instrument YearMonths agree and are >= existing latest portfolio YearMonth, or forceSync; otherwise persist each instrument latest YearMonth only.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:714 · comment 524629024 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Evidence:** anon-2.jsonl:714 · comment 524629024 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0809 — ServiceClientExceptionSerializer: Move this to akka-client-common? Anyhow akka-client-common depends on silver-commons, so we can just move it there so all service client API st...

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), silver-commons/src/main/scala/com/endowus/silver/commons/exception/ServiceClientExceptionSerializer.scala; original row 809.

**Concern stated in the source:** Move this to akka-client-common? Anyhow akka-client-common depends on silver-commons, so we can just move it there so all service client API stays in one place

**Source-preserving request, proposal, or question:**

> Move this to akka-client-common? Anyhow akka-client-common depends on silver-commons, so we can just move it there so all service client API stays in one place

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:809 · comment 516343502 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/exception/ServiceClientExceptionSerializer.scala`

**Evidence:** anon-2.jsonl:809 · comment 516343502 · PR 9440 · 2024-07-02

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/exception/ServiceClientExceptionSerializer.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0818 — ServiceClientExceptionSerializerTest: Let’s add a positive test too?

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala; original row 818.

**Source-preserving request, proposal, or question:**

> Let’s add a positive test too?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:818 · comment 525233980 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala`

**Evidence:** anon-2.jsonl:818 · comment 525233980 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0820 — ServiceClientExceptionSerializerTest: Shouldn’t it be `implicit val system: ActorSystem`

**Source stance:** suggestion

**Context:**

> PR 9440 ([LAGOM-97] (timeseries) Lagom client removal for timeseries), akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala; original row 820.

**Concern stated in the source:** Shouldn’t it be `implicit val system: ActorSystem`

‌

**Source-preserving request, proposal, or question:**

> Shouldn’t it be `implicit val system: ActorSystem`
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:820 · comment 525234003 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala`

**Evidence:** anon-2.jsonl:820 · comment 525234003 · PR 9440 · 2024-07-26

Source path: `akka-client-commons/src/test/scala/ServiceClientExceptionSerializerTest.scala`

**Explicit source context (pr_title):**

> [LAGOM-97] (timeseries) Lagom client removal for timeseries

## A2-0929 — package: We won’t be sending this as separate payload anywhere between the actors, so shouldn’t need extend `PlayJsonSerializable`

**Source stance:** explanation

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala; original row 929.

**Concern stated in the source:** We won’t be sending this as separate payload anywhere between the actors, so shouldn’t need extend `PlayJsonSerializable`

**Source-preserving request, proposal, or question:**

> We won’t be sending this as separate payload anywhere between the actors, so shouldn’t need extend `PlayJsonSerializable`

**Conditions and limits:**

- PlayJsonSerializable is unnecessary only because this object is not sent separately between actors.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:929 · comment 520040192 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

**Evidence:** anon-2.jsonl:929 · comment 520040192 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/state/package.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0983 — SgComplianceChecker: Let’s just rename existing to SgComplianceCkaRestrictionViolation and add new SgComplianceTradingRestrictionViolation, both extends ComplianceViolation? Thi...

**Source stance:** suggestion

**Context:**

> PR 9262 (TT-4461 Investment calling checkCustomerTradingRestrictionV3), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/SgComplianceChecker.scala; original row 983.

**Concern stated in the source:** Let’s just rename existing to SgComplianceCkaRestrictionViolation and add new SgComplianceTradingRestrictionViolation, both extends ComplianceViolation? This thing is not persisted, so should be ok

**Source-preserving request, proposal, or question:**

> Let’s just rename existing to SgComplianceCkaRestrictionViolation and add new SgComplianceTradingRestrictionViolation, both extends ComplianceViolation? This thing is not persisted, so should be ok

**Conditions and limits:**

- Exception/type rename is considered safe because ComplianceViolation is not persisted.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:983 · comment 507982903 · PR 9262 · 2024-06-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/SgComplianceChecker.scala`

**Evidence:** anon-2.jsonl:983 · comment 507982903 · PR 9262 · 2024-06-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/SgComplianceChecker.scala`

**Explicit source context (pr_title):**

> TT-4461 Investment calling checkCustomerTradingRestrictionV3

## A2-1050 — GoalBasedStatementInfoDbDto: I’m not sure if we need all these new fields in `*DbDto`. As I understand, these DTO are persisted and used to check if a statement is reprint or not.

**Source stance:** explanation

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala; original row 1050.

**Concern stated in the source:** I’m not sure if we need all these new fields in `*DbDto`. As I understand, these DTO are persisted and used to check if a statement is reprint or not.

Generally, we do not change isDiscretionary flag of a goal - even if we do, we probably can force-reprint if needed, rather than storing these fields?

--

Even if we don’t change these DTO, the page content would already changed due to new format. It’s a more generic question for report svc, how do we version the statement design to avoid mass reprint / support ability to print an old month using old format, etc…

**Source-preserving request, proposal, or question:**

> I’m not sure if we need all these new fields in `*DbDto`. As I understand, these DTO are persisted and used to check if a statement is reprint or not.
> 
> Generally, we do not change isDiscretionary flag of a goal - even if we do, we probably can force-reprint if needed, rather than storing these fields?
> 
> --
> 
> Even if we don’t change these DTO, the page content would already changed due to new format. It’s a more generic question for report svc, how do we version the statement design to avoid mass reprint / support ability to print an old month using old format, etc…

**Conditions and limits:**

- Persisted *DbDto fields drive reprint detection. isDiscretionary rarely changes and force-reprint may suffice; broader old-format/versioning versus mass-reprint question is unresolved.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1050 · comment 502458481 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Evidence:** anon-2.jsonl:1050 · comment 502458481 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1056 — package: Should be compatible cuz this is not persisted \(only the `*DbDto` are persisted\).

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala; original row 1056.

**Concern stated in the source:** Should be compatible cuz this is not persisted \(only the `*DbDto` are persisted\).

I see some lookup done by traversing this list. If it’s safe to refactor, should we just change to

```
goalIdsToDisplay: List[UUID], // ordering is maintained here
goalInfoByGoalId: Map[UUID, GoalInfoToDisplay] // lookup only
```

‌

**Source-preserving request, proposal, or question:**

> Should be compatible cuz this is not persisted \(only the `*DbDto` are persisted\).
> 
> I see some lookup done by traversing this list. If it’s safe to refactor, should we just change to
> 
> ```
> goalIdsToDisplay: List[UUID], // ordering is maintained here
> goalInfoByGoalId: Map[UUID, GoalInfoToDisplay] // lookup only
> ```
> 
> ‌

**Conditions and limits:**

- List+Map is a proposed lookup/order refactor, but row 1064 later accepts leaving it a List after usage review. Only *DbDto are persisted.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1056 · comment 502456452 · PR 9052 · 2024-05-21

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala`

**Evidence:** anon-2.jsonl:1056 · comment 502456452 · PR 9052 · 2024-05-21

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1064 — package: [person] after checking the usage of this class again, I’m convinced that

**Source stance:** explanation

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala; original row 1064.

**Concern stated in the source:** [person] after checking the usage of this class again, I’m convinced that

* it’s not used for public DTO - let’s move to report-impl instead, otherwise it can be confusing to see `*RawData` case class in report-api. I think these can just stay in `GoalBasedStatementDataGenerator`
* it’s not used at all for serdes, not even in test - so we don’t need the format at all

‌

I checked the lookup usage of this `goalsInfoForDisplay`. Not too bad so I guess we can leave it as a List still. But let’s move both `GoalBasedStatementRawData` and `GoalInfoToDisplay` to impl so that it’s less confusing on usage scope

**Source-preserving request, proposal, or question:**

> [person] after checking the usage of this class again, I’m convinced that
> 
> * it’s not used for public DTO - let’s move to report-impl instead, otherwise it can be confusing to see `*RawData` case class in report-api. I think these can just stay in `GoalBasedStatementDataGenerator`
> * it’s not used at all for serdes, not even in test - so we don’t need the format at all
> 
> ‌
> 
> I checked the lookup usage of this `goalsInfoForDisplay`. Not too bad so I guess we can leave it as a List still. But let’s move both `GoalBasedStatementRawData` and `GoalInfoToDisplay` to impl so that it’s less confusing on usage scope

**Conditions and limits:**

- After inspection, raw-data classes are neither public DTOs nor serialized; move GoalBasedStatementRawData/GoalInfoToDisplay into report-impl and remove format. List lookup is accepted, revising row 1056.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1064 · comment 503067120 · PR 9052 · 2024-05-22

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala`

> after checking the usage of this class again, I’m convinced that
> 
> * it’s not used for public DTO - let’s move to report-impl instead, otherwise it can be confusing to see `*RawData` case class in report-api. I think these can just stay in `GoalBasedStatementDataGenerator`
> * it’s not used at all for serdes, not even in test - so we don’t need the format at all
> 
> ‌
> 
> I checked the lookup usage of this `goalsInfoForDisplay`. Not too bad so I guess we can leave it as a List still. But let’s move both `GoalBasedStatementRawData` and `GoalInfoToDisplay` to impl so that it’s less confusing on usage scope

**Evidence:** anon-2.jsonl:1064 · comment 503067120 · PR 9052 · 2024-05-22

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1073 — PushNotificationProviderData: In theory these should be optional \(otherwise we might break serdes of there are lagged messages in the kafka topic\), but I guess this one is ok ...

**Source stance:** explanation

**Context:**

> PR 9257 (TT-4230 autofund upcoming recur inv comms), communication-api/src/main/scala/com/endowus/silver/communication/api/v2/pushNotitification/PushNotificationProviderData.scala; original row 1073.

**Concern stated in the source:** In theory these should be optional \(otherwise we might break serdes of there are lagged messages in the kafka topic\), but I guess this one is ok cuz we know this type of notification is only triggered in the morning

**Source-preserving request, proposal, or question:**

> In theory these should be optional \(otherwise we might break serdes of there are lagged messages in the kafka topic\), but I guess this one is ok cuz we know this type of notification is only triggered in the morning

**Conditions and limits:**

- Optionality is generally needed for lagged Kafka messages, but this morning-only notification is explicitly accepted as a narrow exception.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1073 · comment 508952279 · PR 9257 · 2024-06-07

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/v2/pushNotitification/PushNotificationProviderData.scala`

**Evidence:** anon-2.jsonl:1073 · comment 508952279 · PR 9257 · 2024-06-07

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/v2/pushNotitification/PushNotificationProviderData.scala`

**Explicit source context (pr_title):**

> TT-4230 autofund upcoming recur inv comms

## A2-1081 — ReportApplication: Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.

**Source stance:** suggestion

**Context:**

> PR 9306 (Feat/EN-3405 use tasktopicsubscriber in report for manual start/stop), report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala; original row 1081.

**Concern stated in the source:** Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.

In case of report, the svc itself is responsible for triggering of the topic producer side. So we can potentially just call start \(via distributed pubsub\) in the same trigger endpoint, i.e. `createMonthlyStatementsV2` first will trigger start, only then produce the message.

* the start is idempotent so if already started, it won’t cause any harm
* the distributed pubsub is at-most once tho, so it could still happen that maybe one of instance does not start… but I suppose this could be checked easily via logs or metrics.

‌

We can also make this pause/resume status persisted, and check upon startup :thumbsup: 

‌

**Source-preserving request, proposal, or question:**

> Just some notes here, yall are right about the trade-offs but manual start is not that bad, depending on use cases.
> 
> In case of report, the svc itself is responsible for triggering of the topic producer side. So we can potentially just call start \(via distributed pubsub\) in the same trigger endpoint, i.e. `createMonthlyStatementsV2` first will trigger start, only then produce the message.
> 
> * the start is idempotent so if already started, it won’t cause any harm
> * the distributed pubsub is at-most once tho, so it could still happen that maybe one of instance does not start… but I suppose this could be checked easily via logs or metrics.
> 
> ‌
> 
> We can also make this pause/resume status persisted, and check upon startup :thumbsup: 
> 
> ‌

**Conditions and limits:**

- Report may start TaskTopicSubscriber idempotently before producing in createMonthlyStatementsV2. Distributed pubsub is at-most-once and may miss an instance; logs/metrics can detect it. Persisted pause/resume is another option.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1081 · comment 508950934 · PR 9306 · 2024-06-07

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala`

**Evidence:** anon-2.jsonl:1081 · comment 508950934 · PR 9306 · 2024-06-07

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala`

**Explicit source context (pr_title):**

> Feat/EN-3405 use tasktopicsubscriber in report for manual start/stop

## A2-1098 — Instrument JDBC processor naming: InstrumentV2JdbcEventProcessorV7

**Source stance:** suggestion

**Context:**

> PR 9014 (Resolve INV-2980: BE changes needed for admin instrument screens), instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessor.scala; original row 1098.

**Source-preserving request, proposal, or question:**

> Let’s follow the existing name, e.g. `InstrumentV2JdbcEventProcessorV7`?
> 
> ‌

**Conditions and limits:**

- InstrumentV2JdbcEventProcessorV7 is the explicit naming example. Do not treat the name as proof that version 7 was deployed or that every service uses this convention.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1098 · comment 499485458 · PR 9014 · 2024-05-09

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:1098 · comment 499485458 · PR 9014 · 2024-05-09

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessor.scala`

**Explicit source context (pr_title):**

> Resolve INV-2980: BE changes needed for admin instrument screens

## A2-1111 — FxWalletDataHelper: Should we return more data than just the rate? Maybe at least `quotationId` and `quotedAt` ? This can be logging or actually get persisted in event too, in c...

**Source stance:** open-question

**Context:**

> PR 9091 ([EN-3271] Add autofx recurring support in investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/FxWalletDataHelper.scala; original row 1111.

**Concern stated in the source:** Should we return more data than just the rate? Maybe at least `quotationId` and `quotedAt` ? This can be logging or actually get persisted in event too, in case we need to trace back

**Source-preserving request, proposal, or question:**

> Should we return more data than just the rate? Maybe at least `quotationId` and `quotedAt` ? This can be logging or actually get persisted in event too, in case we need to trace back

**Conditions and limits:**

- quotationId/quotedAt would aid tracing and could be logged or persisted; the choice remains open.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1111 · comment 500263638 · PR 9091 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/FxWalletDataHelper.scala`

**Evidence:** anon-2.jsonl:1111 · comment 500263638 · PR 9091 · 2024-05-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/FxWalletDataHelper.scala`

**Explicit source context (pr_title):**

> [EN-3271] Add autofx recurring support in investment

## A2-1176 — Review: That would be next step. Need to check w PM regarding where to store, and the query requirement for it. Likely we just need to stamp in productLineAndIntent… and build h...

**Source stance:** suggestion

**Context:**

> PR 9146 (feat(advisory): terms agreement ack for add goal flagship dpm simulation summary and confirmation endpoints), no inline path; original row 1176.

**Concern stated in the source:** That would be next step. Need to check w PM regarding where to store, and the query requirement for it. Likely we just need to stamp in productLineAndIntent… and build history projection for any historical query.

I have asked [person] to focus on getting the DTO and main logic done first, so that we unblock FE guys. Persistence can be done afterwards in BE only, since it’s not needed in FE to show existing acks

**Source-preserving request, proposal, or question:**

> That would be next step. Need to check w PM regarding where to store, and the query requirement for it. Likely we just need to stamp in productLineAndIntent… and build history projection for any historical query.
> 
> I have asked [person] to focus on getting the DTO and main logic done first, so that we unblock FE guys. Persistence can be done afterwards in BE only, since it’s not needed in FE to show existing acks

**Conditions and limits:**

- Ack persistence/query model is deferred pending PM; likely productLineAndIntent plus history projection. DTO/main flow first unblocks FE, which need not display prior acks.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1176 · comment 500935158 · PR 9146 · 2024-05-15

> That would be next step. Need to check w PM regarding where to store, and the query requirement for it. Likely we just need to stamp in productLineAndIntent… and build history projection for any historical query.
> 
> I have asked

**Evidence:** anon-2.jsonl:1176 · comment 500935158 · PR 9146 · 2024-05-15

> to focus on getting the DTO and main logic done first, so that we unblock FE guys. Persistence can be done afterwards in BE only, since it’s not needed in FE to show existing acks

**Evidence:** anon-2.jsonl:1176 · comment 500935158 · PR 9146 · 2024-05-15

**Explicit source context (pr_title):**

> feat(advisory): terms agreement ack for add goal flagship dpm simulation summary and confirmation endpoints

## A2-1194 — InvestmentEmailHelper: We don’t need this format right? It’s not serdes anywhere

**Source stance:** suggestion

**Context:**

> PR 9153 (TT-4228 Autofund one time investment and alts investment setup comms), investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/InvestmentEmailHelper.scala; original row 1194.

**Concern stated in the source:** We don’t need this format right? It’s not serdes anywhere

**Source-preserving request, proposal, or question:**

> We don’t need this format right? It’s not serdes anywhere

**Conditions and limits:**

- Format is unnecessary if the internal object is not serialized.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1194 · comment 502298075 · PR 9153 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/InvestmentEmailHelper.scala`

**Evidence:** anon-2.jsonl:1194 · comment 502298075 · PR 9153 · 2024-05-20

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/InvestmentEmailHelper.scala`

**Explicit source context (pr_title):**

> TT-4228 Autofund one time investment and alts investment setup comms

## A2-1202 — HttpServerStartup: Oh we definitely want to set `rejectionHandler` for all services, especially when we extract this to common code. And in order to use a custom rejection handl...

**Source stance:** suggestion

**Context:**

> PR 9049 (DYNAMIC-1046: Terminate service if onMemberUp fails (ready for review)), akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala; original row 1202.

**Concern stated in the source:** Oh we definitely want to set `rejectionHandler` for all services, especially when we extract this to common code. And in order to use a custom rejection handler, we need to use `Route.seal` with implicit `rejectionHandler`

Last time I checked, that was the only way to provide. And this is useful to catch errors before the ServiceLogic is hit, and allow us to handle and return them in usual error json format that other services \+ FE knows how to deserialize.

I took a shortcut and only added for the services we need back then \(some issue in FE sending incorrect payload, and we reject with validation errors not in json, and Davinci doesn’t log full error msg\)

**Source-preserving request, proposal, or question:**

> Oh we definitely want to set `rejectionHandler` for all services, especially when we extract this to common code. And in order to use a custom rejection handler, we need to use `Route.seal` with implicit `rejectionHandler`
> 
> Last time I checked, that was the only way to provide. And this is useful to catch errors before the ServiceLogic is hit, and allow us to handle and return them in usual error json format that other services \+ FE knows how to deserialize.
> 
> I took a shortcut and only added for the services we need back then \(some issue in FE sending incorrect payload, and we reject with validation errors not in json, and Davinci doesn’t log full error msg\)

**Conditions and limits:**

- Route.seal with implicit rejectionHandler is needed to return standard JSON for validation errors rejected before service logic.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1202 · comment 497987974 · PR 9049 · 2024-05-03

Source path: `akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala`

**Evidence:** anon-2.jsonl:1202 · comment 497987974 · PR 9049 · 2024-05-03

Source path: `akka-http-commons/src/main/scala/com/endowus/silver/server/akka/http/HttpServerStartup.scala`

**Explicit source context (pr_title):**

> DYNAMIC-1046: Terminate service if onMemberUp fails (ready for review)

## A2-1248 — TransactionTypes: Same here. Individual transaction should be serdes via the sealed trait `Transaction` by default. You can ref this inside the object so that we ensure it’s onl...

**Source stance:** suggestion

**Context:**

> PR 8998 (TT-4221 add depositDetails in transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala; original row 1248.

**Concern stated in the source:** Same here. Individual transaction should be serdes via the sealed trait `Transaction` by default. You can ref this inside the object so that we ensure it’s only used there

```
object UpdateDepositTransactionCmd {
  implicit private val depositTransaction: Format[DepositTransaction] = DepositTransaction.format
  implicit def format(implicit system: ActorSystem[_]): Format[UpdateDepositTransactionCmd] = Json.format
}
```

‌

**Source-preserving request, proposal, or question:**

> Same here. Individual transaction should be serdes via the sealed trait `Transaction` by default. You can ref this inside the object so that we ensure it’s only used there
> 
> ```
> object UpdateDepositTransactionCmd {
>   implicit private val depositTransaction: Format[DepositTransaction] = DepositTransaction.format
>   implicit def format(implicit system: ActorSystem[_]): Format[UpdateDepositTransactionCmd] = Json.format
> }
> ```
> 
> ‌

**Conditions and limits:**

- Transactions normally serialize through sealed Transaction; DepositTransaction format should be private local implicit inside UpdateDepositTransactionCmd.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1248 · comment 499180515 · PR 8998 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:1248 · comment 499180515 · PR 8998 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Explicit source context (pr_title):**

> TT-4221 add depositDetails in transaction

## A2-1249 — TransactionV3Entity: I think it’s safer to assume we only want to copy over tradeDetails from existing to new value, than to assume we only need to take new statusDetails only f...

**Source stance:** suggestion

**Context:**

> PR 8998 (TT-4221 add depositDetails in transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/TransactionV3Entity.scala; original row 1249.

**Concern stated in the source:** I think it’s safer to assume we only want to copy over tradeDetails from existing to new value, than to assume we only need to take new statusDetails only from new value.  
  
How about we keep this logic just simple as below, no need to think about various status sequences. After all, it’s still an upsert cmd

```
val updatedTransaction = cmd.depositTransaction.copy(
  tradeDetails = cmd.depositTransaction.tradeDetails.orElse(existingTx.tradeDetails)
)
Effect.persist(TransactionUpdatedEvt(updatedTransaction)).thenAck(cmd.replyTo)
```

‌

**Source-preserving request, proposal, or question:**

> I think it’s safer to assume we only want to copy over tradeDetails from existing to new value, than to assume we only need to take new statusDetails only from new value.  
>   
> How about we keep this logic just simple as below, no need to think about various status sequences. After all, it’s still an upsert cmd
> 
> ```
> val updatedTransaction = cmd.depositTransaction.copy(
>   tradeDetails = cmd.depositTransaction.tradeDetails.orElse(existingTx.tradeDetails)
> )
> Effect.persist(TransactionUpdatedEvt(updatedTransaction)).thenAck(cmd.replyTo)
> ```
> 
> ‌

**Conditions and limits:**

- Upsert takes the complete new depositTransaction and only preserves existing tradeDetails when new tradeDetails are absent; avoid reconstructing all fields from status-order assumptions.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1249 · comment 499184615 · PR 8998 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/TransactionV3Entity.scala`

**Evidence:** anon-2.jsonl:1249 · comment 499184615 · PR 8998 · 2024-05-08

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/TransactionV3Entity.scala`

**Explicit source context (pr_title):**

> TT-4221 add depositDetails in transaction

## A2-1310 — D56 abort rejected withdrawal dividend: 187.44 switches to cash balance; 12.56 reinvestment remains unchanged

**Source stance:** reported-verification

**Context:**

> PR 9037 ([INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested), no inline path; original row 1310.

**Source-preserving request, proposal, or question:**

> Tested in d56
> 
> ‌
> 
> Setup dividend \+ rejected withdrawal
> 
> * withdrawal with amount 187.44 is rejected
> * dividend has distribution withdrawal pref, amount = 187.44, stuck in Processing
> * another dividend with same distribution has distribution reinvested pref, amount = 12.56, in Processing \(not affected\)
> 
> ![](<url>
> dividend svc logs error as expected when received `WithdrawalRequestRejectedMsg` from trading svc
> 
> ‌
> 
> Trigger abort endpoint
> 
> Results:
> 
> * withdrawal with amount 187.44 is still rejected \(in tact\)
> * previously stuck dividend now has distribution cash balance pref, amount = 187.44, and is completed
> * the other dividend with same distribution is not affected
> 
> ![](<url>
> timeseries svc processes the new event and update distribution pref correctly
> 
> ‌
> 
> Inspection reports DividendWithdrawalRequestAbortedEvt with overridingDistributionPreference=DistributeCashBalance, and final Distributed state.

**Conditions and limits:**

- Reported D56 test affects only 187.44 withdrawal dividend; 12.56 reinvestment dividend in same distribution is a negative/control case. Incidental entity/account identifiers omitted.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> Tested in d56
> 
> ‌
> 
> Setup dividend \+ rejected withdrawal
> 
> * withdrawal with amount 187.44 is rejected
> * dividend has distribution withdrawal pref, amount = 187.44, stuck in Processing
> * another dividend with same distribution has distribution reinvested pref, amount = 12.56, in Processing \(not affected\)
> 
> ![](<url>
> dividend svc logs error as expected when received `WithdrawalRequestRejectedMsg` from trading svc
> 
> ‌
> 
> Trigger abort endpoint

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> Results:
> 
> * withdrawal with amount 187.44 is still rejected \(in tact\)
> * previously stuck dividend now has distribution cash balance pref, amount = 187.44, and is completed
> * the other dividend with same distribution is not affected
> 
> ![](<url>
> timeseries svc processes the new event and update distribution pref correctly
> 
> ‌

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "eventName": "DividendWithdrawalRequestAbortedEvt"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "overridingDistributionPreference": "DistributeCashBalance"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "distributionPreference": "DistributeCashBalance"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

> "_type": "com.endowus.silver.dividend.impl.entities.dividend.ces.Distributed"

**Evidence:** anon-2.jsonl:1310 · comment 496994504 · PR 9037 · 2024-04-30

**Explicit source context (pr_title):**

> [INV-3016] feat(dividend)(timeseries)(transaction): Support aborting dividend stuck in WithdrawalRequested

## A2-1404 — BaseAdvisoryService: Can you help to change this to `LagomCompatServiceExceptionSerializer` cuz we already migrated Advisory off Lagom

**Source stance:** suggestion

**Context:**

> PR 8792 (Feat/INV-2730/flagship dpm offerring min required amts), advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryService.scala; original row 1404.

**Concern stated in the source:** Can you help to change this to `LagomCompatServiceExceptionSerializer` cuz we already migrated Advisory off Lagom

**Source-preserving request, proposal, or question:**

> Can you help to change this to `LagomCompatServiceExceptionSerializer` cuz we already migrated Advisory off Lagom

**Conditions and limits:**

- Advisory already migrated off Lagom; requested serializer is LagomCompatServiceExceptionSerializer.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1404 · comment 485152367 · PR 8792 · 2024-03-26

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryService.scala`

**Evidence:** anon-2.jsonl:1404 · comment 485152367 · PR 8792 · 2024-03-26

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryService.scala`

**Explicit source context (pr_title):**

> Feat/INV-2730/flagship dpm offerring min required amts

## A2-1496 — PR-description Projections table: FeeChargeRequestJdbcProjection V6

**Source stance:** requested-change

**Context:**

> PR 8796 (PLATFORM-1096: Switch off gcp for Charge svc), no inline path; original row 1496.

**Source-preserving request, proposal, or question:**

> Nit: `FeeChargeRequestJdbcProjection` should be V6 in `Projections` table in PR description

**Conditions and limits:**

- The correction is specifically V6 in the Projections table of the PR description. It is not a request to migrate the implementation, alter a database schema, or claim a new deployment.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1496 · comment 484741806 · PR 8796 · 2024-03-25

**Evidence:** anon-2.jsonl:1496 · comment 484741806 · PR 8796 · 2024-03-25

**Explicit source context (pr_title):**

> PLATFORM-1096: Switch off gcp for Charge svc

## A2-1499 — InitiateCancellationFlowCmdHandler: Alright let’s leave those as is for now. This exception will also hit the serdes issue, but ok we clean in separate PR.

**Source stance:** explanation

**Context:**

> PR 8665 (TT-3981 Do not allow cancelling investment requests that have fxConversionRequestId defined), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala; original row 1499.

**Source-preserving request, proposal, or question:**

> Alright let’s leave those as is for now. This exception will also hit the serdes issue, but ok we clean in separate PR.

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Cancellation exception serialization issue is acknowledged but accepted for separate cleanup, not claimed fixed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1499 · comment 482757887 · PR 8665 · 2024-03-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Evidence:** anon-2.jsonl:1499 · comment 482757887 · PR 8665 · 2024-03-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Explicit source context (hunk):**

> +    existing.fundingInstructions match {
> +      case Some(fundingInstructions: SpecifiedAccountFundingInstructions) if fundingInstructions.fxConversionRequestId.isDefined =>
> +        return Effect.replyError(cmd.replyTo)(
> +          InvestmentSvcException(
> +            s"InvestmentPlanEntity [$entityId] received ${InitiateCancellationFlowCmd.getClass.getSimpleName} but the investment request has " +
> +              s"funding instructions with fxConversionRequestId [${fundingInstructions.fxConversionRequestId.get}], meaning " +
> +              s"that the cash for the FX conversion has already been reserved, and we implicitly assume that the FX conversion " +

**Evidence:** anon-2.jsonl:1499 · comment 482757887 · PR 8665 · 2024-03-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/handlers/InitiateCancellationFlowCmdHandler.scala`

**Explicit source context (pr_title):**

> TT-3981 Do not allow cancelling investment requests that have fxConversionRequestId defined

## A2-1540 — FundSmartInstrument: We shouldn’t need this one, cuz the case class should be serdes without `_type` and we rely on the implicit region to match type right? Same for `FundSmartI...

**Source stance:** suggestion

**Context:**

> PR 8429 (Resolve INV-2639: New endpoints for HK fund smart Instruments.), advisory-api/src/main/scala/com/endowus/silver/advisory/api/models/FundSmartInstrument.scala; original row 1540.

**Concern stated in the source:** We shouldn’t need this one, cuz the case class should be serdes without `_type` and we rely on the implicit region to match type right? Same for `FundSmartInstrumentDetails`

**Source-preserving request, proposal, or question:**

> We shouldn’t need this one, cuz the case class should be serdes without `_type` and we rely on the implicit region to match type right? Same for `FundSmartInstrumentDetails`

**Conditions and limits:**

- Case-class serdes relies on implicit region instead of _type discriminator; individual format may be unnecessary.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1540 · comment 480517780 · PR 8429 · 2024-03-11

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/models/FundSmartInstrument.scala`

**Evidence:** anon-2.jsonl:1540 · comment 480517780 · PR 8429 · 2024-03-11

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/models/FundSmartInstrument.scala`

**Explicit source context (pr_title):**

> Resolve INV-2639: New endpoints for HK fund smart Instruments.

## A2-1556 — SgFundSmartManagerV3: [person] can help check which NotFound that we would catch from performance svc? I remember performance svc doesn’t have service exception, so likely it’s ...

**Source stance:** open-question

**Context:**

> PR 8346 (Resolve INV-2436: Changes to include portfolio performance for illiquid alts.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala; original row 1556.

**Concern stated in the source:** [person] can help check which NotFound that we would catch from performance svc? I remember performance svc doesn’t have service exception, so likely it’s using default error serializer which means we would get Lagom NotFound here?

**Source-preserving request, proposal, or question:**

> [person] can help check which NotFound that we would catch from performance svc? I remember performance svc doesn’t have service exception, so likely it’s using default error serializer which means we would get Lagom NotFound here?

**Conditions and limits:**

- Which NotFound crosses performance-service boundary remains initially uncertain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1556 · comment 475796437 · PR 8346 · 2024-02-26

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

> can help check which NotFound that we would catch from performance svc? I remember performance svc doesn’t have service exception, so likely it’s using default error serializer which means we would get Lagom NotFound here?

**Evidence:** anon-2.jsonl:1556 · comment 475796437 · PR 8346 · 2024-02-26

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/sg/SgFundSmartManagerV3.scala`

**Explicit source context (pr_title):**

> Resolve INV-2436: Changes to include portfolio performance for illiquid alts.

## A2-1561 — PersistentEntityRefProvider: Let’s put a scaladoc for this class, noting down all the entity names that were used in the history

**Source stance:** suggestion

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/PersistentEntityRefProvider.scala; original row 1561.

**Source-preserving request, proposal, or question:**

> Let’s put a scaladoc for this class, noting down all the entity names that were used in the history

**Conditions and limits:**

- Historical entity names must be documented before removing old transaction entities.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1561 · comment 478982324 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/PersistentEntityRefProvider.scala`

**Evidence:** anon-2.jsonl:1561 · comment 478982324 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/PersistentEntityRefProvider.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1586 — TransactionTypes: Please help to mark this as deprecated with msg explaining to use V2 \+ rationale, but still keep it for old event \+ snapshot serdes

**Source stance:** suggestion

**Context:**

> PR 8011 (TT-3566 Make broker account optional for FX transactions), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala; original row 1586.

**Concern stated in the source:** Please help to mark this as deprecated with msg explaining to use V2 \+ rationale, but still keep it for old event \+ snapshot serdes

**Source-preserving request, proposal, or question:**

> Please help to mark this as deprecated with msg explaining to use V2 \+ rationale, but still keep it for old event \+ snapshot serdes

**Conditions and limits:**

- Deprecated V1 model/format must stay for old event and snapshot deserialization; explain V2 replacement/rationale.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1586 · comment 476496928 · PR 8011 · 2024-02-28

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:1586 · comment 476496928 · PR 8011 · 2024-02-28

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Explicit source context (pr_title):**

> TT-3566 Make broker account optional for FX transactions

## A2-1590 — package: As in we should only serdes the individual case class via the trait `FundingInstructionsDto` only. No one should serdes `SpecifiedAccountFundingInstructionsDto` directl...

**Source stance:** suggestion

**Context:**

> PR 7947 (TT-3480 Add funding instructions to investment request), investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala; original row 1590.

**Concern stated in the source:** As in we should only serdes the individual case class via the trait `FundingInstructionsDto` only. No one should serdes `SpecifiedAccountFundingInstructionsDto` directly, hence its formatter should stay private

**Source-preserving request, proposal, or question:**

> As in we should only serdes the individual case class via the trait `FundingInstructionsDto` only. No one should serdes `SpecifiedAccountFundingInstructionsDto` directly, hence its formatter should stay private

**Conditions and limits:**

- Serialize through sealed FundingInstructionsDto only; subtype SpecifiedAccountFundingInstructionsDto formatter remains private.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1590 · comment 477278503 · PR 7947 · 2024-03-01

Source path: `investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala`

**Evidence:** anon-2.jsonl:1590 · comment 477278503 · PR 7947 · 2024-03-01

Source path: `investment-api/src/main/scala/com/endowus/silver/investment/api/models/package.scala`

**Explicit source context (pr_title):**

> TT-3480 Add funding instructions to investment request

## A2-1668 — AdvisoryServiceE4s: Don’t use this one. Locale has special formatter, so we want to use the implicit one in `ParameterSerializersE4s`

**Source stance:** suggestion

**Context:**

> PR 8161 (INV-2486: Add translation logic for fund smart templates.), advisory-api/src/main/scala/com/endowus/silver/advisory/api/AdvisoryServiceE4s.scala; original row 1668.

**Concern stated in the source:** Don’t use this one. Locale has special formatter, so we want to use the implicit one in `ParameterSerializersE4s`

```
  implicit val queryStringParamLocale: QueryStringParam[Locale] =
    stringQueryString.xmapWithCodec(localeUnitCodec)
```

‌

**Source-preserving request, proposal, or question:**

> Don’t use this one. Locale has special formatter, so we want to use the implicit one in `ParameterSerializersE4s`
> 
> ```
>   implicit val queryStringParamLocale: QueryStringParam[Locale] =
>     stringQueryString.xmapWithCodec(localeUnitCodec)
> ```
> 
> ‌

**Conditions and limits:**

- Locale must use ParameterSerializersE4s stringQueryString.xmapWithCodec(localeUnitCodec), not default serializer.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1668 · comment 465169414 · PR 8161 · 2024-01-26

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/AdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:1668 · comment 465169414 · PR 8161 · 2024-01-26

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/AdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> INV-2486: Add translation logic for fund smart templates.

## A2-1692 — common: Still need to remember to add this bit

**Source stance:** explanation

**Context:**

> PR 8053 ([INV-2481] feat(advisory): Move CacheManagementPubSub to silver-commons for reuse), advisory-impl/src/main/resources/common.conf; original row 1692.

**Concern stated in the source:** Still need to remember to add this bit

* `PlayJsonSerializer` is in akka-abstraction-layer so the reference.conf of silver-commons shouldn’t ref it
* and it feels wrong to add the bindings to play-json there without defining the serializers

‌

**Source-preserving request, proposal, or question:**

> Still need to remember to add this bit
> 
> * `PlayJsonSerializer` is in akka-abstraction-layer so the reference.conf of silver-commons shouldn’t ref it
> * and it feels wrong to add the bindings to play-json there without defining the serializers
> 
> ‌

**Conditions and limits:**

- silver-commons reference.conf cannot refer to PlayJsonSerializer located in akka-abstraction-layer, and bindings should not exist without serializer definitions.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1692 · comment 460275724 · PR 8053 · 2024-01-11

Source path: `advisory-impl/src/main/resources/common.conf`

**Evidence:** anon-2.jsonl:1692 · comment 460275724 · PR 8053 · 2024-01-11

Source path: `advisory-impl/src/main/resources/common.conf`

**Explicit source context (pr_title):**

> [INV-2481] feat(advisory): Move CacheManagementPubSub to silver-commons for reuse

## A3-0014 — InstrumentService region serdes: implicit def contract implemented as val for Lagom Service

**Source stance:** explanation

**Context:**

> instrument-api/src/main/scala/com/endowus/silver/instrument/api/BaseInstrumentService.scala; PR: [INV-2214] feat(advisory)(instrument): WIP FundSmart instrument details

**Concern stated in the source:** And it has to be implemented as `val` because Lagom expects all methods in trait `Service` to return either Descriptor or ServiceCall

**Source-preserving request, proposal, or question:**

> V2 instrument DTO requires implicit region to serdes… so now InstrumentService needs `implicit def region: SilverRegion`
> 
> And it has to be implemented as `val` because Lagom expects all methods in trait `Service` to return either Descriptor or ServiceCall
> 
> So I need to split this into InstrumentService and HkInstrumentService like this.
> 
> In theory, this region is local to this trait only. Other services won’t have any issue even if they use \(SG\)InstrumentService in their HK application, but I changed for all anyway.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 1821, 2107, 2108: Read together for Lagom Service val implementation and later regional-data singleton implicit refinements.

**Evidence:** anon-2.jsonl:1821 · comment 441558034 · PR 7385 · 2023-11-03

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/BaseInstrumentService.scala`

**Evidence:** anon-2.jsonl:1821 · comment 441558034 · PR 7385 · 2023-11-03

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/BaseInstrumentService.scala`

**Explicit source context (hunk):**

> +        /**
> +          * internal
> +          */
> +        restCall(Method.GET, "/api/internal/v2/instrument/find-by-id?id", getInternalInstrumentV2 _),
> +        restCall(Method.GET, "/api/internal/v2/instrument/find-by-ids?ids", getInternalInstrumentV2ByIds _),
> +        restCall(Method.GET, "/api/internal/v2/instrument/diy?investorType&currency&maybeFromInstrumentIds", getInternalDiyInstrumentsV2 _),
> +        pathCall("/internal/instruments/page", internalPaginateInstruments),

## A3-0031 — package.scala: `DailyFee` before this PR is not persisted anywhere, so I just make these breaking changes directly to model and DTO

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/commons/package.scala; PR: [INV-2015] feat(charge): Support estimated daily fee

**Source-preserving request, proposal, or question:**

> `DailyFee` before this PR is not persisted anywhere, so I just make these breaking changes directly to model and DTO

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1841 · comment 438135774 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/commons/package.scala`

**Evidence:** anon-2.jsonl:1841 · comment 438135774 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/commons/package.scala`

**Explicit source context (hunk):**

> +    annualFeeRatio: BigDecimal,
>      dailyFee: BigDecimal,
> -    updatedAt: Option[ZonedDateTime] = None
> +    updatedAt: Instant
>    )
>  
>    object DailyFee {

## A3-0067 — InstrumentCommands.scala: Don’t we need format for this?

**Source stance:** open-question

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommands.scala; PR: Resolve INV-2049: New instrument events, event handlers, v2 logic split.

**Source-preserving request, proposal, or question:**

> Don’t we need format for this?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1883 · comment 437273722 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommands.scala`

**Evidence:** anon-2.jsonl:1883 · comment 437273722 · PR 7097 · 2023-10-19

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentCommands.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  case class UpdateInstrumentIdCmd(
> +    idMap: Map[InstrumentIdType, String],
> +    updatedBy: String,
> +    updatedAt: ZonedDateTime,
> +    replyTo: ActorRef[StatusReply[InstrumentReply]]

## A3-0083 — TransactionV2AccountSerializerRegistry.scala: Don’t var if you can

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala; PR: Feat/INV-2152 hk v2 v3 migration processor

**Source-preserving request, proposal, or question:**

> Don’t var if you can

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1900 · comment 438075484 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Evidence:** anon-2.jsonl:1900 · comment 438075484 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Explicit source context (hunk):**

> +object TransactionMigratorHelper {
> +
> +  def fixCancelledStatusDetails(transactionJson: JsObject): JsObject = {
> +    val txnJson = transactionJson
> +    val innerTransactionJson = (txnJson \ "transaction").as[JsObject]
> +    val statusDetails = (transactionJson \ "transaction" \ "statusDetails").as[JsObject]
> +

## A3-0084 — TransactionV2AccountSerializerRegistry.scala: you have to update the field using \+\+ but still you don’t need to reassign to existing val?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala; PR: Feat/INV-2152 hk v2 v3 migration processor

**Source-preserving request, proposal, or question:**

> Yes you have to update the field using \+\+ but still you don’t need to reassign to existing val?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1901 · comment 438079279 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Evidence:** anon-2.jsonl:1901 · comment 438079279 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Explicit source context (hunk):**

> +object TransactionMigratorHelper {
> +
> +  def fixCancelledStatusDetails(transactionJson: JsObject): JsObject = {
> +    val txnJson = transactionJson
> +    val innerTransactionJson = (txnJson \ "transaction").as[JsObject]
> +    val statusDetails = (transactionJson \ "transaction" \ "statusDetails").as[JsObject]
> +

## A3-0085 — common.conf: And why don’t we need for prod? Cuz you think prod doesn’t these cancelled events?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/resources/common.conf; PR: Feat/INV-2152 hk v2 v3 migration processor

**Concern stated in the source:** Cuz you think prod doesn’t these cancelled events?

**Source-preserving request, proposal, or question:**

> And why don’t we need for prod? Cuz you think prod doesn’t these cancelled events?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1902 · comment 438080113 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/resources/common.conf`

**Evidence:** anon-2.jsonl:1902 · comment 438080113 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/resources/common.conf`

**Explicit source context (hunk):**

> "com.endowus.silver.transaction.impl.entities.CustomerTransactionManagerStateMigrator"
> +
> +        #HK V2 Migrations
> +        "com.endowus.silver.transaction.impl.entities.transaction.ces.events.package$TransactionUpdatedEvt" =
> +          "com.endowus.silver.transaction.impl.entities.transaction.TransactionV2UpdatedEvtMigrator"
>        }
>      }

## A3-0086 — TransactionV2AccountSerializerRegistry.scala: I suppose we don’t migrate state because we only need events to move to V3?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala; PR: Feat/INV-2152 hk v2 v3 migration processor

**Concern stated in the source:** I suppose we don’t migrate state because we only need events to move to V3?

**Source-preserving request, proposal, or question:**

> I suppose we don’t migrate state because we only need events to move to V3?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1903 · comment 438080163 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Evidence:** anon-2.jsonl:1903 · comment 438080163 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transaction/TransactionV2AccountSerializerRegistry.scala`

**Explicit source context (hunk):**

> +    classOf[TransactionUpdatedEvt].getName -> TransactionV2UpdatedEvtMigration1
> +}
> +
> +class TransactionV2UpdatedEvtMigrator
> +  extends JsonMigrationCapture2(TransactionV2AccountSerializerRegistry.TransactionV2UpdatedEvtMigration)
> +

## A3-0087 — common.conf: V2 will be thrown away soon, let’s just keep parity to avoid confusion

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/resources/common.conf; PR: Feat/INV-2152 hk v2 v3 migration processor

**Source-preserving request, proposal, or question:**

> V2 will be thrown away soon, let’s just keep parity to avoid confusion

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1904 · comment 438080626 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/resources/common.conf`

**Evidence:** anon-2.jsonl:1904 · comment 438080626 · PR 7261 · 2023-10-23

Source path: `transaction-impl/src/main/resources/common.conf`

**Explicit source context (hunk):**

> "com.endowus.silver.transaction.impl.entities.CustomerTransactionManagerStateMigrator"
> +
> +        #HK V2 Migrations
> +        "com.endowus.silver.transaction.impl.entities.transaction.ces.events.package$TransactionUpdatedEvt" =
> +          "com.endowus.silver.transaction.impl.entities.transaction.TransactionV2UpdatedEvtMigrator"
>        }
>      }

## A3-0101 — package.scala: Sorry I forgot… this is V1 entity, only used in SG - we’re good here

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/package.scala; PR: [INV-1141] Fix transaction L1 dates for v2

**Source-preserving request, proposal, or question:**

> Sorry I forgot… this is V1 entity, only used in SG - we’re good here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1918 · comment 434757607 · PR 7114 · 2023-10-11

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/package.scala`

**Evidence:** anon-2.jsonl:1918 · comment 434757607 · PR 7114 · 2023-10-11

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/package.scala`

**Explicit source context (hunk):**

> tradingAccountType = d.tradingAccountType,
>          transactionId = d.transactionId,
> -        statusUpdatedDate = d.lastUpdatedDate.atStartOfDay().toInstant(ZoneOffset.UTC),
> +        statusUpdatedDate = d.lastUpdatedDate.atStartOfDay(ZoneId.of("Asia/Singapore")).toInstant,
>          ccy = d.ccy,
>          transactionType = d.transactionType,
>          status = d.status,

## A3-0160 — package.scala: I guess this is ok - we should ideally already move read ops to v2 before we start using these v2-only features

**Source stance:** explanation

**Context:**

> instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/converter/package.scala; PR: Resolve INV-1797: Instrument entity v2 initial work

**Source-preserving request, proposal, or question:**

> I guess this is ok - we should ideally already move read ops to v2 before we start using these v2-only features

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1979 · comment 422626247 · PR 6760 · 2023-08-28

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/converter/package.scala`

**Evidence:** anon-2.jsonl:1979 · comment 422626247 · PR 6760 · 2023-08-28

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/converter/package.scala`

**Explicit source context (hunk):**

> +
> +  def getComplexDetails(instrument: InstrumentInfoDtoV2)(implicit region: SilverRegion): Option[Boolean] = {
> +    matchAll(
> +      sg = _ => None,
> +      hk = implicit region => Some(instrument.regionSpecificDetails.regional.isComplex)
> +    )
> +  }

## A3-0173 — enums.scala: These enums, should they be in instrument-api or commons? I don’t think other services would need to persist these? If other services just need to acc

**Source stance:** open-question

**Context:**

> silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala; PR: Resolve INV-1797: Instrument entity v2 initial work

**Source-preserving request, proposal, or question:**

> These enums, should they be in instrument-api or commons? I don’t think other services would need to persist these? If other services just need to access these enums, they can import instrument-api?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1992 · comment 430320399 · PR 6760 · 2023-09-25

Source path: `silver-commons/src/main/scala/com/endowus/silver/commons/models/enums.scala`

## A3-0181 — ServiceLogicImpl.scala: Just keep v1 as is, and name this v2?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> Just keep v1 as is, and name this v2?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2001 · comment 426630785 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2001 · comment 426630785 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +    val rebalanceSvc: RebalanceService,
> +    val marketDataService: MarketDataService,
> +    val fxConverter: TransactionFxConverter,
> +    val transactionJdbcRepository: TransactionJdbcRepository,
> +    val transactionJdbcRepositoryV2: TransactionJdbcRepositoryV2,
> +    val fxRatesProjectionJdbcDbHandler: FxRatesProjectionJdbcDbHandler,
> +    val supportedCurrencies: SupportedCurrencies,

## A3-0182 — ServiceLogicImpl.scala: Assuming this is just a way to validate data, not actual migration, can we move this if check out to `TransactionServiceImpl` instead? ``` def queryTr

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> Assuming this is just a way to validate data, not actual migration, can we move this if check out to `TransactionServiceImpl` instead?
> 
> ```
> def queryTransactions(...) {
>   if (isV2Query) {
>     logic.queryCustomerTransactions(...)
>   } else {
>     logic.queryTransactions(...)
>   }
> }
> ```
> 
>   
> This way we don’t need to touch v1 code, and it’s also clear that we copy paste the method content `queryCustomerTransactions` from `TransactionQueryLogic`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2002 · comment 426642036 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala`

> Assuming this is just a way to validate data, not actual migration, can we move this if check out to `TransactionServiceImpl` instead?
> 
> ```
> def queryTransactions(...) {
>   if (isV2Query) {
>     logic.queryCustomerTransactions(...)
>   } else {
>     logic.queryTransactions(...)
>   }
> }
> ```
> 
>   
> This way we don’t need to touch v1 code, and it’s also clear that we copy paste the method content `queryCustomerTransactions` from `TransactionQueryLogic`
> 
> ‌

## A3-0183 — CustomerTransactionMigrationEventProcessor.scala: Hmm I guess it’s ok, but we will lose the requestedBy and reason in these events

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> Hmm I guess it’s ok, but we will lose the requestedBy and reason in these events

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2003 · comment 426642760 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

**Evidence:** anon-2.jsonl:2003 · comment 426642760 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

**Explicit source context (hunk):**

> +        .map(_.transaction)
> +      transactionV2 <- convertTransaction(transaction, eventTimestamp)
> +      res <- refProvider.getTransactionEntityRef(transaction.transactionId)
> +        .ask(ForceOverrideTransactionCmd(
> +          _,
> +          transaction = transactionV2,
> +          expectedExistingTransaction = existingTransaction,

## A3-0192 — InvestmentTransactionV2Transformer.scala: patch will blindly copy and toV2Order will set status according to assumedAt/confirmedAt… so we will have assumed order here even if it’s still pendin

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/InvestmentTransactionV2Transformer.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> patch will blindly copy and toV2Order will set status according to assumedAt/confirmedAt… so we will have assumed order here even if it’s still pending status?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2012 · comment 426649156 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/InvestmentTransactionV2Transformer.scala`

**Evidence:** anon-2.jsonl:2012 · comment 426649156 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/InvestmentTransactionV2Transformer.scala`

**Explicit source context (hunk):**

> +          shouldFallbackOn = {
> +            case _: NotFound => true
> +            case _ => false
> +          },
> +          futFallback = for {
> +            planInvestments <- investmentService.findInvestmentRequestsForPlan(transaction.planId.get).invoke()
> +            investmentData = planInvestments.find(_.investmentRequestId == transaction.transactionId).getOrElse(

## A3-0193 — No-order rebalance migration: v1 sell/buy sums versus v2 buy-confirmed/sell fallback

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/RebalanceTransactionV2Transformer.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> When we do we have these cases? Is it staging only, or also prod?
> 
> I think we won’t have data if the rebalance is created on rebalance svc, but then got completed without actual sell/buy, e.g. accepted RPC on an empty plan
> 
> v1 enforces requestedAmount = sum of sell orders' order amount, and confirmedAmount = sum of buy orders' confirmed amount
> 
> but v2 has logic change to use buy confirmed amount, if it’s 0 then fallback to sell confirmed amount

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve v1 requested/sell and confirmed/buy amounts separately from v2 buy-confirmed with sell-confirmed fallback at zero.

**Evidence:** anon-2.jsonl:2013 · comment 426654498 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/RebalanceTransactionV2Transformer.scala`

**Evidence:** anon-2.jsonl:2013 · comment 426654498 · PR 6863 · 2023-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/transformers/RebalanceTransactionV2Transformer.scala`

**Explicit source context (hunk):**

> +        requestedAt = eventTimestamp, //in v2 it's rebalanceRequest.lastStatusChangeAt, event should suffice since this is intermediate state and will follow trade changes
> +        orders = transaction.orders.map(toV2Order)
> +      )
> +      case SETTLEMENT_CONFIRMED => ConfirmedOrdersStatusDetails(
> +        transactionStatus = transaction.status,
> +        confirmedAmount = transaction.settledAmount.getOrElse(
> +          calculateBuyOrdersConfirmedAmountSum(transaction.orders)

## A3-0204 — DTO/domain defaults discouraged except massive legacy-v1-transaction call-site changes

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/package.scala; PR: Feat/INV-1972 transaction migrator processor

**Concern stated in the source:** Essentially we should not default in DTO and domain model, unless it cause massive amount of changes, e.g.

**Source-preserving request, proposal, or question:**

> No default here too. Essentially we should not default in DTO and domain model, unless it cause massive amount of changes, e.g. v1 transaction

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Exception explicitly allows defaults when removing them causes massive changes, with v1 transaction as example.

**Evidence:** anon-2.jsonl:2025 · comment 427290738 · PR 6863 · 2023-09-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/package.scala`

**Evidence:** anon-2.jsonl:2025 · comment 427290738 · PR 6863 · 2023-09-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/package.scala`

**Explicit source context (hunk):**

> feeChargeRequestId: UUID,
>      startAuaDate: LocalDate,
>      endAuaDate: LocalDate,
> +    //Added since GST, will be mandatory, but kept optional with default for backward serdes
> +    reason: Option[PlanFeeChargeReason],
>      requestedAt: Option[ZonedDateTime] = None,

## A3-0206 — CustomerTransactionMigrationEventProcessor.scala: Yea this one is purely just to capture the requestedBy/reason - which helps to explain these manual override if we have to dig in future. If we don’t 

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala; PR: Feat/INV-1972 transaction migrator processor

**Source-preserving request, proposal, or question:**

> Yea this one is purely just to capture the requestedBy/reason - which helps to explain these manual override if we have to dig in future.
> 
> If we don’t want to look up entity, we can always add a command to override without state \(or make it optional in current cmd\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2027 · comment 428086048 · PR 6863 · 2023-09-18

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

**Evidence:** anon-2.jsonl:2027 · comment 428086048 · PR 6863 · 2023-09-18

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/customer/processors/CustomerTransactionMigrationEventProcessor.scala`

**Explicit source context (hunk):**

> +        .map(_.transaction)
> +      transactionV2 <- convertTransaction(transaction, eventTimestamp)
> +      res <- refProvider.getTransactionEntityRef(transaction.transactionId)
> +        .ask(ForceOverrideTransactionCmd(
> +          _,
> +          transaction = transactionV2,
> +          expectedExistingTransaction = existingTransaction,

## A3-0256 — Schedule history without key duplicates on event retry

**Source stance:** observed-defect

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Concern stated in the source:** exception and retry\), we will insert multiple duplicate entries

**Source-preserving request, proposal, or question:**

> This history table doesn’t have key… if for whatever reason the event is replayed \(e.g. exception and retry\), we will insert multiple duplicate entries

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Related source rows 2080, 2086, 2089: History PK opinion evolves from broad composite suggestion to duplicate-tolerance or fakeUUID PK; do not flatten to mandatory wide composite key.

**Evidence:** anon-2.jsonl:2080 · comment 422183334 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

## A3-0265 — UpdatedEvt old/new inserts and offset-commit failures: duplicate windows and PK alternatives

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Concern stated in the source:** Even with separate processors, the chance of duplicated rows is still there because we perform 2 inserts for UpdatedEvt \(but yes, splitting the processors reduce this chance much further\)

Even for event with single insert, duplicates can happen if insert succeeds and offset commit fails.

If data side is able to handle the \(rare\) duplicates, I’d say we stick with no pk.

However, if data side insists we cannot have duplicates, then as  suggested, generate a fake UUID based on the fields, and use it as pk.

Let’s not add a composite key so many fields, as under the hood, pg would create index for them too - which is useless because we are not querying this table at all from application side?

**Source-preserving request, proposal, or question:**

> Even with separate processors, the chance of duplicated rows is still there because we perform 2 inserts for UpdatedEvt \(but yes, splitting the processors reduce this chance much further\)
> 
> Within the history processor itself, this can still happen for UpdatedEvt if:
> 
> * insert old succeeds, but insert new fails → retry for the event, which will insert old again
> * insert old succeeds, insert new also succeeds, but offset commit fails → retry for the event, which will insert both again
> 
> Even for event with single insert, duplicates can happen if insert succeeds and offset commit fails.
> 
> 
> 
> If data side is able to handle the \(rare\) duplicates, I’d say we stick with no pk. I’m skeptical with the amount of fields in this composite key too.
> 
> However, if data side insists we cannot have duplicates, then as  suggested, generate a fake UUID based on the fields, and use it as pk. Let’s not add a composite key so many fields, as under the hood, pg would create index for them too - which is useless because we are not querying this table at all from application side?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Retain all insert/offset-commit windows, tolerated-duplicate branch versus deterministic fake UUID PK alternative, and objection to wide composite index.
- Related source rows 2080, 2086, 2089: History PK opinion evolves from broad composite suggestion to duplicate-tolerance or fakeUUID PK; do not flatten to mandatory wide composite key.

**Evidence:** anon-2.jsonl:2089 · comment 422620412 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

> Even with separate processors, the chance of duplicated rows is still there because we perform 2 inserts for UpdatedEvt \(but yes, splitting the processors reduce this chance much further\)
> 
> Within the history processor itself, this can still happen for UpdatedEvt if:
> 
> * insert old succeeds, but insert new fails → retry for the event, which will insert old again
> * insert old succeeds, insert new also succeeds, but offset commit fails → retry for the event, which will insert both again
> 
> Even for event with single insert, duplicates can happen if insert succeeds and offset commit fails.
> 
> ‌
> 
> If data side is able to handle the \(rare\) duplicates, I’d say we stick with no pk. I’m skeptical with the amount of fields in this composite key too.
> 
> However, if data side insists we cannot have duplicates, then as

**Evidence:** anon-2.jsonl:2089 · comment 422620412 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

> suggested, generate a fake UUID based on the fields, and use it as pk. Let’s not add a composite key so many fields, as under the hood, pg would create index for them too - which is useless because we are not querying this table at all from application side?
> 
> ‌

## A3-0284 — JdbcSchema.scala: Create V4?

**Source stance:** open-question

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/db/JdbcSchema.scala; PR: InvestmentPlanTableV4

**Source-preserving request, proposal, or question:**

> Create V4?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2109 · comment 420917948 · PR 6639 · 2023-08-21

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/db/JdbcSchema.scala`

**Evidence:** anon-2.jsonl:2109 · comment 420917948 · PR 6639 · 2023-08-21

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/db/JdbcSchema.scala`

**Explicit source context (hunk):**

> -        _ <- createTableIfNotExists(TableQuery[InvestmentPlanTable])
>          _ <- createTableIfNotExists(TableQuery[InvestmentRequestTable])
>          _ <- createTableIfNotExists(TableQuery[InvestmentPlanTableV3])
> +        _ <- createTableIfNotExists(TableQuery[InvestmentPlanTableV4])
>          _ <- createTableIfNotExists(TableQuery[InvestmentScheduleActivePeriodTable])
>        } yield ()
>      }

## A3-0308 — PlanCommunicationV2EventProcessor.scala: Use createdAt if exist?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-1990] Email/PlatformNotification for recurring setup, modify, stop

**Source-preserving request, proposal, or question:**

> Use createdAt if exist?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2133 · comment 420900464 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2133 · comment 420900464 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +        planId = plan.planId,
> +        recurringInvestmentScheduleFromEvent = recurringOpt.get,
> +        eventTimestamp = plan.createdAt
> +      )
> +    }
> +  }
> +

## A3-0309 — PlanCommunicationV2EventProcessor.scala: Fallback to event timestamp instead of now?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-1990] Email/PlatformNotification for recurring setup, modify, stop

**Source-preserving request, proposal, or question:**

> Fallback to event timestamp instead of now?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2134 · comment 420900518 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2134 · comment 420900518 · PR 6686 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +        goalId = event.goalId,
> +        planId = event.planId,
> +        recurringInvestmentScheduleFromEvent = event.updatedSchedule,
> +        eventTimestamp = updatedAt
> +      )
> +    } else {
> +      sendRecurringInvestmentScheduleModifiedNotification(event)

## A3-0313 — Old replayed events missing createdAt should use event timestamp to avoid fresh communication

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-1990] Email/PlatformNotification for recurring setup, modify, stop

**Source-preserving request, proposal, or question:**

> Do we still have any flow that set `createdAt` = None? Maybe let’s fallback to event timestamp if not set?
> 
> If we ever replay old events that does not have `createdAt`, we wouldn’t want to send out those communication right?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2138 · comment 421230791 · PR 6686 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2138 · comment 421230791 · PR 6686 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +    ele: EventEnvelope[PlanCreatedEvt]
> +  ): Future[Done] = {
> +    val plan = ele.event.plan
> +    val recurringOpt = plan.recurringInvestmentSchedule
> +    if (recurringOpt.isEmpty || plan.createdAt.isBefore(dateTimeProvider.now.minusDays(2))) {
> +      Future.successful(Done)
> +    } else {

## A3-0314 — PlanCommunicationV2EventProcessor.scala: Same here, let’s also fallback to event timestamp

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: [EN-1990] Email/PlatformNotification for recurring setup, modify, stop

**Source-preserving request, proposal, or question:**

> Same here, let’s also fallback to event timestamp

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2139 · comment 421231428 · PR 6686 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2139 · comment 421231428 · PR 6686 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +  def planRecurringInvestmentScheduleUpdatedEvtHandler(
> +    ele: EventEnvelope[PlanRecurringInvestmentScheduleUpdatedEvt]
> +  ): Future[Done] = {
> +    val event = ele.event
> +    val updatedAt = event.updatedAt.getOrElse(EventEnvelopeUtils.extractEventTimestamp(ele).atZone(dateTimeProvider.zoneId))
> +    if (updatedAt.isBefore(dateTimeProvider.now.minusDays(2))) {
> +      Future.successful(Done)

## A3-0316 — RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala: Can we just use data from event itself?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala; PR: [EN-1361] Create read side history table for Recurring investment schedule

**Source-preserving request, proposal, or question:**

> Can we just use data from event itself?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2141 · comment 420917234 · PR 6668 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2141 · comment 420917234 · PR 6668 · 2023-08-21

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +        customerId = event.customerId,
> +        tradingAccountType = event.tradingAccountType,
> +        schedule = Some(event.updatedSchedule)
> +      )
> +    } yield ()
> +  }
> +

## A3-0318 — PlanRecurringInvestmentScheduleHistory.scala: It’s a little weird to see this one Optional, but I guess it’s ok cuz even in events it’s optional. The more important field would be updatedAt

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleHistory.scala; PR: [EN-1361] Create read side history table for Recurring investment schedule

**Concern stated in the source:** It’s a little weird to see this one Optional, but I guess it’s ok cuz even in events it’s optional.

**Source-preserving request, proposal, or question:**

> It’s a little weird to see this one Optional, but I guess it’s ok cuz even in events it’s optional. The more important field would be updatedAt

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2143 · comment 421206769 · PR 6668 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleHistory.scala`

**Evidence:** anon-2.jsonl:2143 · comment 421206769 · PR 6668 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleHistory.scala`

**Explicit source context (hunk):**

> +  interval: CashflowInterval,
> +  startingFrom: LocalDate,
> +  investmentAmount: BigDecimal,
> +  createdAt: Option[LocalDate],
> +  recurrenceEndDetails: Option[RecurrenceEndDetails],
> +  isCancelled: Boolean,
> +  isStopped: Boolean,

## A3-0344 — Upstream optional fee fields remain optional for V1-to-V2 migration

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriberV2.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Source-preserving request, proposal, or question:**

> Ok if upstream data \(redemption / withdrawal\) is optional, then we must keep these as Optional, even though we know it’s always available in charge.
> 
> We need to make sure we can migrate existing v1 model to v2 model via event processor.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2169 · comment 419070780 · PR 6671 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2169 · comment 419070780 · PR 6671 · 2023-08-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +
>  }
>  
>  object WithdrawalTopicSubscriberV2 {
> +  def buildFeeWithdrawalTransaction(
> +    customerId: UUID,
> +    tradingAccountType: TradingAccountType,

## A3-0345 — TransactionTypes.scala: Can we remove all these defaults? Let’s make it a habit to not use default unless for legit reason, e.g. if we add new fields in the v1 transaction th

**Source stance:** requested-change

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1864] feat(transaction): v2 charge transaction

**Concern stated in the source:** if we add new fields in the v1 transaction then I don’t mind, cuz I know there are a million places to update… but new code/new flow, let’s avoid

**Source-preserving request, proposal, or question:**

> Can we remove all these defaults? Let’s make it a habit to not use default unless for legit reason, e.g. if we add new fields in the v1 transaction then I don’t mind, cuz I know there are a million places to update… but new code/new flow, let’s avoid

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Preserve explicit exception for legacy v1 transaction changes with many callers; new code/flow should avoid defaults per this comment.

**Evidence:** anon-2.jsonl:2170 · comment 419356433 · PR 6671 · 2023-08-15

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

## A3-0365 — Requested-state submission statuses: remove unused external, preserve existing internal if prod data

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala; PR: Feat/INV-1866 rebate v2 model

**Concern stated in the source:** Ideally I would want to remove submitted-internally status from this state as well, cuz it should already be pending status.

**Source-preserving request, proposal, or question:**

> WDYT about removing this submitted-externally status in Requested state?
> 
> Ideally I would want to remove submitted-internally status from this state as well, cuz it should already be pending status.
> 
> Looking at usage, looks like:
> 
> * no flow is using submitted-externally status here yet, should be safe to remove
> * `WithdrawalRequestAcceptedMsg` is using submitted-internally status in Requested state
> 
>     * I suppose we should have put it as Pending state
>     * Can we check in prod if we have withdrawal txn yet? If yes \(likely\), then I guess too late, and we can keep submitted-internally here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- External-submission status appears unused; internal-submission removal depends on checking production withdrawal transactions, with compatibility retention if present.

**Evidence:** anon-2.jsonl:2191 · comment 419362224 · PR 6687 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

> WDYT about removing this submitted-externally status in Requested state?
> 
> Ideally I would want to remove submitted-internally status from this state as well, cuz it should already be pending status.
> 
> Looking at usage, looks like:
> 
> * no flow is using submitted-externally status here yet, should be safe to remove
> * `WithdrawalRequestAcceptedMsg` is using submitted-internally status in Requested state
> 
>     * I suppose we should have put it as Pending state
>     * Can we check in prod if we have withdrawal txn yet? If yes \(likely\), then I guess too late, and we can keep submitted-internally here
>     
> 
> ‌

**Evidence:** anon-2.jsonl:2191 · comment 419362224 · PR 6687 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Explicit source context (hunk):**

> val ApplicableTransactionStatuses: Set[common.TransactionStatus.Value] = Set(
>        TransactionStatus.CREATED_AND_PENDING_INTERNAL_BROKER_SUBMISSION,
>        TransactionStatus.SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION,
> -      TransactionStatus.SUBMITTED_EXTERNALLY_AND_PENDING_SETTLEMENT,
>        TransactionStatus.PROCESSING
>      )

## A3-0366 — RebateDistributionTopicSubscriberV2.scala: If we are keeping submitted-internally in Requested state, then I suppose we can let this one be in Requested state :pray:

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala; PR: Feat/INV-1866 rebate v2 model

**Source-preserving request, proposal, or question:**

> If we are keeping submitted-internally in Requested state, then I suppose we can let this one be in Requested state :pray:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2192 · comment 419362475 · PR 6687 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2192 · comment 419362475 · PR 6687 · 2023-08-15

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/RebateDistributionTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +    case msg: RebateDistributionRequestCreatedMsg if msg.distributedRebateAmount > 0 =>
> +      logger.info(s"Received message that rebate distribution request was created. Plan Id: ${msg.planId}, Rebate request ID: ${msg.rebateRequestId}")
> +      val statusDetails = RequestedAmountStatusDetails(
> +        transactionStatus = TransactionStatus.SUBMITTED_INTERNALLY_AND_PENDING_EXTERNAL_BROKER_SUBMISSION,
> +        requestedAmount = msg.distributedRebateAmount,
> +        requestedAt = msg.createdAt
> +      )

## A3-0388 — New updatedAt missing on old events: ele.timestamp rather than replay-now

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> updatedAt was a new field added, so old events would not have this field, so defaulting to current timestamp would mess up your data here.
> 
> Can you check if we fallback to use `ele.timestamp` instead?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2215 · comment 416497592 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2215 · comment 416497592 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +        )
> +      )
> +      .setFutureEventHandler[InvestmentPlanCreatedEvt](
> +        ele => createSchedule(UUID.fromString(ele.entityId), ele.event.investmentPlan)
> +      )
> +      .setFutureEventHandler[RecurringInvestmentScheduleRemovedEvt](
> +        ele => removeSchedule(UUID.fromString(ele.entityId), ele.event.removedAt)

## A3-0400 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Use `event.updatedAt` if available

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Use `event.updatedAt` if available

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2227 · comment 416513206 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2227 · comment 416513206 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +            UUID.fromString(ele.entityId),
> +            ele.event.updatedSchedule,
> +            ele.event.updatedAt.getOrElse(ZonedDateTime.ofInstant(Instant.ofEpochMilli(ele.timestamp), dateTimeProvider.zoneId))
> +        )
> +      )
> +      .setFutureEventHandler[InvestmentPlanCreatedEvt](
> +        ele => createSchedule(UUID.fromString(ele.entityId), ele.event.investmentPlan)

## A3-0428 — package.scala: I think it’s cleaner to create new cmd, mark old one deprecated. Once we switch the usage completely, it’s simple to remove the old cmd whenever we to

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/ces/commands/package.scala; PR: Feat/INV-1600/productline cash smart goal create and modify

**Source-preserving request, proposal, or question:**

> Yeah I think it’s cleaner to create new cmd, mark old one deprecated. Once we switch the usage completely, it’s simple to remove the old cmd whenever we touch the service again.
> 
> Chance of running into ’s example is low, but not non-zero. Once we hit that case, it might be troublesome to deal with, especially for FundSmart

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- New cmd+deprecation proposal preserves low-probability but nonzero FundSmart compatibility risk, not universal mandatory command versioning.

**Evidence:** anon-2.jsonl:2258 · comment 405844795 · PR 6115 · 2023-06-23

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/ces/commands/package.scala`

> Yeah I think it’s cleaner to create new cmd, mark old one deprecated. Once we switch the usage completely, it’s simple to remove the old cmd whenever we touch the service again.
> 
> Chance of running into

**Evidence:** anon-2.jsonl:2258 · comment 405844795 · PR 6115 · 2023-06-23

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/ces/commands/package.scala`

> ’s example is low, but not non-zero. Once we hit that case, it might be troublesome to deal with, especially for FundSmart

## A3-0439 — ThresholdBreachTable.scala: Alright it was there in the Cassandra table too. I guess we can leave it for now.

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/ThresholdBreachTable.scala; PR: Feat/INV-1663 migrate to readside rebalance

**Source-preserving request, proposal, or question:**

> Alright it was there in the Cassandra table too. I guess we can leave it for now.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2269 · comment 412995762 · PR 6482 · 2023-07-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/ThresholdBreachTable.scala`

**Evidence:** anon-2.jsonl:2269 · comment 412995762 · PR 6482 · 2023-07-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/ThresholdBreachTable.scala`

**Explicit source context (hunk):**

> +  def planCcy = column[CurrencyUnit]("planCcy")
> +  def rebalanceRequestId = column[UUID]("rebalance_request_id")
> +  def createdAt = column[ZonedDateTime]("created_at")
> +  def createdDate = column[LocalDate]("created_date")
> +  def breachedInstruments = column[List[InstrumentThresholdCheckResultDto]]("breached_instruments")
> +  def pk = primaryKey(ThresholdBreachTable.pkName, rebalanceRequestId)
> +  override def * : ProvenShape[ThresholdBreachedDto] =

## A3-0450 — PlanTraderEntityTestForSellFeeCharge.scala: No events mean state will not change right?

**Source stance:** open-question

**Context:**

> trading-impl/src/test/scala/com/endowus/silver/trading/imp/entities/plan/PlanTraderEntityTestForSellFeeCharge.scala; PR: [INV-1719] feat(charge)(trading): Fee charge leakage

**Source-preserving request, proposal, or question:**

> No events mean state will not change right?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2283 · comment 412646982 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/test/scala/com/endowus/silver/trading/imp/entities/plan/PlanTraderEntityTestForSellFeeCharge.scala`

**Evidence:** anon-2.jsonl:2283 · comment 412646982 · PR 6463 · 2023-07-19

Source path: `trading-impl/src/test/scala/com/endowus/silver/trading/imp/entities/plan/PlanTraderEntityTestForSellFeeCharge.scala`

**Explicit source context (hunk):**

> outcome3.reply shouldBe Ack
> -        outcome3.events should have size 1
> -        outcome3.events.head shouldBe an[TradeSettlementConfirmedEvt]
> +        outcome3.events shouldBe empty
> +        outcome3.state.trades.find(_.tradeId == requestSellCmd.stub.tradeId).map(_.status) should contain(TradeStatus.WAITING_FOR_MARKET_DATA)
> +    }

## A3-0472 — package.scala: If we are splitting to 2 optional fields for oneTime vs recurring, then it doesn’t make sense to have `RecurringInvestmentRequest` extending `Investme

**Source stance:** suggestion

**Context:**

> advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/invest/package.scala; PR: [EN-1787][More recurring Schedules] DTO and model changes

**Source-preserving request, proposal, or question:**

> If we are splitting to 2 optional fields for oneTime vs recurring, then it doesn’t make sense to have `RecurringInvestmentRequest` extending `InvestmentRequest` right? Once all migrated, we can drop the sealed trait and just have `OneTimeInvestmentRequest` and `RecurringInvestmentRequest` independenly

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2305 · comment 412689335 · PR 6422 · 2023-07-19

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/invest/package.scala`

**Evidence:** anon-2.jsonl:2305 · comment 412689335 · PR 6422 · 2023-07-19

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/invest/package.scala`

**Explicit source context (hunk):**

> +    day: Int,
> +    interval: CashflowInterval,
> +    recurrenceRangeConfig: RecurrenceRangeConfigDto
> +  ) {
> +    require(
> +      ((interval == CashflowInterval.WEEKLY || interval == CashflowInterval.BIWEEKLY) && (day >= 1 && day <= 5)) ||
> +        (interval == CashflowInterval.MONTHLY && (day >= 1 && day <= 28)),

## A3-0474 — package.scala: Since there is a migration, can we change caller to pass `customerAcknowledgements` properly so we don’t need this default anymore?

**Source stance:** open-question

**Context:**

> goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala; PR: [EN-1787][More recurring Schedules] DTO and model changes

**Source-preserving request, proposal, or question:**

> Since there is a migration, can we change caller to pass `customerAcknowledgements` properly so we don’t need this default anymore?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2307 · comment 412692361 · PR 6422 · 2023-07-19

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala`

**Evidence:** anon-2.jsonl:2307 · comment 412692361 · PR 6422 · 2023-07-19

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/requests/package.scala`

**Explicit source context (hunk):**

> +      customerAcknowledgements = v2.customerAcknowledgements
> +    )
> +  }
> +
>    case class StopRecurringInvestmentScheduleRequest(goalId: UUID, planId: UUID)
>  
>    object StopRecurringInvestmentScheduleRequest {

## A3-0477 — : Overall looks ok. But you’ll need to fix the import for play json serdes

**Source stance:** requested-change

**Context:**

> None; PR: [EN-1787][More recurring Schedules] DTO and model changes

**Source-preserving request, proposal, or question:**

> Overall looks ok. But you’ll need to fix the import for play json serdes

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2310 · comment 412991088 · PR 6422 · 2023-07-20

## A3-0489 — TransactionJdbcDbHandlerV1.scala: no need to rename at all. Just leave the latest as v1\_3… otherwise we will have massive PR just to rename things when we have v1\_4…

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcDbHandlerV1.scala; PR: Feat/INV-1762 deprecate transaction transititonal

**Concern stated in the source:** Just leave the latest as v1\_3… otherwise we will have massive PR just to rename things when we have v1\_4…

**Source-preserving request, proposal, or question:**

> I think no need to rename at all. Just leave the latest as v1\_3… otherwise we will have massive PR just to rename things when we have v1\_4…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2325 · comment 411313680 · PR 6436 · 2023-07-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcDbHandlerV1.scala`

## A3-0515 — Post-Lagom API contract exception versus actor serializer; goal internal exception pattern unresolved

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala; PR: [INV-1303] feat(rebalance): Increase min backoff to 1.5s

**Source-preserving request, proposal, or question:**

> Yeah this is where the voodoo happens.
> 
> 
> 
> Before:
> 
> * SvcException extends Lagom TransportException which the Lagom ExceptionSerializer knows how to serdes them. The `LagomServiceExceptionHelper` is extra logic to help avoiding sentry spamming
> * This same exception is also used to throw inside entity/cmdHandler. These can be serdes thanks to `JsonSerializer[AdvisorySvcException]`
> 
> 
> 
> After Lagom removal:
> 
> * SvcException in \*-api module are now intended as API contract only. They are converted to HTTP error via `EndpointResultCompat#mapToApiError`
> * akka serdes now is configured as
> 
> ```
> akka {
>   actor {
>     serializers {
>       play-json = "com.endowus.silver.persistence.serialization.PlayJsonSerializer"
>     }
>     serialization-bindings {
>       "akka.Done" = akka-misc
>       "akka.actor.Address" = akka-misc
>       "akka.remote.UniqueAddress" = akka-misc
>       "com.endowus.silver.persistence.serialization.PlayJsonSerializable" = play-json
>     }
>   }
> }
> ```
> 
> * this is why if we want serdes to work… we need to extends `PlayJsonSerializable` \(all the state/cmd/evt do this\)
> * however, it’s debate-able whether we want to add this to our API contract. You can see none of the services do this, except for goal svc
> 
> 
> 
> Goal svc does it in a subtle way:
> 
> * it creates another `GoalSvcException` inside goal-impl and throw this in entity/cmdHandler
> * this is why serdes works for goal svc \(and only goal svc\)
> * and if such internal GoalSvcException is propagate to http, it converts back to the goal-api GoalSvcException
> 
> ```
>   val ServiceErrorMap: Throwable => Throwable = {
>     case logic.GoalSvcException(message, errorType) => GoalSvcException.toApiError(GoalSvcException(message, errorType))
>     case e: GoalSvcException                        => GoalSvcException.toApiError(e)
>     case e                                          => e
>   }
> ```
> 
> 
> 
> So following goal svc should work - but I’m not sure if this is the right way to do it. Let’s think more before we mass apply this pattern

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Detailed before/after Lagom-removal serdes distinction retained. Goal internal GoalSvcException mapping is a possible model explicitly NOT approved for mass adoption.

**Evidence:** anon-2.jsonl:2351 · comment 407028769 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala`

> Yeah this is where the voodoo happens.
> 
> ‌
> 
> Before:
> 
> * SvcException extends Lagom TransportException which the Lagom ExceptionSerializer knows how to serdes them. The `LagomServiceExceptionHelper` is extra logic to help avoiding sentry spamming
> * This same exception is also used to throw inside entity/cmdHandler. These can be serdes thanks to `JsonSerializer[AdvisorySvcException]`
> 
> ‌
> 
> After Lagom removal:
> 
> * SvcException in \*-api module are now intended as API contract only. They are converted to HTTP error via `EndpointResultCompat#mapToApiError`
> * akka serdes now is configured as
> 
> ```
> akka {
>   actor {
>     serializers {
>       play-json = "com.endowus.silver.persistence.serialization.PlayJsonSerializer"
>     }
>     serialization-bindings {
>       "akka.Done" = akka-misc
>       "akka.actor.Address" = akka-misc
>       "akka.remote.UniqueAddress" = akka-misc
>       "com.endowus.silver.persistence.serialization.PlayJsonSerializable" = play-json
>     }
>   }
> }
> ```
> 
> * this is why if we want serdes to work… we need to extends `PlayJsonSerializable` \(all the state/cmd/evt do this\)
> * however, it’s debate-able whether we want to add this to our API contract. You can see none of the services do this, except for goal svc
> 
> ‌
> 
> Goal svc does it in a subtle way:
> 
> * it creates another `GoalSvcException` inside goal-impl and throw this in entity/cmdHandler
> * this is why serdes works for goal svc \(and only goal svc\)
> * and if such internal GoalSvcException is propagate to http, it converts back to the goal-api GoalSvcException
> 
> ```
>   val ServiceErrorMap: Throwable => Throwable = {
>     case logic.GoalSvcException(message, errorType) => GoalSvcException.toApiError(GoalSvcException(message, errorType))
>     case e: GoalSvcException                        => GoalSvcException.toApiError(e)
>     case e                                          => e
>   }
> ```
> 
> ‌
> 
> So following goal svc should work - but I’m not sure if this is the right way to do it. Let’s think more before we mass apply this pattern

**Evidence:** anon-2.jsonl:2351 · comment 407028769 · PR 6313 · 2023-06-28

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/handlers/TriggerThresholdBreachedRebalanceCmdHandler.scala`

**Explicit source context (hunk):**

> if (plan != cmd.loadedRebalancePlan) {
>        return Effect.replyError(cmd.replyTo)(
> -        new RebalanceSvcException(s"current plan state is inconsistent with command caller plan state for planId [${plan.planId}] received!",
> +        RebalanceSvcException(s"current plan state is inconsistent with command caller plan state for planId [${plan.planId}] received!",
>            RebalanceSvcErrorType.CONCURRENT_MODIFICATION
>          )
>        )

## A3-0518 — ChargeServiceE4s.scala: Yup. Will use amend script for this: * we can put all the queries required in the script to do one-time backfill for old fee charges * we still can re

**Source stance:** explanation

**Context:**

> charge-api/src/main/scala/com/endowus/silver/charge/api/ChargeServiceE4s.scala; PR: [INV-1710] feat(charge): Add endpoint to support back-filling absorbed GST in completed fee charge

**Source-preserving request, proposal, or question:**

> Yup. Will use amend script for this:
> 
> * we can put all the queries required in the script to do one-time backfill for old fee charges
> * we still can reuse this endpoint in future if ever needed on adhoc basis

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2354 · comment 406612914 · PR 6306 · 2023-06-27

Source path: `charge-api/src/main/scala/com/endowus/silver/charge/api/ChargeServiceE4s.scala`

> Yup. Will use amend script for this:
> 
> * we can put all the queries required in the script to do one-time backfill for old fee charges
> * we still can reuse this endpoint in future if ever needed on adhoc basis
> 
> ‌

**Evidence:** anon-2.jsonl:2354 · comment 406612914 · PR 6306 · 2023-06-27

Source path: `charge-api/src/main/scala/com/endowus/silver/charge/api/ChargeServiceE4s.scala`

**Explicit source context (hunk):**

> +      val forceUpdate = qs[Boolean]("forceUpdate")
> +
> +      endpoint(
> +        request(Patch, path / "api" / "v1" / "charge" / "backfill-absorbed-tax-details" /? (planId & feeChargeRequestId & forceUpdate), emptyRequest),
> +        withStatus(ok(emptyResponse))
> +      )
> +    }

## A3-0519 — SgServiceLogicImpl.scala: As I type this, I can’t recall why I even created `TaxCalculationDetails` at all… so I’m thinking to drop it. Will need to clean cassandra of charge s

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala; PR: [INV-1710] feat(charge): Add endpoint to support back-filling absorbed GST in completed fee charge

**Source-preserving request, proposal, or question:**

> As I type this, I can’t recall why I even created `TaxCalculationDetails` at all… so I’m thinking to drop it. Will need to clean cassandra of charge svc in d56

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2356 · comment 406613102 · PR 6306 · 2023-06-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2356 · comment 406613102 · PR 6306 · 2023-06-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      *
> +      * If full redemption fee charge crossed two quarters, e.g. 2022Q4 and beginning of 2023Q1, it was agreed that we
> +      * tax (and absorb) following tax rate of 2023Q1.
> +      */
> +    def extractTaxDate(request: FeeChargeRequest): LocalDate = {
> +      request.endDate
> +    }

## A3-0520 — SgServiceLogicImpl.scala: I’ll test this backfilling logic a bit with existing fee charge request in d56, then will drop this nested field

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala; PR: [INV-1710] feat(charge): Add endpoint to support back-filling absorbed GST in completed fee charge

**Source-preserving request, proposal, or question:**

> I’ll test this backfilling logic a bit with existing fee charge request in d56, then will drop this nested field

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2357 · comment 406623758 · PR 6306 · 2023-06-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2357 · comment 406623758 · PR 6306 · 2023-06-27

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      *
> +      * If full redemption fee charge crossed two quarters, e.g. 2022Q4 and beginning of 2023Q1, it was agreed that we
> +      * tax (and absorb) following tax rate of 2023Q1.
> +      */
> +    def extractTaxDate(request: FeeChargeRequest): LocalDate = {
> +      request.endDate
> +    }

## A3-0528 — SgTaxCalculator.scala: Placeholder logic for now. Not in-use until we add the backfill logic for old fee charges

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgTaxCalculator.scala; PR: [INV-1709] feat(charge): SG charge logic for GST

**Source-preserving request, proposal, or question:**

> Placeholder logic for now. Not in-use until we add the backfill logic for old fee charges

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2366 · comment 405842803 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgTaxCalculator.scala`

**Evidence:** anon-2.jsonl:2366 · comment 405842803 · PR 6283 · 2023-06-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/sg/SgTaxCalculator.scala`

**Explicit source context (hunk):**

> +    calculateTax(baseAmount, Gst8PctRate)
> +  }
> +
> +  def calculateTaxOnDate(baseAmount: BigDecimal, taxDate: LocalDate): Option[TaxCalculationResult] = {
> +    if (taxDate.isBefore(GstRegisteredDate)) {
> +      None
> +    } else if (taxDate.isBefore(Gst8PctEffectiveDate)) {

## A3-0541 — DividendDistributionEventProcessor.scala: Old events will not have fileVersion but they are actually on V1?

**Source stance:** open-question

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividenddistribution/processors/DividendDistributionEventProcessor.scala; PR: TT-2234 Add V2 parser for dividend distribution file

**Source-preserving request, proposal, or question:**

> Old events will not have fileVersion but they are actually on V1?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2383 · comment 405179177 · PR 5950 · 2023-06-21

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividenddistribution/processors/DividendDistributionEventProcessor.scala`

**Evidence:** anon-2.jsonl:2383 · comment 405179177 · PR 5950 · 2023-06-21

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividenddistribution/processors/DividendDistributionEventProcessor.scala`

**Explicit source context (hunk):**

> val fileName = ele.event.fileName
>      val fileGeneration = ele.event.fileGeneration
>      val eventTimestamp = EventEnvelopeUtils.extractEventTimestamp(ele).atZone(timeService.zoneId)
> +    val fileVersion = ele.event.fileVersion.getOrElse(DividendDistributionFileVersion.V1) // Any event without file version would have been created for the V1 parser
> +    val fileParser = dividendDistributionFileParserFactory.getParser(fileVersion)
> +
>      // Note: We want to make sure that we only start distributing after we confirmed that all rows in the file are valid

## A3-0567 — BaseChargeServiceE4s.scala: After we release today, help me rebase and add these endpoints to BaseChargeService too. I know it’s not used but let’s just be consistent. In fact, w

**Source stance:** requested-change

**Context:**

> charge-api/src/main/scala/com/endowus/silver/charge/api/BaseChargeServiceE4s.scala; PR: Resolve INV-1298: Charge different fees for quant edge

**Source-preserving request, proposal, or question:**

> After we release today, help me rebase and add these endpoints to BaseChargeService too. I know it’s not used but let’s just be consistent.
> 
> In fact, we might be able to add the mandatory rebate for existing AltsB3 instruments via amend-script. That will require the endpoints in Lagom ChargeService

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2414 · comment 400693251 · PR 6038 · 2023-06-06

Source path: `charge-api/src/main/scala/com/endowus/silver/charge/api/BaseChargeServiceE4s.scala`

## A3-0584 — PlanProfileJdbcRepositoryV2.scala: Ok let’s up-version this table and fix this next, after we release these open PRs :thumbsup:

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/profile/jdbc/PlanProfileJdbcRepositoryV2.scala; PR: Resolve INV-1570: Changes to return accumulated plan fees.

**Source-preserving request, proposal, or question:**

> Ok let’s up-version this table and fix this next, after we release these open PRs :thumbsup:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2431 · comment 400278928 · PR 6100 · 2023-06-05

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/profile/jdbc/PlanProfileJdbcRepositoryV2.scala`

**Evidence:** anon-2.jsonl:2431 · comment 400278928 · PR 6100 · 2023-06-05

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/profile/jdbc/PlanProfileJdbcRepositoryV2.scala`

**Explicit source context (hunk):**

> }
>    }
>  
> +  override def streamAltsCustomers: Source[UUID, NotUsed] = {
> +    streamCustomers(
> +      goalTypes = Set(InvestmentGoalType.GENERAL_WEALTH_ACCUMULATION),
> +      targetTradingAccountTypes = Set(TradingAccountType.SINGAPORE_USD_CASH_ACCOUNT, TradingAccountType.HONGKONG_USD_CASH_ACCOUNT)

## A3-0642 — : Will trading release this for HK too? If yes, we would need to handle in V2 entity?

**Source stance:** open-question

**Context:**

> None; PR: [INV-1438] feat(transaction): Listen to trading messages for asset_transfer

**Source-preserving request, proposal, or question:**

> Will trading release this for HK too? If yes, we would need to handle in V2 entity?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2491 · comment 391965757 · PR 5918 · 2023-05-05

## A3-0646 — TransactionJdbcDbHandlerV1.scala: You don’t need to rename this. Just leave it as is. When migration is completed, we can simply drop it.

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcDbHandlerV1.scala; PR: [INV-1438] feat(transaction): Listen to trading messages for asset_transfer

**Source-preserving request, proposal, or question:**

> You don’t need to rename this. Just leave it as is. When migration is completed, we can simply drop it.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2495 · comment 392000186 · PR 5918 · 2023-05-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcDbHandlerV1.scala`

## A3-0647 — TransactionTableV1.scala: Same. Don’t need to rename this

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionTableV1.scala; PR: [INV-1438] feat(transaction): Listen to trading messages for asset_transfer

**Source-preserving request, proposal, or question:**

> Same. Don’t need to rename this

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2496 · comment 392000379 · PR 5918 · 2023-05-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionTableV1.scala`

## A3-0668 — package.scala: Ok to default here, because otherwise we have to update many places

**Source stance:** explanation

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/package.scala; PR: [INV-1437] feat(transaction): Models

**Concern stated in the source:** Ok to default here, because otherwise we have to update many places

**Source-preserving request, proposal, or question:**

> Ok to default here, because otherwise we have to update many places

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Defaults tolerated here specifically to avoid changing many call sites.

**Evidence:** anon-2.jsonl:2518 · comment 387921832 · PR 5770 · 2023-04-19

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/package.scala`

**Evidence:** anon-2.jsonl:2518 · comment 387921832 · PR 5770 · 2023-04-19

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/package.scala`

**Explicit source context (hunk):**

> fxConversionDetails: Option[FxConversionDetailsDto] = None,
> -    withdrawToLinkedBankAccount: Option[Boolean] = None
> +    withdrawToLinkedBankAccount: Option[Boolean] = None,
> +    assetTransferDetails: Option[AssetTransferDetailsDto] = None
>    ) extends Ordered[TransactionDto] {
>  
>      override def compare(that: TransactionDto): Int = {

## A3-0679 — Proposed requestedUnits at AssetTransfer top level later withdrawn after L1 usage review

**Source stance:** suggestion

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1437] feat(transaction): Models

**Source-preserving request, proposal, or question:**

> I suppose we can add `requestedUnits` to v2 `AssetTransferTransactionDto` with same rationale as `requestedDate`, i.e. the fields are set on creation, and immutable onwards regardless of status

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Proposed requestedUnits addition is later withdrawn in2533 because L1 does not show it; do not promote to settled requirement.
- Related source rows 2529, 2533, 2534: RequestedUnits top-level addition is withdrawn after L1 display check; StatusFields rationale remains separate.

**Evidence:** anon-2.jsonl:2529 · comment 390028406 · PR 5770 · 2023-04-27

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Evidence:** anon-2.jsonl:2529 · comment 390028406 · PR 5770 · 2023-04-27

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> +          createdAt = Some(t.createdAt),
> +          assetTransferDetails = Some(
> +            AssetTransferDetailsDto(
> +              counterpartyPlatform = t.counterpartyPlatform,
> +              counterpartyAccountNumber = t.counterpartyAccountNumber,
> +              requestedDate = t.requestedDate,
> +              instrumentId = t.instrumentId,

## A3-0683 — StatusFields V1 bridge differs from always-present AssetTransfer units

**Source stance:** explanation

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala; PR: [INV-1437] feat(transaction): Models

**Source-preserving request, proposal, or question:**

> My rationale on not-using-StatusFields for this is:
> 
> * StatusFields is a bridge to V1 to support these optional-per-status fields, e.g. requestedAmount is None and only populated when transaction is created, settledAmount is None and only populated when transaction is settled etc
> * These fields are at top level in v1 TransactionDto, so the v2 to v1 mapping, we just blindly set them
> * Whereas in this AssetTransfer case, the field is required in v1 \(since we create dedicated v1 DTO for it\), and the value is always populated either with requestedUnits or settledUnits. This means `statusFields.requestedUnits` wouldn’t be used anywhere, but when it’s used for AssetTransfer, we will call `Option.get`. This is why it looks off in my head.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 2529, 2533, 2534: RequestedUnits top-level addition is withdrawn after L1 display check; StatusFields rationale remains separate.

**Evidence:** anon-2.jsonl:2534 · comment 390032775 · PR 5770 · 2023-04-27

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

> My rationale on not-using-StatusFields for this is:
> 
> * StatusFields is a bridge to V1 to support these optional-per-status fields, e.g. requestedAmount is None and only populated when transaction is created, settledAmount is None and only populated when transaction is settled etc
> * These fields are at top level in v1 TransactionDto, so the v2 to v1 mapping, we just blindly set them
> * Whereas in this AssetTransfer case, the field is required in v1 \(since we create dedicated v1 DTO for it\), and the value is always populated either with requestedUnits or settledUnits. This means `statusFields.requestedUnits` wouldn’t be used anywhere, but when it’s used for AssetTransfer, we will call `Option.get`. This is why it looks off in my head.
> 
> ‌

**Evidence:** anon-2.jsonl:2534 · comment 390032775 · PR 5770 · 2023-04-27

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/TransactionTypes.scala`

**Explicit source context (hunk):**

> +          createdAt = Some(t.createdAt),
> +          assetTransferDetails = Some(
> +            AssetTransferDetailsDto(
> +              counterpartyPlatform = t.counterpartyPlatform,
> +              counterpartyAccountNumber = t.counterpartyAccountNumber,
> +              requestedDate = t.requestedDate,
> +              instrumentId = t.instrumentId,

## A3-0688 — TransactionTableV1_2.scala: No change required, but just to make sure we are on same page, this is the final table we want to switch over to. It’s not “intermediary”

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionTableV1_2.scala; PR: [INV-1437] feat(transaction): Models

**Source-preserving request, proposal, or question:**

> No change required, but just to make sure we are on same page, this is the final table we want to switch over to. It’s not “intermediary”

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2539 · comment 391031702 · PR 5770 · 2023-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionTableV1_2.scala`

**Evidence:** anon-2.jsonl:2539 · comment 391031702 · PR 5770 · 2023-05-02

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionTableV1_2.scala`

**Explicit source context (hunk):**

> +  val pkName = s"transaction_pk_v${dtoVersion}_${dbVersion}"
> +}
> +
> +class TransactionTableV1_2(tag: Tag)
> +    extends Table[Transaction](
> +      tag,
> +      Some(TransactionTableV1_2.schemaName),

## A3-0704 — Historical event-handler change accepted as specific exception, supporting Jira unavailable

**Source stance:** suggestion

**Context:**

> None; PR: [INV-1473] feat(portfolio): Update logic about latest TAA in ModelPortfolioEntity

**Source-preserving request, proposal, or question:**

> It’s against the rule of not changing behaviour of event handler in EventSource…. but in this specific case, I think it’s safe to do so.
> 
> More context in Jira [<url> data-inline-card='' }

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Changing event handler behavior is accepted only as source-specific safe exception; supporting Jira is redacted and not available.

**Evidence:** anon-2.jsonl:2555 · comment 388008639 · PR 5787 · 2023-04-19

## A3-0730 — package.scala: Sorry I forgot to mention. I put without default initially and set in all the places required in new model. Then provide default so that we don’t need

**Source stance:** explanation

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/package.scala; PR: [INV-1362] feat(transaction) Add withdrawToLinkedBankAccount flag for RedemptionTransaction

**Concern stated in the source:** Then provide default so that we don’t need to mass change everywhere in old model.

**Source-preserving request, proposal, or question:**

> Sorry I forgot to mention. I put without default initially and set in all the places required in new model. Then provide default so that we don’t need to mass change everywhere in old model.
> 
> This field in new model is not optional, and limited to redemption transaction only.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2582 · comment 384583158 · PR 5655 · 2023-04-05

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/package.scala`

**Evidence:** anon-2.jsonl:2582 · comment 384583158 · PR 5655 · 2023-04-05

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/package.scala`

**Explicit source context (hunk):**

> dividendDetails: Option[DividendDetailsDto] = None,
> -    fxConversionDetails: Option[FxConversionDetailsDto] = None
> +    fxConversionDetails: Option[FxConversionDetailsDto] = None,
> +    withdrawToLinkedBankAccount: Option[Boolean] = None
>    ) extends Ordered[TransactionDto] {
>  
>      override def compare(that: TransactionDto): Int = {

## A3-0756 — TransactionApplication.scala: We don’t want these V1 entity for transaction in SG anymore?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/TransactionApplication.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> We don’t want these V1 entity for transaction in SG anymore?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2608 · comment 370755182 · PR 5266 · 2023-02-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/TransactionApplication.scala`

## A3-0822 — Recurring failure email: actual reason, event-domain coupling and direct-publish deferral

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/communication/hk/HkRecurringInvestmentFailureEmailComposer.scala; PR: Resolve INV-1135: Send email for failed recurring investments with state change info

**Concern stated in the source:** And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain.

* Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
* You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
* If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)

**Source-preserving request, proposal, or question:**

> Yeah simulation only makes sense if we want to warn user about potential failure in the upcoming-recurring-investment email. For this jira, we want to include exactly the failure reason. This means the entry point to construct the email should already contain the failure reason, passed from the `RecurringInvestmentProcessor`.
> 
> 
> 
> This can be achieved via Cmd\+Evt like what you did here. However, I feel we might couple our event domain with the copy \(suitability VS risk breach\), e.g today we add CrBreach as reason, tmr copy wants to distinguish between Cat1 breach vs Cat2 breach. And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain. Not to mention, we would likely support this to SG too - in which case, do we want to handle SG vs HK failure reason in the event?
> 
> 
> 
> The above is not necessarily wrong, but I don’t think we know everything to decide it now. And there’s a way to postpone this decision: by publishing directly to communication in the `RecurringInvestmentProcessor`
> 
> * Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
> * You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
> * If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)
> 
> 
> 
> `RecurringInvestmentRequestFailedEvent` with proper region-specific failure reason sounds like a good thing to me, I’m just not sure we’re ready to implement it yet.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Keep upcoming-warning simulation distinct from actual failure reason. Persisted region/compliance/copy coupling is unresolved; direct publish with bounded retry/manual endpoint is a deferral option, later task topic/event flow conditional on slowness.

**Evidence:** anon-2.jsonl:2679 · comment 369402726 · PR 5203 · 2023-02-13

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/utils/communication/hk/HkRecurringInvestmentFailureEmailComposer.scala`

> Yeah simulation only makes sense if we want to warn user about potential failure in the upcoming-recurring-investment email. For this jira, we want to include exactly the failure reason. This means the entry point to construct the email should already contain the failure reason, passed from the `RecurringInvestmentProcessor`.
> 
> ‌
> 
> This can be achieved via Cmd\+Evt like what you did here. However, I feel we might couple our event domain with the copy \(suitability VS risk breach\), e.g today we add CrBreach as reason, tmr copy wants to distinguish between Cat1 breach vs Cat2 breach. And if we add all applicable compliance block reasons \(so that we can evolve the email logic freely\), we would also bake the compliance domain to investment event domain. Not to mention, we would likely support this to SG too - in which case, do we want to handle SG vs HK failure reason in the event?
> 
> ‌
> 
> The above is not necessarily wrong, but I don’t think we know everything to decide it now. And there’s a way to postpone this decision: by publishing directly to communication in the `RecurringInvestmentProcessor`
> 
> * Since it might fail, we should retry, and add support to retry manually via endpoint, if needed
> * You can add all the failure reasons here, but no need to think too hard, cuz it’s all on the fly - nothing is persisted
> * If it gets too slow and starts impacting the main triggering flow, we can revisit moving to event processor \(or postpone further by dispatching to another kafka topic, and construct the email and publish to communication from there\)
> 
> ‌
> 
> `RecurringInvestmentRequestFailedEvent` with proper region-specific failure reason sounds like a good thing to me, I’m just not sure we’re ready to implement it yet. 
> 
> ‌

## A3-0836 — : I guess this one we will add a sync to update existing plans?

**Source stance:** open-question

**Context:**

> None; PR: fix(goal): INV-1248 save dividend distribution preference to DB

**Source-preserving request, proposal, or question:**

> I guess this one we will add a sync to update existing plans?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2694 · comment 374537418 · PR 5410 · 2023-03-03

## A3-0919 — CraManager.scala: Hmm this will emit `ExpiryDateOverriddenEvt` which is not what happening here… I think we will need another pair of cmd/event

**Source stance:** observed-defect

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Hmm this will emit `ExpiryDateOverriddenEvt` which is not what happening here… I think we will need another pair of cmd/event

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2778 · comment 367135684 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2778 · comment 367135684 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        case _: VulnerableCustomerProfile =>
> +          logger.warn(s"Customer $customerId is vulnerable")
> +          Future.successful(Done)
> +      }
> +    } yield Done
> +  }
> +

## A3-0920 — Stale onboarding DOB can overwrite newer customer DOB: version/timestamp TODO

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/subscribers/hk/CustomerPersonalDetailsTopicSubscriber.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Chance is low, but if somehow we have lag on onboarding svc side… we might run into situation that we write latest value of DOB from customer svc to the table, and then it got overridden with stale value from onboarding svc… Will need some version or timestamp to avoid it…
> 
> Let’s note a TODO for now

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Stale onboarding DOB can overwrite newer customer DOB; version/timestamp repair is left TODO, not implemented.

**Evidence:** anon-2.jsonl:2779 · comment 367136193 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/subscribers/hk/CustomerPersonalDetailsTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2779 · comment 367136193 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/subscribers/hk/CustomerPersonalDetailsTopicSubscriber.scala`

**Explicit source context (hunk):**

> case msg: RegionalPersonalDetailsUpdatedMsg =>
> -      recalculateVcStatus(msg.customerId, "CustomerService")
> +      handleCustomerInfoUpdated(
> +        CustomerProjectionData(
> +          customerId = msg.customerId,
> +          dateOfBirth = msg.regionalPersonalDetailsDto.genericPersonalDetailsDto.dateOfBirth,
> +          lastUpdated = msg.updatedAt.toInstant

## A3-1040 — CustomerCraUpdatedLogic.scala: Ah I should have added the timestamp in the event :see_no_evil:

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerCraUpdatedLogic.scala; PR: Feat/INV-676 cancel investment vc expired

**Source-preserving request, proposal, or question:**

> Ah I should have added the timestamp in the event :see_no_evil:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2904 · comment 350429242 · PR 4789 · 2022-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerCraUpdatedLogic.scala`

**Evidence:** anon-2.jsonl:2904 · comment 350429242 · PR 4789 · 2022-12-02

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/CustomerCraUpdatedLogic.scala`

**Explicit source context (hunk):**

> +
> +  override def handleCustomerExpiryDateChange(customerId: UUID, isCraExpired: Boolean): Future[Done] = {
> +    if (isCraExpired) {
> +      cancelAllPendingInvestments(customerId, Instant.now())
> +    } else {
> +      Future.successful(Done)
> +    }

## A3-1101 — PlanCommunicationV2EventProcessor.scala: If we throw here, the event processor will get stuck. And given we can’t practically modify event, should we just log error and move on?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala; PR: Feat/EN-312 comm v2 for redemption investment

**Concern stated in the source:** If we throw here, the event processor will get stuck.

**Source-preserving request, proposal, or question:**

> If we throw here, the event processor will get stuck. And given we can’t practically modify event, should we just log error and move on?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2968 · comment 344067505 · PR 4602 · 2022-11-09

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Evidence:** anon-2.jsonl:2968 · comment 344067505 · PR 4602 · 2022-11-09

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/PlanCommunicationV2EventProcessor.scala`

**Explicit source context (hunk):**

> +        )
> +        Future.successful(List())
> +      } { previousSchedule =>
> +        val commIdSeed = "RECURRING_INVESTMENT_STOPPED" + "|" + event.planId.toString + "|" + event.removedAt.toString
> +        val communicationId = UUID.nameUUIDFromBytes(commIdSeed.getBytes)
> +
> +        for {

## A3-1109 — PlanAcknowledgementManagerEvents.scala: Cmd I guess we can merge them all in single `RemoveAcknowledgementsCmd`, but let’s not merge them in events

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala; PR: [INV-675] Added modify acks with testcase

**Source-preserving request, proposal, or question:**

> Cmd I guess we can merge them all in single `RemoveAcknowledgementsCmd`, but let’s not merge them in events

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2976 · comment 343433664 · PR 4605 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala`

**Evidence:** anon-2.jsonl:2976 · comment 343433664 · PR 4605 · 2022-11-07

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala`

**Explicit source context (hunk):**

> implicit val format: Format[AcknowledgedRecurringInvestmentEvt] = Json.format
>    }
>  
> +  case object CraCat2AcknowledgementRemovedEvt extends PlanAcknowledgementManagerEvent {
> +    implicit val format: Format[CraCat2AcknowledgementRemovedEvt.type] = Json.format
> +  }
> +

## A3-1119 — : Will do the following in next PR: * enrich audit payload * persist to audit repository * add internal query endpoints for audit repository

**Source stance:** explanation

**Context:**

> None; PR: Feat/INV-558 CR audit

**Source-preserving request, proposal, or question:**

> Will do the following in next PR:
> 
> * enrich audit payload
> * persist to audit repository
> * add internal query endpoints for audit repository

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2990 · comment 343769577 · PR 4628 · 2022-11-08

> Will do the following in next PR:
> 
> * enrich audit payload
> * persist to audit repository
> * add internal query endpoints for audit repository
> 
> ‌

## A3-1186 — TransactionService.scala: Don’t we need V2 for this too?

**Source stance:** open-question

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/TransactionService.scala; PR: feat/INV-442 Transaction V2 Impl

**Source-preserving request, proposal, or question:**

> Don’t we need V2 for this too?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3059 · comment 339574020 · PR 4436 · 2022-10-21

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/TransactionService.scala`

**Evidence:** anon-2.jsonl:3059 · comment 339574020 · PR 4436 · 2022-10-21

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/TransactionService.scala`

**Explicit source context (hunk):**

> ccy: Option[String] = None
>    ): ServiceCall[NotUsed, TransactionListDto]
>  
> +  def queryCustomerTransactions(
> +    customerId: UUID,
> +    accountType: Option[TradingAccountType] = None,
> +    goalId: Option[UUID] = None,
> +    planId: Option[UUID] = None,
> +    transactionTypes: Option[List[TransactionType]] = None
> +  ): ServiceCall[NotUsed, TransactionTypes.TransactionListDto]
> +
>    def queryTransactionsForActivities(
>      customerId: Option[UUID] = None,
>      accountType: Option[String],

## A3-1197 — PlanAcknowledgementManagerEvents.scala: Generally, we want to capture events as facts that happened, so this should be `CraCat2AckedEvt`

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala; PR: Feat/INV-560 recurring and ack persistence

**Source-preserving request, proposal, or question:**

> Generally, we want to capture events as facts that happened, so this should be `CraCat2AckedEvt`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3070 · comment 337483304 · PR 4477 · 2022-10-13

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala`

**Evidence:** anon-2.jsonl:3070 · comment 337483304 · PR 4477 · 2022-10-13

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/acknowledgements/ces/PlanAcknowledgementManagerEvents.scala`

**Explicit source context (hunk):**

> +      AggregateEventTag.sharded[PlanAcknowledgementManagerEvent](NumShards)
> +  }
> +
> +  case class AcknowledgedCraCat2Evt(
> +     ackTime: Instant
> +  ) extends PlanAcknowledgementManagerEvent
> +

## A3-1208 — TradingRestrictionLogic.scala: FYi… I’ll implement this when I add the refId as part of audit

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala; PR: Feat/INV-560 recurring and ack persistence

**Source-preserving request, proposal, or question:**

> FYi… I’ll implement this when I add the refId as part of audit

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3082 · comment 338184689 · PR 4477 · 2022-10-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

> FYi… I’ll implement this when I add the refId as part of audit
> 
> ‌

**Evidence:** anon-2.jsonl:3082 · comment 338184689 · PR 4477 · 2022-10-17

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/TradingRestrictionLogic.scala`

**Explicit source context (hunk):**

> -      }
> +      planAcknowledgements <- preloadAckForRecurringRequest(request, planId)
> +      response <- doCraChecks(request, customerId)(craValidationOutput, planAcknowledgements, targetAllocation, advisoryProfile)
> +      //TODO Add logging to notify failure of persisting acks (Check orphaned earmark)
> +      _ <- persistAcksIfRequired(request, planId)(response)
>      } yield response
>    }

## A3-1225 — ServiceLogicImpl.scala: Shall we drop the Cassandra repository too, to avoid further wrong usage?

**Source stance:** open-question

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImpl.scala; PR: adds fund inception date/distribution status/is complex to instrument

**Source-preserving request, proposal, or question:**

> Shall we drop the Cassandra repository too, to avoid further wrong usage?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3100 · comment 336602364 · PR 4455 · 2022-10-10

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:3100 · comment 336602364 · PR 4455 · 2022-10-10

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> override def getInstrumentByIds(ids: List[String]): Future[Seq[InstrumentInfoDto]] = {
> -    instrumentRepository.findByIds(ids)
> +    instrumentJdbcRepository.findByIds(ids).map(_.map(toDto))
>    }
>  
>    override def getInstrumentByIdSet(request: Set[String]): Future[Seq[InstrumentInfoDto]] = {

## A3-1292 — BuyEarmark sameID/amount idempotency validated in command, event appends only

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Concern stated in the source:** So that in event handler, we would simply add the earmark to the list

**Source-preserving request, proposal, or question:**

> So WDYT about this? IMO, we should:
> 
> * if brand new earmark, add it
> * if match existing id:
> 
>     * if amount is fine, do nothing
>     * if amount is different, it feels like we should reject the command here, since for same ID, we should not change at all
>     
> 
> This logic should ideally sit in the command handler, i.e. `handleCreateBuyEarmark`
> 
> So that in event handler, we would simply add the earmark to the list
> 
> 
> 
> In case of some error that requires changing amount of an existing earmark, let’s add separate command for it?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- New earmark emits; sameID+sameamount no-op; sameID+differentamount reject, separate correction command. Validate in command handler so event handler only appends.
- Related source rows 3174, 3178, 3180, 3185, 3200, 3201: Keep currentVersion check, no-op duplicateID+amount, reject changed amount, new event only for new earmark;3200 question does not override3201 matrix.

**Evidence:** anon-2.jsonl:3174 · comment 333428532 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

> So WDYT about this? IMO, we should:
> 
> * if brand new earmark, add it
> * if match existing id:
> 
>     * if amount is fine, do nothing
>     * if amount is different, it feels like we should reject the command here, since for same ID, we should not change at all
>     
> 
> This logic should ideally sit in the command handler, i.e. `handleCreateBuyEarmark`
> 
> So that in event handler, we would simply add the earmark to the list
> 
> ‌
> 
> In case of some error that requires changing amount of an existing earmark, let’s add separate command for it?

**Evidence:** anon-2.jsonl:3174 · comment 333428532 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +    case (evt: BuyEarmarkCreatedEvt, state) => state.copy(evt.buyEarmark +: state.buyEarmarks)
> +  }
> +
> +  private def handleCreateBuyEarmark(
> +                                      cmd: CreateBuyEarmarkCmd,
> +                                      ctx: CommandContext[Done],
> +                                      state: CustomerTradingEarmarkManagerState): Persist = {

## A3-1296 — CustomerTradingEarmarkManagerEntity.scala: the idea is we validate and reject in command handler, so that event handler can be dumb and just append

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Concern stated in the source:** Yeah the idea is we validate and reject in command handler, so that event handler can be dumb and just append

**Source-preserving request, proposal, or question:**

> Yeah the idea is we validate and reject in command handler, so that event handler can be dumb and just append

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 3174, 3178, 3180, 3185, 3200, 3201: Keep currentVersion check, no-op duplicateID+amount, reject changed amount, new event only for new earmark;3200 question does not override3201 matrix.

**Evidence:** anon-2.jsonl:3178 · comment 333436666 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Evidence:** anon-2.jsonl:3178 · comment 333436666 · PR 4344 · 2022-09-27

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +    case (evt: BuyEarmarkCreatedEvt, state) => state.copy(evt.buyEarmark +: state.buyEarmarks)
> +  }
> +
> +  private def handleCreateBuyEarmark(
> +                                      cmd: CreateBuyEarmarkCmd,
> +                                      ctx: CommandContext[Done],
> +                                      state: CustomerTradingEarmarkManagerState): Persist = {

## A3-1298 — Same earmarkID+amount returns Done without event

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> If exists earmark with same ID and same amount, we don’t want to create another earmark - we want to reply done without any event, maybe can add some logs for troubleshooting purpose

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 3174, 3178, 3180, 3185, 3200, 3201: Keep currentVersion check, no-op duplicateID+amount, reject changed amount, new event only for new earmark;3200 question does not override3201 matrix.

**Evidence:** anon-2.jsonl:3180 · comment 333680877 · PR 4344 · 2022-09-28

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Evidence:** anon-2.jsonl:3180 · comment 333680877 · PR 4344 · 2022-09-28

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +          if (existingEarmark.amount != cmd.buyEarmark.amount) {
> +            ctx.commandFailed(
> +              ComplianceServiceException(ComplianceServiceErrorType.ConcurrentModification,
> +                s"Earmark exists with same id ${cmd.buyEarmark.id} but with different amount, illegal operation!"
> +              )
> +            )
> +            ctx.done

## A3-1319 — BuyEarmark currentVersion then ID+amount branch matrix

**Source stance:** explanation

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Hmm current logic is:
> 
> 1. if different version => you validate on stale data, reject due to concurrent request
> 2. if same version:
> 
>     1. if brand new id => event
>     2. same id exists:
>     
>         1. different amount => something is wrong, error \(if want to amend, then we need different command\)
>         2. same amount => it’s no-op, just reply Done
>         
>     
> 
> 
> 
> Which part are you suggesting to change? 2.b.ii?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Keep concurrency-version branch before ID+amount branch; same-version+newID emits, differentamount errors, sameamount no-op; question about which branch to alter remains open.
- Related source rows 3174, 3178, 3180, 3185, 3200, 3201: Keep currentVersion check, no-op duplicateID+amount, reject changed amount, new event only for new earmark;3200 question does not override3201 matrix.

**Evidence:** anon-2.jsonl:3201 · comment 334076151 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

> Hmm current logic is:
> 
> 1. if different version => you validate on stale data, reject due to concurrent request
> 2. if same version:
> 
>     1. if brand new id => event
>     2. same id exists:
>     
>         1. different amount => something is wrong, error \(if want to amend, then we need different command\)
>         2. same amount => it’s no-op, just reply Done
>         
>     
> 
> ‌
> 
> Which part are you suggesting to change? 2.b.ii?
> 
> ‌

**Evidence:** anon-2.jsonl:3201 · comment 334076151 · PR 4344 · 2022-09-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +                                      cmd: CreateBuyEarmarkCmd,
> +                                      ctx: CommandContext[Done],
> +                                      state: CustomerTradingEarmarkManagerState): Persist = {
> +    if (cmd.currentVersion != state.version) {
> +      ctx.commandFailed(
> +        ComplianceServiceException(ComplianceServiceErrorType.ConcurrentModification,
> +          s"Earmark have been modified, this request is stale! Request version ${cmd.currentVersion}, current version ${state.version}!"

## A3-1325 — CustomerTradingEarmarkManagerEvents.scala: Hmmm one action should only create one BuyEarmark I think. Only action that would trigger multiple earmark is modification of a multiple-plan goal. Bu

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerEvents.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Hmmm one action should only create one BuyEarmark I think. Only action that would trigger multiple earmark is modification of a multiple-plan goal. But even then, we might want to emit multiple event instead. Let’s think a bit more on this.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3207 · comment 333140108 · PR 4330 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerEvents.scala`

**Evidence:** anon-2.jsonl:3207 · comment 333140108 · PR 4330 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/ces/CustomerTradingEarmarkManagerEvents.scala`

**Explicit source context (hunk):**

> }
>  
> +  case class BuyTradingEarmarkCreatedEvt(
> +    buyEarmark: BuyEarmark
> +  ) extends CustomerTradingEarmarkManagerEvent
> +
> +  object BuyTradingEarmarkCreatedEvt {

## A3-1326 — CustomerTradingEarmarkManagerEntity.scala: Ah I think the event should contain only the new earmark, and we append inside `handleEvents` instead of here

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala; PR: Feat/INV-486 add goal earmark

**Source-preserving request, proposal, or question:**

> Ah I think the event should contain only the new earmark, and we append inside `handleEvents` instead of here

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3208 · comment 333140369 · PR 4330 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Evidence:** anon-2.jsonl:3208 · comment 333140369 · PR 4330 · 2022-09-26

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/entities/CustomerTradingEarmarkManagerEntity.scala`

**Explicit source context (hunk):**

> +    }else if (state.buyEarmarks.exists(e => e.id.equals(cmd.buyEarmark.id) && e.amount != cmd.buyEarmark.amount)) {
> +      ctx.commandFailed(
> +        ComplianceServiceException(ComplianceServiceErrorType.ConcurrentModification,
> +          s"Earmark exists with same id ${cmd.buyEarmark.id} but with different amount, illegal operation!"
> +        )
> +      )
> +      ctx.done

## A3-1349 — transactionTypes.scala: When would we need to do this conversion? Ideally we should only to convert from \(old/new\) domain to \(old/new\) DTO, but not between old/new DTO I 

**Source stance:** open-question

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/transactionTypes.scala; PR: [WIP] INV-235 Transaction Service v2 models

**Source-preserving request, proposal, or question:**

> When would we need to do this conversion? Ideally we should only to convert from \(old/new\) domain to \(old/new\) DTO, but not between old/new DTO I think

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3235 · comment 329426164 · PR 4217 · 2022-09-09

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/transactionTypes.scala`

**Evidence:** anon-2.jsonl:3235 · comment 329426164 · PR 4217 · 2022-09-09

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/transactionTypes.scala`

**Explicit source context (hunk):**

> +    implicit val format: Format[TransactionDto] = Json.format[TransactionDto]
> +  }
> +
> +  def toTransactionDtoV1(transactionV2: TransactionDto): models.TransactionDto = {
> +    transactionV2 match {
> +      case t: InvestmentTransactionDto =>
> +        models.TransactionDto(

## A3-1354 — transactionTypes.scala: so I’m saying we should convert from new entity to old/new DTO, instead of new DTO to old DTO

**Source stance:** requested-change

**Context:**

> transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/transactionTypes.scala; PR: [WIP] INV-235 Transaction Service v2 models

**Source-preserving request, proposal, or question:**

> Yeah so I’m saying we should convert from new entity to old/new DTO, instead of new DTO to old DTO

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3240 · comment 329768076 · PR 4217 · 2022-09-12

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/transactionTypes.scala`

> Yeah so I’m saying we should convert from new entity to old/new DTO, instead of new DTO to old DTO
> 
> ‌

**Evidence:** anon-2.jsonl:3240 · comment 329768076 · PR 4217 · 2022-09-12

Source path: `transaction-api/src/main/scala/com/endowus/silver/transaction/api/models/transactionTypes.scala`

**Explicit source context (hunk):**

> +    implicit val format: Format[TransactionDto] = Json.format[TransactionDto]
> +  }
> +
> +  def toTransactionDtoV1(transactionV2: TransactionDto): models.TransactionDto = {
> +    transactionV2 match {
> +      case t: InvestmentTransactionDto =>
> +        models.TransactionDto(

## A3-1355 — transactionTypes.scala: on point \(3\), it’s not about losing data. Old data is still there in events, we just want latest snapshot in State \(ideally\). From readside point 

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala; PR: [WIP] INV-235 Transaction Service v2 models

**Source-preserving request, proposal, or question:**

> Yeah on point \(3\), it’s not about losing data. Old data is still there in events, we just want latest snapshot in State \(ideally\). From readside point of view, we can always have a read model providing snapshot, and potentially another read model providing all data, if needed. But as you pointed out, we don’t need this old data today. In fact, we store all fields, and then have to introduce object level fields like amount and statusUpdatedAt to merge the them again.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3241 · comment 329769641 · PR 4217 · 2022-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala`

**Evidence:** anon-2.jsonl:3241 · comment 329769641 · PR 4217 · 2022-09-12

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/transactionTypes.scala`

**Explicit source context (hunk):**

> +    goalId: UUID,
> +    planId: UUID,
> +    requestedAmount: BigDecimal,
> +    assumedAmount: Option[BigDecimal] = None,
> +    settledAmount: Option[BigDecimal] = None,
> +    recurringTransactionId: Option[String] = None,
> +    assumedAt: Option[ZonedDateTime] = None,

## A3-1357 — CRA scoring/questionnaire versions evolve independently: v1.2/v1.3 versus v2.1

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/hk/cra/questionnaire/QuestionnaireV1.scala; PR: [INV-349] feat(advisory): Trigger CRA VC status reassessment when customer update PersonalDetails

**Source-preserving request, proposal, or question:**

> Yeah they can potentially evolve independently. E.g.
> 
> * scoring matrix may change, but the questionnaire shown to customer stays the same → v1.2, v1.3, etc
> * new questionnaire → v2.1

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3243 · comment 329415610 · PR 4209 · 2022-09-09

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/hk/cra/questionnaire/QuestionnaireV1.scala`

> Yeah they can potentially evolve independently. E.g.
> 
> * scoring matrix may change, but the questionnaire shown to customer stays the same → v1.2, v1.3, etc
> * new questionnaire → v2.1
> 
> ‌

**Evidence:** anon-2.jsonl:3243 · comment 329415610 · PR 4209 · 2022-09-09

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/calculators/hk/cra/questionnaire/QuestionnaireV1.scala`

**Explicit source context (hunk):**

> )
> +}
> +
> +case object `QuestionnaireV1.1` extends Questionnaire {
>  
>    private object VulnerableCustomerMatrixV1 extends VcCalculationMatrix {

## A3-1359 — package.scala: I need these 2 extra fields on instrument. Ideally they should be required in HK context. Not sure how we want to proceed with this yet, I just add th

**Source stance:** explanation

**Context:**

> instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/package.scala; PR: INV-411: Add CRA validation logic for HK compliance

**Source-preserving request, proposal, or question:**

> I need these 2 extra fields on instrument. Ideally they should be required in HK context. Not sure how we want to proceed with this yet, I just add them as Optional field with default to None for now.
> 
> These will not affect SG, and we don’t have active trading flows in HK yet.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3245 · comment 326212223 · PR 4100 · 2022-08-26

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/package.scala`

**Evidence:** anon-2.jsonl:3245 · comment 326212223 · PR 4100 · 2022-08-26

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/package.scala`

**Explicit source context (hunk):**

> fundSmartCma: Boolean,
> -    tradability: Tradability = Tradability.BuySell
> +    tradability: Tradability = Tradability.BuySell,
> +    riskLevel: Option[Int] = None,
> +    isComplex: Option[Boolean] = None
>    )

## R-3352 — Last chance to extract PlanProfile together with this ProductLine into repository populated via TopicSubscriber directly, instead of going via entity…. Onc

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/events/events.scala; PR 3691: Merged in feat/SILVER-13762-ignore-charging-ai-fundsmart (pull request #3524)

**Source-preserving request, proposal, or question:**

> Last chance to extract PlanProfile together with this ProductLine into repository populated via TopicSubscriber directly, instead of going via entity….
> 
> Once the events are in prod, we will need to keep this class here, deprecated..

**Evidence:** anon-2.jsonl:3352 · comment 309905710 · PR 3691 · 2022-06-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/ces/events/events.scala`

## R-3394 — Old reports would not have fields for currencyBought and currencySold. And I don’t want them to be optional.

**Source stance:** open-question

**Context:**

> report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala; PR 3397: IAO fx-admin part 1

**Source-preserving request, proposal, or question:**

> Old reports would not have fields for currencyBought and currencySold. And I don’t want them to be optional.

**Evidence:** anon-2.jsonl:3394 · comment 295239688 · PR 3397 · 2022-04-18

Source path: `report-api/src/main/scala/com/endowus/silver/report/api/commons/statement/package.scala`

## R-3407 — We are still using transitional one today. So I keep the transitional one as is, and update this directly instead.

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepository.scala; PR 3265: IAO changes for FX admin

**Source-preserving request, proposal, or question:**

> We are still using transitional one today. So I keep the transitional one as is, and update this directly instead.

**Evidence:** anon-2.jsonl:3407 · comment 288546128 · PR 3265 · 2022-03-18

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepository.scala`

## R-3466 — Old transitional handler not removed yet

**Source stance:** observed-defect

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/cassandra/GoalDbHandlerTransitional.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Old transitional handler not removed yet

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3466 · comment 278834927 · PR 3029 · 2022-02-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/cassandra/GoalDbHandlerTransitional.scala`

## R-3467 — Rename from old transitional handler, hence there are 2 new columns here, instead of one. ‌

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/cassandra/PlanDbHandlerV4.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Rename from old transitional handler, hence there are 2 new columns here, instead of one.
> 
> ‌

**Evidence:** anon-2.jsonl:3467 · comment 278835541 · PR 3029 · 2022-02-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/cassandra/PlanDbHandlerV4.scala`

## R-3468 — Extracted `upsert` and `createTableIfNotExists` from existing `GoalJdbcRepositoryImpl`

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalJdbcDbHandler.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Extracted `upsert` and `createTableIfNotExists` from existing `GoalJdbcRepositoryImpl`

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3468 · comment 278835872 · PR 3029 · 2022-02-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalJdbcDbHandler.scala`

## R-3469 — Extracted `upsert` and `createTableIfNotExists` from existing `PlanJdbcRepositoryImpl`

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanJdbcDbHandler.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Extracted `upsert` and `createTableIfNotExists` from existing `PlanJdbcRepositoryImpl`

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3469 · comment 278836719 · PR 3029 · 2022-02-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanJdbcDbHandler.scala`

## R-3470 — New version of `PlanJdbcDbHandler` using new table definition `PlanTableV1`

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanJdbcDbHandlerV1.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> New version of `PlanJdbcDbHandler` using new table definition `PlanTableV1`

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3470 · comment 278836942 · PR 3029 · 2022-02-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanJdbcDbHandlerV1.scala`

## R-3471 — Almost identical to existing `PlanTable` except with `V1` and one new column for `preferences`

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanTableV1.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Almost identical to existing `PlanTable` except with `V1` and one new column for `preferences`

**Evidence:** anon-2.jsonl:3471 · comment 278837366 · PR 3029 · 2022-02-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanTableV1.scala`

## R-3472 — Old transition event processor not removed

**Source stance:** observed-defect

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/cassandra/GoalDbEventProcessorV5.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Old transition event processor not removed

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3472 · comment 278837450 · PR 3029 · 2022-02-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/cassandra/GoalDbEventProcessorV5.scala`

## R-3473 — Diff between `PlanDbHandler` \(current prod\) and `PlanDbHandlerV4` \(target state\) should only contain the new column `preferences`

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/cassandra/PlanDbHandlerV4.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Diff between `PlanDbHandler` \(current prod\) and `PlanDbHandlerV4` \(target state\) should only contain the new column `preferences`

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.

**Evidence:** anon-2.jsonl:3473 · comment 278837987 · PR 3029 · 2022-02-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/cassandra/PlanDbHandlerV4.scala`

## R-3474 — Renamed from existing old transitional event processor, hence contains more event changes. ‌ Diff between `PlanDbEventProcessor` \(current prod\) and `Plan

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/cassandra/PlanDbEventProcessorV4.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Renamed from existing old transitional event processor, hence contains more event changes.
> 
> ‌
> 
> Diff between `PlanDbEventProcessor` \(current prod\) and `PlanDbEventProcessorV4` \(target state\) only contains the version bump from v3 to v4

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.

**Evidence:** anon-2.jsonl:3474 · comment 278838414 · PR 3029 · 2022-02-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/cassandra/PlanDbEventProcessorV4.scala`

## R-3475 — Initial proposal keeps old Plan writes while a separate new Plan processor populates V1

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessor.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Existing `GoalJdbcEventProcessor` handles both goal and plan events to persist to JDBC - even though they are independent.
> 
> ‌
> 
> Keep `PlanJdbcDbHandler` in here so that it continue to populate existing table.
> 
> Add `PlanJdbcEventProcessor` handling only plan events, and persist via `PlanJdbcDbHandlerV1` to new table.
> 
> Once switch, we can remove plan events from `GoalJdbcEventProcessor`

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.

**Evidence:** anon-2.jsonl:3475 · comment 278839281 · PR 3029 · 2022-02-10

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessor.scala`

## R-3476 — Turned out `deactivatedAt` and `rebalanceRequest` are also missing. Added them here as well

**Source stance:** observed-defect

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/cassandra/PlanDbHandlerV4.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Turned out `deactivatedAt` and `rebalanceRequest` are also missing. Added them here as well

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.

**Evidence:** anon-2.jsonl:3476 · comment 279562543 · PR 3029 · 2022-02-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/cassandra/PlanDbHandlerV4.scala`

## R-3477 — Identical to `GoalTable` except for version bump. We want to ensure consistency between Goal and Plan tables, hence update them together in same JdbcEventP

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalTableV1.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Identical to `GoalTable` except for version bump. We want to ensure consistency between Goal and Plan tables, hence update them together in same JdbcEventProcessor

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.

**Evidence:** anon-2.jsonl:3477 · comment 279569847 · PR 3029 · 2022-02-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalTableV1.scala`

## R-3478 — Initial processor split is withdrawn so Goal and Plan update together for consistency

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessor.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> We no longer follow the above approach to split `GoalJdbcEventProcessor` into separate processors for Goal and Plan - because we want to update them together to ensure consistency \(e.g. avoid scenarios that we somehow update plans but not goals, and vice versa, due to some stuck event processor\)

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.

**Evidence:** anon-2.jsonl:3478 · comment 279569999 · PR 3029 · 2022-02-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessor.scala`

## R-3479 — Identical to `GoalJdbcEventProcessor` except using V1 DBHandler \+ V1 readsideId

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV1.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> Identical to `GoalJdbcEventProcessor` except using V1 DBHandler \+ V1 readsideId

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.
- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3479 · comment 279570105 · PR 3029 · 2022-02-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV1.scala`

## R-3480 — We also switch to use CassandraReadSide instead of SlickReadSide for the offsetstore for more reliability.

**Source stance:** requested-change

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV1.scala; PR 3029: SILVER-11092: Add missing columns in readside Plan tables

**Source-preserving request, proposal, or question:**

> We also switch to use CassandraReadSide instead of SlickReadSide for the offsetstore for more reliability.

**Conditions and limits:**

- PR3029 changes direction: the initial preferences-only and split-processor plan is corrected for missing fields and replaced with jointly updating Goal/Plan for consistency. Preserve the old-table/new-table and offset-store details as historical rollout choices. Source rows: anon-2.jsonl:3473, anon-2.jsonl:3474, anon-2.jsonl:3475, anon-2.jsonl:3476, anon-2.jsonl:3477, anon-2.jsonl:3478, anon-2.jsonl:3479, anon-2.jsonl:3480.

**Evidence:** anon-2.jsonl:3480 · comment 280376612 · PR 3029 · 2022-02-16

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/GoalJdbcEventProcessorV1.scala`

## R-3514 — Deployed to `staging` together with actual Factors changes. Created new goal / modified goal / invested new funding source, and observe no serdes error \(r

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 2979: SILVER-11940: Add new ProductLineAndIntent for Factors

**Source-preserving request, proposal, or question:**

> Deployed to `staging` together with actual Factors changes. Created new goal / modified goal / invested new funding source, and observe no serdes error \(related to goal\)
> 
> Kibana URL \(lots of filter because we have lots of other noises\)
> 
> ```
> <url>
> ```
> 
> ![](<url>
> ‌

**Evidence:** anon-2.jsonl:3514 · comment 277347036 · PR 2979 · 2022-02-04

## R-3517 — Added `Deleted` to the cases in `deleteRelatedTransaction` I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state

**Source stance:** reported-verification

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/common/DividendDeleter.scala; PR 2835: SILVER-11314: Fetch DividendState from entity before deleting to handle lag between DividendJdbcEventProcessor and DividendEventProcessor

**Source-preserving request, proposal, or question:**

> Added `Deleted` to the cases in `deleteRelatedTransaction`
> 
> I see `DeleteCmd` is already handled correctly by the entity if in `Deleted` state

**Evidence:** anon-2.jsonl:3517 · comment 272457921 · PR 2835 · 2022-01-13

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/common/DividendDeleter.scala`

## R-3522 — Migration transactionDate pdd.createdAt differs from subscriber payoutDate at SGD start of day

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/package.scala; PR 2298: Feat/SILVER-9365

**Source-preserving request, proposal, or question:**

> [incidental identifier omitted] Sorry to dig this up. Is this a bug or intended that we set `transactionDate = pdd.createdAt` here which will be used for state \+ event migration
> 
> While we would set `transactionDate = ZonedDateTime.from(msg.payoutDate.atStartOfDay(TimeUtils.sgdTimeZone))` for in `PlanDividendDistributionTopicSubscriber`

**Conditions and limits:**

- PR2833 preserves separate historical migration, Confirmed-only sync, date/timestamp meanings, and optional-field alternatives. Naming evolves through priceDate to settlementDate. The final comment defers optional-forever versus mandatory-plus-migration to a later decision. Source rows: anon-2.jsonl:3522, anon-2.jsonl:3523, anon-2.jsonl:3524, anon-2.jsonl:3525, anon-2.jsonl:3526, anon-2.jsonl:3527, anon-2.jsonl:3528, anon-2.jsonl:3531, anon-2.jsonl:3533, anon-2.jsonl:3535, anon-2.jsonl:3536, anon-2.jsonl:3537, anon-2.jsonl:3538.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3522 · comment 274265217 · PR 2298 · 2022-01-21

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/package.scala`

>  Sorry to dig this up. Is this a bug or intended that we set `transactionDate = pdd.createdAt` here which will be used for state \+ event migration
> 
> While we would set `transactionDate = ZonedDateTime.from(msg.payoutDate.atStartOfDay(TimeUtils.sgdTimeZone))` for in `PlanDividendDistributionTopicSubscriber`

## R-3526 — As I understand that field `settlementConfirmation` was introduced only in Income P1 and we didn’t patch old dividends that were auto-reinvested by uobkh

**Source stance:** explanation

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/common/ReinvestedDividendDataSyncHelper.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> As I understand that field `settlementConfirmation` was introduced only in Income P1 and we didn’t patch old dividends that were auto-reinvested by uobkh

**Conditions and limits:**

- PR2833 preserves separate historical migration, Confirmed-only sync, date/timestamp meanings, and optional-field alternatives. Naming evolves through priceDate to settlementDate. The final comment defers optional-forever versus mandatory-plus-migration to a later decision. Source rows: anon-2.jsonl:3522, anon-2.jsonl:3523, anon-2.jsonl:3524, anon-2.jsonl:3525, anon-2.jsonl:3526, anon-2.jsonl:3527, anon-2.jsonl:3528, anon-2.jsonl:3531, anon-2.jsonl:3533, anon-2.jsonl:3535, anon-2.jsonl:3536, anon-2.jsonl:3537, anon-2.jsonl:3538.

**Evidence:** anon-2.jsonl:3526 · comment 272765962 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/common/ReinvestedDividendDataSyncHelper.scala`

## R-3527 — I mark this deprecated, and will remove after we verify everything is fixed in prod. For same reason, I will reuse existing `DividendReinvestedEvt` since t

**Source stance:** requested-change

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendServiceImpl.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> I mark this deprecated, and will remove after we verify everything is fixed in prod.
> 
> For same reason, I will reuse existing `DividendReinvestedEvt` since this is only temporary.
> 
> We can consider adding an OverrideDividendStateEvt in future, if the need to sync with Investment service comes back. But then, we should implement all cases properly, rather than just Reinvested state

**Conditions and limits:**

- PR2833 preserves separate historical migration, Confirmed-only sync, date/timestamp meanings, and optional-field alternatives. Naming evolves through priceDate to settlementDate. The final comment defers optional-forever versus mandatory-plus-migration to a later decision. Source rows: anon-2.jsonl:3522, anon-2.jsonl:3523, anon-2.jsonl:3524, anon-2.jsonl:3525, anon-2.jsonl:3526, anon-2.jsonl:3527, anon-2.jsonl:3528, anon-2.jsonl:3531, anon-2.jsonl:3533, anon-2.jsonl:3535, anon-2.jsonl:3536, anon-2.jsonl:3537, anon-2.jsonl:3538.

**Evidence:** anon-2.jsonl:3527 · comment 272781190 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendServiceImpl.scala`

## R-3531 — Hypothetical V0/V1/V2 optional-to-mandatory dividend field migration paths

**Source stance:** suggestion

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendJsonSerializerRegistry.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> As I understand, old events will never have these new fields, optional or not.
> 
> So if we go with Optional, we would have:
> 
> * V0: no new field
> * V1: new fields but Optional - no need migration step, since they are populated to None by default
> * V2: new fields but mandatory \(it does not make sense to keep them optional forever\). So V0 and V1 events will both need migration step for them
> 
>     * V0 events will need “magic” values
>     * V1 events will just unwrap the Option
>     
> 
> Please correct me if I’m wrong here :pray: 
> 
> ‌

**Conditions and limits:**

- PR2833 preserves separate historical migration, Confirmed-only sync, date/timestamp meanings, and optional-field alternatives. Naming evolves through priceDate to settlementDate. The final comment defers optional-forever versus mandatory-plus-migration to a later decision. Source rows: anon-2.jsonl:3522, anon-2.jsonl:3523, anon-2.jsonl:3524, anon-2.jsonl:3525, anon-2.jsonl:3526, anon-2.jsonl:3527, anon-2.jsonl:3528, anon-2.jsonl:3531, anon-2.jsonl:3533, anon-2.jsonl:3535, anon-2.jsonl:3536, anon-2.jsonl:3537, anon-2.jsonl:3538.

**Evidence:** anon-2.jsonl:3531 · comment 272793495 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/DividendJsonSerializerRegistry.scala`

## R-3533 — That’s right, but event processor would still retry \(and fail\) until all pods are successfully deployed.

**Source stance:** observed-defect

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/ces/DividendEvents.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> That’s right, but event processor would still retry \(and fail\) until all pods are successfully deployed.

**Conditions and limits:**

- PR2833 preserves separate historical migration, Confirmed-only sync, date/timestamp meanings, and optional-field alternatives. Naming evolves through priceDate to settlementDate. The final comment defers optional-forever versus mandatory-plus-migration to a later decision. Source rows: anon-2.jsonl:3522, anon-2.jsonl:3523, anon-2.jsonl:3524, anon-2.jsonl:3525, anon-2.jsonl:3526, anon-2.jsonl:3527, anon-2.jsonl:3528, anon-2.jsonl:3531, anon-2.jsonl:3533, anon-2.jsonl:3535, anon-2.jsonl:3536, anon-2.jsonl:3537, anon-2.jsonl:3538.

**Evidence:** anon-2.jsonl:3533 · comment 272794260 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/ces/DividendEvents.scala`

## R-3538 — Final optional event fields defer optional-forever versus mandatory-plus-migration choice

**Source stance:** requested-change

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/ces/DividendEvents.scala; PR 2833: SILVER-11229: Fix settlement date for dividend reinvestment

**Source-preserving request, proposal, or question:**

> All new fields are now optional in events, hence all JsonMigration steps are removed.
> 
> We can:
> 
> A. Keep them optional forever to correctly reflect the event history, i.e. they are indeed new fields that were added at some point of time.
> 
> B. Make them mandatory \+ add back the migration step to provide default value in separate release
> 
> ‌
> 
> \(A\) would force new event processors to think and handle them, since all events will be re-processed by them. They might fallback to default values, or not. \(A\) give them an obligation to handle, but a choice to choose.
> 
> \(B\) effectively forces all new event processors to follow the default value via the serializer.
> 
> ‌
> 
> Making them optional now defer the decision of choosing \(A\) or \(B\) of out scope of this PR.

**Conditions and limits:**

- PR2833 preserves separate historical migration, Confirmed-only sync, date/timestamp meanings, and optional-field alternatives. Naming evolves through priceDate to settlementDate. The final comment defers optional-forever versus mandatory-plus-migration to a later decision. Source rows: anon-2.jsonl:3522, anon-2.jsonl:3523, anon-2.jsonl:3524, anon-2.jsonl:3525, anon-2.jsonl:3526, anon-2.jsonl:3527, anon-2.jsonl:3528, anon-2.jsonl:3531, anon-2.jsonl:3533, anon-2.jsonl:3535, anon-2.jsonl:3536, anon-2.jsonl:3537, anon-2.jsonl:3538.

**Evidence:** anon-2.jsonl:3538 · comment 272855156 · PR 2833 · 2022-01-14

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/entities/dividend/ces/DividendEvents.scala`

