# Slick, PostgreSQL, Cassandra, keys, queries, and indexes

360 source-specific cases. Statements retain their historical scope and source stance. Read related PR cases for corrections or alternatives.

## Cases

- A1-0006 — OrderTableV8 new column requires ALTER TABLE ADD COLUMN
- A1-0011 — Remove code in CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4
- A1-0014 — Assessment history PK is customerId and lastUpdatedTS
- A1-0016 — CRA snapshot stores queryable derived columns while history updates only advisoryProfile
- A1-0018 — CRA history does not update by lastUpdatedTS alone
- A1-0019 — CRA snapshot updates explicit columns to exclude complex product acknowledgement
- A1-0435 — Lookup plan by PK planId then validate customerId
- A1-0456 — CustomerId PK prevents duplicate fee profile; change collection type to Set
- A1-0460 — Distinguish true date from timestamp in PRP annotation mapping
- A1-0487 — Resolved Cassandra profiles override apparent LOCAL_ONE with LOCAL_QUORUM on Astra
- A1-0488 — Extracted basic.graph configuration redundant because DSE-only
- A1-0489 — Lagom to Alpakka Cassandra migration hid changed session configuration path
- A1-0552 — Fetch monthly returns from DB rather than entity
- A1-0812 — Tag filter may ignore condition and include empty tags
- A1-0813 — Reuse optional(t.name,op,value)(stringIsOrIlike) for Option[String]
- A1-0815 — inSetBind already handles empty set
- A1-0817 — Test empty inSetBind returning false
- A1-0820 — Separate EventTagRecordInput without ordering from required-ordering select record
- A1-0822 — Slick insert projection takes EventTagRecordInput and returns generated ordering
- A1-0943 — Compiler warning finds map/flatMap bug mixing DBIO and Future
- A1-1047 — Stream DB once and loop locales inside; otherwise mapAsync(1)
- A1-1053 — Stream templates before locales and validate tags without collecting
- A1-1066 — Stream outside locale so query once like advisory
- A1-1069 — Timestamp still required because TTL cannot apply to Cassandra key columns
- A1-1070 — Use Cassandra materialized view instead of high-cardinality index
- A1-1072 — Monitor query performance and tombstone metrics
- A1-1074 — Partition key is entity_type and entity_id
- A1-1075 — Compare per-version timestamp PK with per-entity TTL upsert
- A1-1076 — Tune compaction and gc grace for TTL usage
- A1-1297 — Force revoke uses deleteRequest matching stale lock
- A1-1302 — Normal release must match original lock request
- A1-1400 — Empty journal partition returns empty instead of throw
- A1-1401 — Refactor TypedEventDao query resolution by optional from/to
- A1-1402 — Compare range with partition lowest sequence rather than1
- A1-1403 — Correction: sequence numbers do not reset per partition
- A1-1404 — Use inclusive range partition logic consistently with minus one
- A1-1405 — requestedTo equal partition size belongs partition0
- A1-1503 — Portfolio repository queries PK portfolioId; validate tenant outside
- A1-1600 — Store trading accounts Set instead of composite-key account component
- A1-1601 — What lookup use case requires account
- A1-1602 — Group portfolios need mapping support too
- A1-1605 — Portfolio assignment table only mapping; Explore visibility elsewhere
- A1-1606 — Specify both tenant and group mapping design
- A1-1608 — Move bulkUpsert into DbHandler; single upsert may be unnecessary
- A1-1609 — Repository findByTenantId/findByGroupId hide principal type
- A1-1610 — PK portfolioId and index ownerId to enforce one owner
- A1-1611 — Can concatenate principal type and ID into one column
- A1-1612 — PrincipalId-only index may suffice versus composite
- A1-1698 — Option-returning query uses take(1) LIMIT1 even if PK already unique
- A1-1719 — Use take(1).result.headOption
- A1-1736 — Readside may need one source-target pair rather than duplicate In/Out schedules
- A1-1737 — Goal recurring-transfer table purpose unclear because trading triggers daily transfers
- A1-1817 — Delete charge rows in bounded batches within one stream
- A1-1818 — Sorted stream plus in-memory groupBy documented; raw SQL still considered
- A1-1820 — Pod waits index drop/create before joining cluster
- A1-1861 — Daily data per instrument/date row instead of growing JSONB
- A1-1862 — Choose numeric decimal precision explicitly
- A1-1864 — Configure precision before MStar sends more dp
- A1-1867 — missingDates collection may OOM; use filterOpt date predicate
- A1-1869 — Latest-date query or DB join/stream instead of per-row lookup
- A1-1870 — Remove Cassandra PortfolioRepository after PG migration
- A1-1878 — streamAll directly from DB instead of memory-loaded stream
- A1-1911 — Query manual prices in PG instead of loading all in memory
- A1-1914 — Question need for declaration not persisted as separate column; exact field unspecified
- A1-1924 — Extract JSON path priceSource _type via #>> List
- A1-1937 — Transaction updated_at uses Instant rather than ZonedDateTime
- A1-2002 — Use RebalancePlan repository streamActivePlansByPortfolioId with effectiveDate
- A1-2020 — Explicit instrumentId query instead of per-instrument unindexed scan
- A1-2023 — Use insert not insertOrUpdate to catch initial-state race
- A2-0028 — PlanProfileJdbcProjectionV3: Since we have the full PlanProfile in the `PlanProfileTenantIdBackFilledEvt`, let’s use it directly instead of fetching from entity again.
- A2-0029 — FeeChargeRequestJdbcProjectionV6: I think we can let DB take care of both the query and update. Something like `UPDATE feeChargeRequests SET tenantId WHERE customerId, planId`
- A2-0030 — FeeChargeRequestJdbcProjectionV6: There’s no need to query this anymore. The `updateTenantId` takes care of all requests with matching customerId/planId
- A2-0031 — BackfillPlanProfileTenantIdTaskTopicSubscriber: I realize we could have made the task keyed by customerId instead, then in this subscriber, we query planProfiles by customerId a...
- A2-0033 — CommunicationContext: These default fallback looks wrong. Since in theory we can’t reliably fallback without locale \(or TranslationContext\)
- A2-0062 — TagTransactionAdvisoryClassification: So why don’t we just start with endpoint that queries v3 repo directly? Why do we query v2 repo, then query again with v3?
- A2-0076 — FixV3DividendsTransactions: Let’s also add which query we use to arrive at the dataset
- A2-0078 — FixV3DividendsTransactions: Why don’t we add more filter here, to reduce the payload size? Also maybe groupBy customerId so that we don’t repeat the query again?
- A2-0190 — BffServiceE4s: Can merge `getGoalCreateTasksByCreatorPendingManager` and `getGoalCreateTasksByCreatorPendingClient` by making FE send `assigneeRole` as query param
- A2-0230 — RebalancePlanTableV4: Remove all the index on customerId/goalId/tradingAccountType/planCcy - we don’t use them at all.
- A2-0236 — InvestmentPlanTableV8: This index is too much I would think. So most of the use cases of recurring investment, I think index on the `NextUpcomingDate` is sufficient. Other condi...
- A2-0237 — GoalTableV4: Do we need all these colums?
- A2-0282 — PlanFeeInstructionEntity: The entity state is default with empty fee instructions, it means the plan always exists, just without any data. Modelling it this way means you can’t ...
- A2-0284 — TenantFeeRangeConfigHistoryTable: Let’s just store jsonb `FeeRange` for history as well?
- A2-0285 — TenantFeeRangeConfigDaoJdbc: Do we need to capture “deleted-by” in the `lastUpdatedBy` field?
- A2-0299 — Review: Reported config-endpoint verification: cassandra-query-journal/events-by-tag/eventual-consistency-delay returned 20s before the environment override and 7s afterward. Po...
- A2-0312 — RecurringInvestmentScheduleHistoryDataEventProcessorV3: Maybe we check w data team on this table is used? I’m not sure about adding another row to history entries when backfilli...
- A2-0313 — RecurringInvestmentScheduleHistoryDataEventProcessorV3: `PlanRecurringInvestmentScheduleHistoryTableV3` stores the history audit entries, so we can’t rely on this backfill evt t...
- A2-0339 — GoalSupportingDataTableV1: How does this work when there are multiple actions on a goal?
- A2-0346 — GoalEventProcessor: We split new projection, inject `WorkflowEngineServiceSg` and wire it only for SG
- A2-0347 — GoalSupportingDataTableV1: `GoalActionContext` covers `CREATION_APPROVED, MODIFICATION_APPROVED` which is initiated from goal svc
- A2-0350 — GoalSupportingDataTableV1: Needs to be composite \(`goalId`, `goalActionContext`, `createdAt`\)
- A2-0358 — GoalSupportingDataTableV1: Let’s try auto increment id and index on goalId
- A2-0365 — GoalSupportingDataJdbcDbHandler: I suppose this would return 0, if row already exists? Do we log error or something cuz we don’t expect that to happen?
- A2-0367 — GoalSupportingDataJdbcDbHandler: Need index on goalId?
- A2-0371 — InstrumentBalanceRepository: ```
- A2-0414 — BaseAdvisoryServiceE4s: Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for c...
- A2-0435 — Review: How to persist documentIds for goal? One approach could be below \(we can review again later\)
- A2-0469 — BffServiceImpl: In on-behalf operations:
- A2-0476 — BffServiceImpl: Ok so my above example would be when FA performs operation on-behalf of customer, so employee would be there.
- A2-0484 — PortfolioStatsJdbcTable: I don’t create these index in V2:
- A2-0489 — HkAdvisedPortfolioOfferingsManager: Let’s set effectiveDate as well, for all these query using portfolioId
- A2-0559 — DistributionCalculatorHelperHk: Pagination will actually run the query twice \(count and actual result\). Best if we simply add an endpoint for this
- A2-0594 — MstarDailyPerformance: The `<currency>` should always be there, cuz it’s data. If that is missing, then sth is wrong w MStar
- A2-0609 — InstrumentMStarDataJdbcDbHandler: In this pattern, the dbHandler should be the one incrementing the version, and outer logic can consider only actual data change
- A2-0610 — ServiceLogicImpl: I mean move this outside too. No need to bulkUpsert this for every ccy cuz this table doesn’t care about marketCcy
- A2-0611 — InstrumentMStarDataJdbcDbHandler: This should be `expectedPreviousUpdatedTimestamp`
- A2-0663 — ProductPortfolioRepository: Nit: can move a little closer to this method so that they stay in pair \(similar to those with stockRatio\)
- A2-0696 — Review: Since we do not support topping up unit dividend on top of existing \(cash or unit\) dividend at all, let’s also check the trigger endpoint of unit dividend, and add que...
- A2-0697 — InstrumentPortfolioSubscribersDataRepository: Let’s do Source because this List will grow for popular instrument
- A2-0700 — PortfolioMonthlyChangesHelper: Let’s move to pg for this readside, using IN across partition in cassandra is dangerous
- A2-0709 — InstrumentPortfolioSubscribersDataTable: Instant requested; exact field unavailable
- A2-0711 — PortfolioMarketDataEventProcessor: Let’s move this to PortfolioTopicSubscriber. Eventually we should also handle `ModelPortfolioDeactivatedMsg` and delete from repo
- A2-0716 — PortfolioMonthlyChangesDataTable: Instant
- A2-0718 — PortfolioMonthlyChangesHelper: I think there are 2 types of race conditions we might see here:
- A2-0720 — InstrumentMonthlyChangesJdbcRepository: Maybe Set for instruments
- A2-0721 — package: Let’s add updatedAt instant here, and use for both model and db. No need to split cuz we have single source that is the db
- A2-0724 — PortfolioMonthlyChangesJdbcHandler: This should be set by caller
- A2-0729 — PortfolioMonthlyChangesJdbcRepository: just `find`
- A2-0730 — InstrumentMonthlyChangesJdbcRepository: Move filter up, and select specific columns
- A2-0737 — InstrumentPricesJdbcHandler: Just instrumentId and priceCcy right? Also let’s assert `data` has same instrumentId and priceCcy
- A2-0741 — InstrumentMonthlyChangesJdbcRepository: map first, then just need `.distinct`
- A2-0742 — InstrumentMonthlyChangesJdbcRepository: Maybe rename:
- A2-0788 — InstrumentPortfolioSubscribersDataRepository: Let’s not put repository yet in this PR. Do join between this and mc table so we can dedupe in DB
- A2-0789 — InstrumentPriceTable: `(instrumentId, priceCcy, priceDate)`
- A2-0792 — InstrumentPortfolioSubscribersDataJdbcHandler: Take VO instead of individual fields. Set updatedAt outside
- A2-0793 — InstrumentMarketDataJdbcProjection: Consider skipping old events, and sync to db separately to save cost processing old events we don’t care
- A2-0796 — InstrumentPortfolioSubscribersDataRepository: Just `streamInstrumentPortfolioSubscribers` ?
- A2-0799 — InstrumentMonthlyChangesJdbcRepository: We don’t need the monthly changes in the result of this query? Otherwise this query is still n\*m.
- A2-0821 — ProductPortfolioRepository: Maybe we can keep this method generic, but only handle for CoreEnhanced for now…
- A2-0837 — ProductPortfolioRepository: On 2nd thought, I suppose for other productlines, we can simply check against `ProductPortfolio.riskTarget`. Then this impl will be complete
- A2-0924 — FeeManager: As discussed, let’s try to refactor and move this decision to outer level \(similar to fee estimation query\), cuz we already have all the planProfiles and customerI...
- A2-0925 — CustomerFeeQueryService: This query service is used for both the notification and admin. Maybe we want to add flag such that admin can estimate the fee but notification won’t send?
- A2-0942 — FeeChargeRequestJdbcRepository: Looks like we also need to upversion this table to add new column for skip details? I suppose for immediate data query needs, we can safely rely ...
- A2-0944 — FeeChargeRequestJdbcRepository: We also need to handle the skipped event in `FeeChargeRequestJdbcProjectionV6`
- A2-0970 — NonAltsFeeManager: There’s a small performance boost here cuz [person] queries tradable-goals by customerId first, and we only care about checking TAA if a plan does not exist i...
- A2-0978 — ServiceLogicImpl: This logic actually works for 1st time trigger too. Maybe we just rename, accept `requestedBy` and `reason` as query params, so we can use in both places?
- A2-1021 — BaseGoalService: Can we remove this param `status`…. currently logic only supports query live or all status… and why would a goal be tradable if it’s not live…
- A2-1050 — GoalBasedStatementInfoDbDto: I’m not sure if we need all these new fields in `*DbDto`. As I understand, these DTO are persisted and used to check if a statement is reprint or not.
- A2-1061 — GoalBasedStatementInfoDbDto: Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.
- A2-1066 — GoalBasedStatementInfoDbDto: Let’s add these fields into the list of data-loss fields in the comment in `GoalBasedStatementPageDataDbDto`, together with explanation, e.g. isDpm ...
- A2-1097 — InstrumentJdbcEventProcessor: Let’s use Cassandra projection manager?
- A2-1098 — Instrument JDBC processor naming: InstrumentV2JdbcEventProcessorV7
- A2-1139 — package: Do we need this case class? Let’s just use query params?
- A2-1168 — PortfolioVersionUpgradeRebalanceRequestsGenerator: Let’s log the `tradingRestrictions` here so we can query for more details if needed
- A2-1176 — Review: That would be next step. Need to check w PM regarding where to store, and the query requirement for it. Likely we just need to stamp in productLineAndIntent… and build h...
- A2-1233 — Review: Oh I didnt realize we already released on `trading` svc side… I guess it’s not worth the effort to rename and bump new table version for everything :sweat_smile:
- A2-1235 — InvestmentRequestTopicSubscriberV3: There can be eventual consistency delay here no? So might end up with stale version of transaction in the repository
- A2-1242 — InvestmentPlanTableV6: FYI, there’s a bug with V6. We will release V7 soon….
- A2-1301 — InvestmentPlanTableV7: Maybe just `schedule.map(s => s.fundingInstructions.getOrElse(PlanAccountPlanFundingInstructions(s.investmentAmount)))`
- A2-1303 — HkAdvisedPortfolioMaaManager: Yea this is existing. portfolio-offerings will be used during add goal / modify goal flow, and we show in portfolio ccy there.
- A2-1309 — AuroraJdbcSchema: keep the `v6` so it’s not confusing when we add v7
- A2-1353 — RebalanceRequestJdbcRepositoryImpl: Let’s just import `import com.endowus.silver.rebalance.impl.db.RebalancePostgresProfile.api._` ?
- A2-1360 — MarketDataUploader: I suppose it’s also good to log for prices we have in our DB but not in MStar.
- A2-1365 — MarketDataUploader: Don’t we need to include `startDate` in this method? Otherwise we will have lots of warn log complaining missing price in MStar, since we compare limited MSt...
- A2-1375 — MarketDataUploader: I think this cassandra table already have priceDate in its clustering key. We should be able to add a method in repository to filter in database itself
- A2-1379 — InstrumentPriceRepository: Let’s just add an overloading of existing `retrievePrices` that takes required `startDate`. Then we can leave to caller to decide which one to call?
- A2-1409 — JdbcSchema: Maybe change this to follow the new pattern in which we have separate DbHandler class supporting createTable/upsert/delete and Repository class supporting queries
- A2-1410 — JdbcSchema: Otherwise, if you don’t want to change too much in this PR, let’s just use `ProductPortfolioJdbcRepository#createTable` here?
- A2-1417 — PortfolioSuitabilityAnalysisResponse: Let’s just match by index or use id in a Map instead of new response type
- A2-1425 — PortfolioSuitabilityAnalysisLogic: We should be able to query CRA profile and extract this once for whole input, instead of doing this every batch?
- A2-1439 — BaseServiceLogicImpl: Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless
- A2-1454 — Review: Can we also delete the cassandra readside \+ projection too :pray:
- A2-1457 — PlanRecurringInvestmentScheduleHistoryTableV3: Actually for these tables, we should just drop `investmentAmount` and make `fundingInstructions` required column?
- A2-1458 — PlanPostgresProfile: just `fundingInstructionsMapper`
- A2-1460 — Review: HK model portfolios are updated more frequently I think, so better to let POps and IO know to stop until we finish migrating data \+ switch the repository
- A2-1487 — Review: Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)
- A2-1511 — BrokerAccountDividendDataTable: Missing table name?
- A2-1513 — RedemptionPlanJdbcDbHandlerV3: Can you help me extract const for these 2 indices too :pray:
- A2-1514 — RedemptionPlanTableV3: Not sure why we didn’t just key by planId… and if we already have composite key like this, we don’t need additional index for customerId / planId… but thi...
- A2-1515 — RedemptionRequestJdbcDbHandlerV3: Can you help me rename this to V4 as well?
- A2-1538 — HkAdvisoryService: These should be named `locale` to match the query parameter too?
- A2-1542 — InstrumentTopHoldingsCache: Why don’t we follow same pattern as other caches here? Just take locale as query input instead? I suppose we might eventually have localisation suppo...
- A2-1554 — RebalanceRequestTable: We missed a `v` for version here, but it’s consistent in V4 too :sweat_smile: we will change this when we upversion  this table again in future
- A2-1566 — TransactionJdbcProjectionV2: Let’s not mix the naming, it can be confusing for future readers:
- A2-1567 — TransactionJdbcProjectionV2 dependency name: transactionJdbcRepositoryV2
- A2-1569 — JdbcSchema: You still need to create V2 and V1\_3 until we completely remove the 2 projections right? Otherwise this will scream if we deploy to new dynamic env \(or if it’s res...
- A2-1576 — RebateDistributionRequestJdbcRepository: We should just move this to `queryRequestsForPeriod`? Then you don’t need the zeroRebateCount
- A2-1580 — RebateDistributionRequestJdbcRepositoryTest: Is it duplicate test? It’s not mockDb btw, it’s real embedded pg
- A2-1583 — InstrumentState: Didn’t realize we are using same model in state and db… it should be cheap enough to convert back to DTO and use all the existing methods there?
- A2-1596 — RebateDistributionRequestJdbcRepository: This should be named `queryRequestsForPeriod`? Also let’s reuse it for all the methods here?
- A2-1597 — RebateDistributionRequestTable: Nit: no need `table` in table name
- A2-1598 — RebateDistributionRequestTable: This table can get quite large. I’m not sure if using so many columns in composite key would have significant performance impact or not, as compa...
- A2-1599 — RebateDistributionSummaryTable: Nit table name
- A2-1614 — RebateDistributionRequestJdbcRepository: Use `queryRequestsForPeriod` here too?
- A2-1620 — RebateDistributionCommunicationsManager: Each customer wouldn’t have too many trailer rebates per quarter, so I suppose it’s ok to run this aggregation in memory. But we potenti...
- A2-1624 — InstrumentTable: [person] [person] let’s create tix, if not already, to completely get rid of V1 instrument repository \+ its entity later
- A2-1630 — Review: * advisory.corporate\_customer\_v2
- A2-1639 — RegionalCustomerTopicCustomer: Btw should we use jdbc readside instead? Eventually we want to get rid of these cassandra readside for general query needs
- A2-1658 — SgAdvisoryLevelClassificationLogic: Should be fast enough cuz compliance won’t need to make any additional lookup or db call. Inter-service calls should be fast within the k8s c...
- A2-1683 — GoalNameSuggestionHelper: Pending confirmation from [person] on the translation. [person] can you help to move this to cache/db lookup in your PR :pray:
- A2-1693 — JdbcSchema: Hmm this looks weird. Ideally we want this `TemplateJdbcDbHandlerV4` injected, or move the `createTableIfNotExists` to its companion object. And templateV4 should be...
- A2-1706 — AuroraJdbcSchema: Can we change to use
- A2-1711 — CustomerAdvisoryProfileJdbcEventProjectionV2: Yea this should give us zero impact for now, cuz we don’t expect `ExpiryDateOverriddenEvt` or `CraExpiredEvt` in prod yet. And data...
- A2-1712 — RebalanceApplication: Can you help to put a comment here to remind us about the mismatch between table version and readside version, to avoid future confusion :pray:
- A2-1713 — RebalanceApplication: Actually do we need a new `AuroraJdbcSchema` that doesn’t take in `planMarketValueJdbcHandler` and `rpcCommunicationDetailsJdbcRepository` as we haven’t mi...
- A2-1714 — RebalanceApplication: So here we are using same class JdbcSchema for both gcpcloud and aurora. It has `planMarketValueJdbcHandler` and `rpcCommunicationDetailsJdbcRepository`, w...
- A2-1715 — AuroraJdbcSchema: Ah yes, creating them as empty is ok. My previous comment was in context of either the repository or the dbHandler having injected database.
- A2-1723 — InvestmentRequestJdbcDbHandler: Yea this is just direct copy paste from the old InvestmentRequestJdbcRepository. I didn’t bother cuz we will remove it soon, once data side has s...
- A2-1725 — InvestmentRequestJdbcRepository: Hmm status filter is behaving same as before. I just move the createdAt check to logic layer, cuz we need to check cutOffDate first.
- A2-1727 — InstrumentHoldingDaoJdbc: Yea as we checked, Slick insertOrUpdateAll will always upsert and return the batch size
- A2-1737 — ServiceLogicImpl: Not really, but since I query plan here, I thought I might as well check. We need to add similar check to advisory ProductLine manager too, another PR
- A2-1743 — Review: We can put new optional field in domain, and required field in DTO. And map in the from/toDto methods? No need migration or anything.
- A2-1779 — ServiceLogicImpl: I think the intention was to dump all current data into repository, without having to process every event, cuz we only care about last value of each price date.
- A2-1780 — ServiceLogicImpl: We can already trust data from this repo, no need to go entity if repo says no annual yield
- A2-1793 — TemplateData: Yes, I haven’t upversioned and switched to aurora config yet so put the fallback here so that it can work with v3 table :see_no_evil:
- A3-0001 — InstrumentMstarData JSONB, instrumentId-only lookup, cron sync and annual-yield API transition
- A3-0005 — InstrumentMStarAddMarketDataTable.scala: DTO is flat with bunch of optional fields. DB doesn’t have to be
- A3-0006 — InstrumentMStarAddMarketDataTable.scala: Miscomm then lol. I guess because you wanted to update annual yield via processor?
- A3-0008 — InstrumentMstarDataVo.scala: We don’t need this VO right? Just store `InstrumentMstarData` directly
- A3-0009 — MarketdataPostgresProfile.scala: Can remove this one
- A3-0012 — InstrumentMstarDataVo.scala: You still can use multiple columns extracting data from `InstrumentMstarData`. But ok it doesn’t matter. I guess we also have this \*VO / \*Data in ot
- A3-0023 — InstrumentV2JdbcRepository.scala: So we change this back to exact match rather than contain?
- A3-0025 — InstrumentJdbcEventProcessorV2.scala: follow the pattern we have in other services with JdbcSchema
- A3-0026 — InstrumentV2JdbcDbHandler.scala: We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed
- A3-0027 — InstrumentJdbcEventProcessorV2.scala: It’s just a bit cleaner to group them together, both those with event processor and those pure CRUD
- A3-0028 — InstrumentDbEventProcessorNew.scala: we can remove already. BQ is currently using pg instruments\_v4
- A3-0032 — DailyMvAuditEntry array_agg/customerId optimization deferred over Slick GROUP BY issues
- A3-0033 — DailyMvPersistenceHelper.scala: Extract this logic out of `PlanTimeSeriesTopicSubscriber` and let it handle updating both dailyMV and dailyMVAuditEntry tables
- A3-0038 — DailyMvAuditEntryJdbcRepository.scala: good point. I’ll add feeType column to this instead
- A3-0039 — DailyMvPersistenceHelper.scala: Can. This cache is very small anyway. I’ll put a month?
- A3-0040 — BaseServiceLogicImpl.scala: Good catch. Let me just handle empty MV inside batchUpsert then
- A3-0041 — DailyFeeCalculationManager.scala: ok. Will oso clean up fees older than business date cutoff :thumbsup:
- A3-0042 — InstrumentTable.scala: maybe change this as tableNamePrefix and use it below?
- A3-0116 — RPC endpoints intentionally differ: customer readside versus goal entity consistency
- A3-0124 — ServiceLogicImpl.scala: We have utils in OptionUtils so this can be written as ``` rpcCmsWebflowIdJdbcRepository .find(portfolioId, effectiveDate) .map(_.map { entry => RpcCm
- A3-0125 — ServiceLogicImpl.scala: Same here, you don’t need to match. Can extract to reuse same toDto method as well ``` rpcCmsWebflowIdJdbcRepository .findByItemId(itemId) .map(_.map(
- A3-0127 — RebalanceService.scala: Should we query by collectionId \+ itemId then, as I understand this is composite key from Webflow?
- A3-0221 — InstrumentDailyReturnIndexDaoJdbc.scala: Change this so that we actually test the clause limit in test
- A3-0254 — PlanRecurringInvestmentScheduleTable.scala: Do we need to key on all 3? Just planId?
- A3-0256 — Schedule history without key duplicates on event retry
- A3-0257 — RecurringInvestmentScheduleJdbcEventProcessor.scala: `upsertPlanRecurringInvestmentSchedule` will skip if schedule is None? don’t we need another method to delete in dbHandler?
- A3-0258 — PlanRecurringInvestmentScheduleJdbcRepositoryImpl.scala: So we want to support 2 modes of query? 1. query by expiry date \(don’t care how it expires, either explicit date or occurrence count\) 2. query by ex
- A3-0259 — : Can we add tests too please, for both processor and repository
- A3-0261 — PlanRecurringInvestmentScheduleTable.scala: Note: No need index on PlanId if it’s pk
- A3-0262 — RecurringInvestmentScheduleJdbcEventProcessor.scala: I’m now thinking we should add composite key using combination of fields… updatedAt should definitely part of that
- A3-0263 — Schedule deactivation domain events belong in command/PlanProjection; JDBC writes only
- A3-0264 — Mutable endingOnDate/toBeExpiredOn indices: catch up projection before adding indices
- A3-0265 — UpdatedEvt old/new inserts and offset-commit failures: duplicate windows and PK alternatives
- A3-0267 — RecurringInvestmentScheduleJdbcEventProcessor.scala: In theory again, since we don’t actually care about this table from application side, we should just add another topic producer that re-publish all me
- A3-0319 — Schedule history created/stopped rows have no link ID: data-team join expectations
- A3-0325 — TAA has four entities/two BQ copies; remove rebalance TAA entity and janitor remaining three
- A3-0328 — BaseServiceLogicImpl.scala: Not that we don’t have index on customerId for this table. So let’s not call for too many customers at once when we call the sync in prod. We can add 
- A3-0378 — SgInvestmentServiceImpl.scala: Better to just inject db directly into `investmentScheduleActivePeriodJdbcRepository` and the methods can return Future instead of DBIO
- A3-0381 — Future schedule startingDate PK collision across01Aug/05Aug/15Aug updates tolerated for CKAE
- A3-0382 — InvestmentScheduleActivePeriodTable.scala: Can we prefix these timestamp field names with `plan_` to indicate they belong to plan level, not schedule level?
- A3-0392 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Better to check if `recurringInvestmentSchedule` exists then upsert, then recurringAmount/Interval won’t be optional
- A3-0393 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Same for customerId/tradingAccountType/ccy. If we can remove them and join on planId instead, then we can make this projection much faster as it doesn
- A3-0395 — InvestmentScheduleActivePeriodJdbcRepository.scala: I see that `deActivatedAt` is at plan level, but `markDeletionByPlanId` is called when schedule is removed, nothing to do with plan deactivation
- A3-0396 — InvestmentScheduleActivePeriodTable.scala: \(3\) will override \(1\) because they have same pk - but ok, we establish it’s ok in context of CKAE
- A3-0397 — Declared customerId index is not created; use JdbcSchema index-adjustment helper
- A3-0398 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Actually, here you should use the `recurringInvestmentSchedule` inside the investmentPlan of the event, instead of fetching latest from entity Also, i
- A3-0399 — InvestmentScheduleActivePeriodJdbcRepository.scala: You will need ``` sqlStatements( adjustCompositePkAndIndexIfNotExists( investmentSchedules, pkName = <pkName>, indexNames = List(<indexName>) ) ) ```
- A3-0425 — : I see we can improve the charge customer/plan query a bit more, e.g. currently for each customer, we query all plans to calculate fee, then again quer
- A3-0435 — RebalanceRequestJdbcRepositoryImpl.scala: ``` filterOpt(planId)(_.planId === _) ``` Does this work?
- A3-0439 — ThresholdBreachTable.scala: Alright it was there in the Cassandra table too. I guess we can leave it for now.
- A3-0441 — RebalanceRequestJdbcRepositoryImpl.scala: So we don’t filter for effectiveDate? Same for streamAll
- A3-0454 — WithdrawalTopicSubscriber.scala: pk is \(customerId, transactionId\)… no other index I think it’s better to query using both customerId \+ goalId / customerId \+ planId
- A3-0455 — WithdrawalTopicSubscriber.scala: Also, query by planId if exists would give fewer results, so let’s match that first
- A3-0457 — WithdrawalTopicSubscriber.scala: Also maybe we extract `feeChargeRequestId` first… if not exist, then we can save the lookup
- A3-0463 — StatementDataGenerator.scala: We would need to remove the absorbed tax details at transaction level in this method `calculateIfSameStatementDataExists` to avoid reprinting old stat
- A3-0508 — FeeChargeRequestJdbcDbHandlerV3.scala: Can we change to use the utils in `ExtendedPostgresProfile` See example in advisory `TemplateJdbcDbHandler`
- A3-0509 — FeeChargeRequestJdbcEventProcessorV5.scala: Hmm so we also update these planProfile too. I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:
- A3-0510 — FeeChargeRequestTableV3.scala: typically pk name should be `tableName_pk` or `tableName_pkey`
- A3-0519 — SgServiceLogicImpl.scala: As I type this, I can’t recall why I even created `TaxCalculationDetails` at all… so I’m thinking to drop it. Will need to clean cassandra of charge s
- A3-0584 — PlanProfileJdbcRepositoryV2.scala: Ok let’s up-version this table and fix this next, after we release these open PRs :thumbsup:
- A3-0615 — Slick cleanUp proposal preserves streaming and avoids running result twice
- A3-0618 — AltsFeeManager.scala: I need an new version of planProfile table, but essentially the idea here is to compute for Alts plans only The `customerFeesCalculator: CustomerAltsF
- A3-0639 — JdbcSchema.scala: We can’t drop until data team has moved
- A3-0660 — : We can run some mode query to check this one right?
- A3-0688 — TransactionTableV1_2.scala: No change required, but just to make sure we are on same page, this is the final table we want to switch over to. It’s not “intermediary”
- A3-0701 — RecommendedPortfolioChangePageLoader.scala: As discussed, this makes sense, but let’s implement this properly with a simple CRUD only table somewhere outside of gateway service.
- A3-0712 — PlanTimeseriesTopicSubscriber.scala: How about ``` _ <- maybeLatestStoredMV match { case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) => logger.info("Skipping..
- A3-0716 — PlanTimeseriesTopicSubscriber.scala: Yup, just normal upserting projection data
- A3-0717 — MV projection upserts every latest message before rebalance checks; same-group migration
- A3-0764 — TransactionFxConverter.scala: Can we change the logging to be clearer that “no fx rate found for ccypair \+ date”. Asking marketdata svc is fine, but more important is we need to f
- A3-0767 — Auto FX sync tradeoff: stale fallback cached for a day versus repeated missing-rate sync
- A3-0770 — FX cache T-10 historical lookup can become wrong fallback for missingT rate
- A3-0771 — FxRateHelper.scala: Why do `we only care about month anyway` ? Current usage of transactions in A&B and monthly statement, we would always need to load all transactions s
- A3-0772 — TransactionFxConverter.scala: distinct the pairs before loading?
- A3-0776 — FxRateHelper.scala: create a TreeMap keyed by priceDate first, then just lookup here? Otherwise we traverse the Seq everytime
- A3-0777 — FxRateHelper.scala: So if latest rate is requested when data is not available yet, we always reload from DB and fallback to near date. Is this intended so that we will ha
- A3-0778 — FxRateHelper.scala: I mean we just need `loadCacheWithFxRates`, no need to `loadCacheAndFind` In fact, using latest date here means we will always load before 3pm everyda
- A3-0779 — FxRateHelper.scala: Exactly my comment here [<url> data-inline-card='' } We don’t put if latest rate is not available
- A3-0781 — FxRateHelper.scala: Should we invalidate the cache after this sync so that we reload fresh rate?
- A3-0861 — DividendService.scala: Indeed. I kept the API in AdminService intact, and changed it to use the pagination endpoint instead.
- A3-0864 — SgServiceLogicImpl.scala: Ah this is just to compare between charge entity and charge readside? I think we can skip this, cuz we will anyhow fetch from entity and write again -
- A3-0880 — FxRatesProjectionRepository.scala: If no streaming, then don’t need SlickSession I think
- A3-0882 — FxRatesTopicSubscriberV2.scala: We are writing to DB only, so I think we can just dump as in \(stay true to projection\). I think we have this logic last time because it was via enti
- A3-0883 — FxRatesTopicSubscriberV2.scala: This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the 
- A3-0884 — FxRatesTopicSubscriberV2.scala: Slick support bulk upsert too
- A3-0886 — AdvisoryApplication.scala: Don’t we need subscriber to customer/onboarding topic to populate the `customerProjectionDataJdbcRepository`?
- A3-0894 — CustomerProjectionDataJdbcRepository.scala: If this gets expensive, we should consider adding another readside table for advisory profile containing only the latest entry
- A3-0895 — CustomerAdvisoryProfileJdbcRepository.scala: Hmm alright, maybe another readside table containing only latest is worth it :grimacing:
- A3-0896 — CustomerAdvisoryProfileJdbcRepository.scala: And in that new table, we can consider extract this field as an optional column, to make query simpler
- A3-0899 — HkServiceLogicImpl.scala: add batchUpsert?
- A3-0909 — CraManager.scala: Ok customer projection table will have data from onboarding entity, just no sync endpoint… So the sync needs to check customer status somehow
- A3-0910 — CustomerProjectionDataJdbcRepository.scala: findCustomerWithNonVcProfile\(bornBeforeDate: LocalDate\)
- A3-0912 — CustomerAdvisoryProfileSnapshotJdbcRepository.scala: should be “with expiry before” right? how about `streamNonVcProfile(expiringBefore: LocalDate)`
- A3-0920 — Stale onboarding DOB can overwrite newer customer DOB: version/timestamp TODO
- A3-0931 — HkServiceLogicImpl.scala: Oh bulk upsert for whole set of customers would be too large… either batch the source, or just upsert one by one I think…
- A3-0932 — HkServiceLogicImpl.scala: I didn’t realize getPaginatedSource already concat all the page previously..
- A3-0938 — DividendApplication.scala: The lags are tracked based on offsets only. So if offset table is not created, nothing will work…
- A3-0974 — TransactionJdbcRepositoryV2Test.scala: Good idea to truncate the table at the end. Save yourself some head scratching when you add the next test
- A3-0978 — ServiceLogicImpl.scala: this existing endpoint is already a hot mess with various conditional check - they are not intuitive API for consumer at all. How about we add new end
- A3-0979 — TransactionJdbcRepositoryV2.scala: we can all agree that having a single find\(\) method with various \(optional\) filters is better? If we do not want to change existing code, let’s ad
- A3-0980 — TransactionJdbcRepositoryV2.scala: You can see example for find method accepting list of filters at `com.endowus.silver.portfolio.impl.entities.portfolio.db.jdbc.PortfolioRepository`
- A3-0997 — CorporateProfileJdbcEventProcessor.scala: We only need to call create tables once, either here or when wiring DbHandler in Application
- A3-1032 — InvestmentRequestProjectionJdbcDbHandler.scala: add repository and move the query there
- A3-1035 — HkInvestmentTopicSubscriber.scala: Then we can upsert always… don’t need another update method
- A3-1038 — InvestmentRequestProjectionTable.scala: Can we name the table column matching field name? either updatedAt or lastUpdatedTS
- A3-1119 — : Will do the following in next PR: * enrich audit payload * persist to audit repository * add internal query endpoints for audit repository
- A3-1135 — PlanTradingRestrictionResponse.scala: Hmm don’t we need different DTO for this? The table columns are different
- A3-1225 — ServiceLogicImpl.scala: Shall we drop the Cassandra repository too, to avoid further wrong usage?
- A3-1332 — Measure goal-readside lookups before adding local eventually-consistent projections
- A3-1334 — TransactionJdbcRepositoryV2.scala: Just curious, what would be the use case to sort by these uuid?
- A3-1335 — TransactionJdbcRepositoryV2.scala: I see this too. But I’m just wondering, as an admin user, why would I ever want to sort by some UUID…
- A3-1412 — MasApiService.scala: Actually why don’t we query repository here…
- A3-1417 — CraManager.scala: I’ll add the Jdbc event processor \+ repository to query for this bit separately… PR is getting too fat now
- R-3320 — FYI this one uses Cassandra repository with IN clause. Not sure if anyone would create a FundSmart goal with 25 instruments though
- R-3367 — Withdrawn EXPLAIN result for instrument_holdings_v1 SUM/MIN join
- R-3368 — Historical allocation/time comparison: in-memory versus DB holding aggregation at parallelism 4
- R-3369 — Corrected holdings EXPLAIN uses two roughly seven-second parallel sequential scans
- R-3370 — Holdings index use differs between all-plan grouped and specific-plan queries
- R-3371 — October and January date ranges lead PostgreSQL to choose different scan plans
- R-3372 — There were 2144 hits of this warn log in Kibana in last distribution. Isn’t it too high to be Trade Ops mistake? Nevertheless, monitoring if any probably s
- R-3373 — Metrics of both approaches observed using [<url> ‌ I think I’m going with the approach in this PR, even though it’s tightly fit to the rebate distribution 
- R-3374 — Oops my bad: * Red and green box is approach in [<url> data-inline-card='' } , triggered with fromDate = 2021-10-01 \(not so much holding data\) and 2021-0
- R-3410 — Reset version since we rename to follow standard naming convention: * using singular noun for table names * using `tableName_pk_v` for pk ‌
- R-3443 — Number of rows play a part, but main reason why select without where condition is slow because it needs to jump multiple nodes to get all data - these netw
- R-3446 — StatementRepository IN-clause comment is conditional on customerId clustering-key placement
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
- R-3481 — I have one side question. This DB handler is not tied to any event processor, so we have to call `handler.createTables` here. If there is a readside event 
- R-3489 — Would `filter().result.headOption` be enough?
- R-3490 — take(1) translates to LIMIT 1, correcting the earlier result.headOption suggestion
- R-3515 — Historical question about TestContainers versus EmbeddedPostgres and in-memory tests
- R-3519 — typo: `indexName` Could we also explain why we need this, and cannot use existing `createIndexIfNotExists` that uses slick?
- R-3520 — Postgres has this naming convention apparently ``` {tablename}_{columnname(s)}_{suffix} ```
- R-3521 — Maybe rename this method to `fixIfNotExistsStatement` or something along that line? Same in `PlanProfileJdbcTable`
- R-3551 — It’s actually recommended to use `NetworkTopologyStrategy` even for local \(with only one DC configured\). But I guess not too important for this PR
- R-3553 — You can run `NetworkTopologyStrategy` with single node. And it will work fine too. And this will make it easy if we want to increase number of nodes later.
- R-3555 — I think it’s better to let consumer\(s\) have to chance to decide what to do with missing data - rather than throwing
- R-3556 — If you prefer Exception instead, because say you expect caller to always call with valid ID… then code is little cleaner to read if we return Future.failed
- R-3558 — Portfolio stats exact-ID lookup and filter lookup both produce a List response
- R-3561 — Nit: Do we want `v%d` instead?
- R-3562 — I think mentioned not to use this syntax in the PR for advisory..
- R-3576 — Yup, that’s correct. Apparent this table was manually updated in all environment without committing back to source code. ‌ See [<url> data-inline-card='' }

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

## A1-0011 — Remove code in CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> remove

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Target unspecified in comment; inspect hunk before applying removal.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:11 · comment 823005056 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:11 · comment 823005056 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala`

**Explicit source context (hunk):**

> +                  r.maybeRiskProfileExpiryDate
> +                )
> +              }.update(
> +                updatedProfile,
> +                Some(updatedProfile.riskProfileStatus),
> +                Some(updatedProfile.expiryDate)
> +              )
> +            }
> +

## A1-0014 — Assessment history PK is customerId and lastUpdatedTS

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcProjection.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Rows cannot share the same timestamp

**Source-preserving request, proposal, or question:**

> pk is `(customerId, lastUpdatedTS)` - they can’t share same TS

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:14 · comment 823078089 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcProjection.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:14 · comment 823078089 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcProjection.scala`

**Explicit source context (hunk):**

> +    dbHandler.upsert(CustomerAdvisoryProfileAssessmentData.fromCustomerAgeCapturedEvt(UUID.fromString(entityId), event))
> +  }
> +
> +  private def handleExpiryDateOverriddenEvt(entityId: String, event: ExpiryDateOverriddenEvt): Future[Unit] = {
> +    dbHandler.updateExpiryDateOfAssessment(UUID.fromString(entityId), event.currentAssessmentUpdatedTS, event.riskProfileStatus, event.expiryDate)
> +  }
> +
> +  private def handleCraExpiredEvt(entityId: String, event: CraExpiredEvt): Future[Unit] = {
> +    dbHandler.expireAssessment(UUID.fromString(entityId), event.currentAssessmentUpdatedTS)

## A1-0016 — CRA snapshot stores queryable derived columns while history updates only advisoryProfile

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> The snapshot table has the derived columns since we need to query on them. The history table doesnt have those. Both update the whole advisoryProfile

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:16 · comment 823088064 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

## A1-0018 — CRA history does not update by lastUpdatedTS alone

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We don’t update by `lastUpdatedTS` alone

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:18 · comment 823075773 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

**Evidence:** anon-1.jsonl:18 · comment 823075773 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileAssessmentHistoryJdbcDbHandler.scala`

**Explicit source context (hunk):**

> +            val updatedProfile = patch(profile)
> +            if (updatedProfile.lastUpdatedTS != profile.lastUpdatedTS) {
> +              DBIO.failed(new Exception(s"Failed to $patchContext: Updating lastUpdatedTS is not allowed"))
> +            } else {
> +              customerAdvisoryProfileAssessments
> +                .filter(_.customerId === data.customerId)
> +                .filter(_.lastUpdatedTS === data.lastUpdatedTS)
> +                .map(_.advisoryProfile)
> +                .update(updatedProfile)

## A1-0019 — CRA snapshot updates explicit columns to exclude complex product acknowledgement

**Source stance:** explanation

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala; operation: [] feat(advisory): Fix CRA assessment history projection; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Yes, need to update the columns explicitly since we want to leave the complex product ack column out

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:19 · comment 823074672 · PR 14228 · 2026-07-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcDbHandlerV4.scala`

**Explicit source context (pr_title):**

> [] feat(advisory): Fix CRA assessment history projection

## A1-0435 — Lookup plan by PK planId then validate customerId

**Source stance:** suggestion

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/PlanFeeInstructionManager.scala; operation: Resolve INV-5291: Eam profile validation integrations, fix up table name; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Why don’t we just look up by planId \(pk\) and check its customerId instead?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:442 · comment 793451305 · PR 13798 · 2026-05-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/PlanFeeInstructionManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-5291: Eam profile validation integrations, fix up table name

**Evidence:** anon-1.jsonl:442 · comment 793451305 · PR 13798 · 2026-05-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/PlanFeeInstructionManager.scala`

**Explicit source context (hunk):**

> private def validateEamCustomer(customerId: UUID, planId: UUID): Future[Done] = {
> -    // TODO (

**Evidence:** anon-1.jsonl:442 · comment 793451305 · PR 13798 · 2026-05-06

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/PlanFeeInstructionManager.scala`

**Explicit source context (hunk):**

> ): Add after profile PR is merged
> -    Future.successful(Done)
> +    for {
> +      mappedCustomerId <- planProfileJdbcRepository.findPlanById(planId).map(_.map(_.customerId))
> +      _ = if (!mappedCustomerId.contains(customerId)) {
> +        throw BadRequest(s"Plan: $planId is not linked to customer: $customerId")
> +      }
> +      _ <- feeTieringProfileMappingJdbcRepository

## A1-0456 — CustomerId PK prevents duplicate fee profile; change collection type to Set

**Source stance:** explanation

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/jdbc/feetiering/mapping/FeeTieringProfileMappingJdbcRepository.scala; operation: [INV-5238] feat(charge): Charge service changes to construct EAM contexts on quarterly charge flow; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> pk is customerId so yea not possible. Just changing the type to Set

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:463 · comment 793864229 · PR 13599 · 2026-05-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/jdbc/feetiering/mapping/FeeTieringProfileMappingJdbcRepository.scala`

**Explicit source context (pr_title):**

> [INV-5238] feat(charge): Charge service changes to construct EAM contexts on quarterly charge flow

**Evidence:** anon-1.jsonl:463 · comment 793864229 · PR 13599 · 2026-05-07

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/jdbc/feetiering/mapping/FeeTieringProfileMappingJdbcRepository.scala`

**Explicit source context (hunk):**

> +        .filter(_.profileId === profileId)
> +        .map(_.customerId)
>          .result
> -    }
> +    }.map(_.toSet)
>    }
>  }
> -

## A1-0460 — Distinguish true date from timestamp in PRP annotation mapping

**Source stance:** suggestion

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala; operation: DATA-1769: Data catalog annotations for transaction; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Use LocalDate if date; otherwise retain timestamp mapping and separate transformed PRP mapping

**Source-preserving request, proposal, or question:**

> Just a note for us to consider in future, but generally I agree with the bot’s detection here. It is a bit off to see the timestamp field gets tagged as date.
> 
> If it is indeed a date field, transaction svc should use LocaleDate instead of ZonedDateTime, otherwise we unnecessarily having to deal the with zone conversion. If it is indeed a timestamp field, then maybe the annotation mappings should be maintained between BE model vs raw tables, and we have another mapping to PRP if there’s any transformation happening on data side

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:467 · comment 795105492 · PR 13801 · 2026-05-11

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/common/TransactionTypes.scala`

**Explicit source context (pr_title):**

> DATA-1769: Data catalog annotations for transaction

## A1-0487 — Resolved Cassandra profiles override apparent LOCAL_ONE with LOCAL_QUORUM on Astra

**Source stance:** reported-verification

**Context:**

> component: conf-reference/src/main/resources/cassandra/datastax-driver-4.x.conf; operation: Refactor configs for Cassandra com.datastax.oss:java-driver-core:4.x; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We are lucky here, otherwise we would have needed to validate all our Cassandra readside tables
> 
> ‌
> 
> Resolved config indeed shows we are using the default LOCAL\_ONE
> […incidental material or intervening source omitted…]
> ‌
> 
> However, checking actual resolved profiles gives LOCAL\_QUORUM for default profile
> […incidental material or intervening source omitted…]
> logs of report svc in SG staging \(only existing 5s timeout override\)
> […incidental material or intervening source omitted…]
> ‌
> 
> The driver logic has this chain:
> 
> * `com.datastax.oss.driver.internal.core.session.DefaultSession`
> 
>     * init
>     * → initializePools
>     * → poolManager.init
>     
> * `com.datastax.oss.driver.internal.core.session.PoolManager`
> 
>     * init
>     * → channelPoolFactory.init
>     * → ChannelPool.init
>     
> * `com.datastax.oss.driver.internal.core.pool`
> 
>     * connect
>     * → addMissingChannels
>     * → channelFactory.connect
>     
> * `com.datastax.oss.driver.internal.core.channel.ChannelFactory`
> 
>     * connect
>     * connect listener that override consistency to LOCAL\_QUORUM if the driver config has default values from its reference.conf, for datastax cloud product \(which Astra Serverless should be true here\)
> […incidental material or intervening source omitted…]
> CassandraSession Profile default: timeout=PT5S consistency=LOCAL_QUORUM
> CassandraSession Profile akka-projection-cassandra-profile: timeout=PT5S consistency=QUORUM
> […incidental material or intervening source omitted…]
> List<String> productTypes = supportedOptions.get("PRODUCT_TYPE");
> String productType =
>     productTypes != null && !productTypes.isEmpty()
>         ? productTypes.get(0)
>         : UNKNOWN_PRODUCT_TYPE;
> ChannelFactory.this.productType = productType;
> DriverConfig driverConfig = context.getConfig();
> if (driverConfig instanceof TypesafeDriverConfig
>     && productType.equals(DATASTAX_CLOUD_PRODUCT_TYPE)) {
>   ((TypesafeDriverConfig) driverConfig)
>       .overrideDefaults(
>           ImmutableMap.of(
>               DefaultDriverOption.REQUEST_CONSISTENCY,
>               ConsistencyLevel.LOCAL_QUORUM.name()));
> }

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Keep actual profile values: default PT5S LOCAL_QUORUM, akka-projection PT5S QUORUM; driver overrides reference.conf defaults for DATASTAX_CLOUD_PRODUCT_TYPE.
- Selected source excerpts preserve this specific case; incidental identities and repetitive logs are omitted. This record does not claim an unreported implementation outcome.

**Evidence:** anon-1.jsonl:494 · comment 787703047 · PR 13756 · 2026-04-24

Source path: `conf-reference/src/main/resources/cassandra/datastax-driver-4.x.conf`

> We are lucky here, otherwise we would have needed to validate all our Cassandra readside tables
> 
> ‌
> 
> Resolved config indeed shows we are using the default LOCAL\_ONE

**Explicit source context (pr_title):**

> Refactor configs for Cassandra com.datastax.oss:java-driver-core:4.x

**Evidence:** anon-1.jsonl:494 · comment 787703047 · PR 13756 · 2026-04-24

Source path: `conf-reference/src/main/resources/cassandra/datastax-driver-4.x.conf`

> ‌
> 
> However, checking actual resolved profiles gives LOCAL\_QUORUM for default profile

**Evidence:** anon-1.jsonl:494 · comment 787703047 · PR 13756 · 2026-04-24

Source path: `conf-reference/src/main/resources/cassandra/datastax-driver-4.x.conf`

> logs of report svc in SG staging \(only existing 5s timeout override\)

**Evidence:** anon-1.jsonl:494 · comment 787703047 · PR 13756 · 2026-04-24

Source path: `conf-reference/src/main/resources/cassandra/datastax-driver-4.x.conf`

> ‌
> 
> The driver logic has this chain:
> 
> * `com.datastax.oss.driver.internal.core.session.DefaultSession`
> 
>     * init
>     * → initializePools
>     * → poolManager.init
>     
> * `com.datastax.oss.driver.internal.core.session.PoolManager`
> 
>     * init
>     * → channelPoolFactory.init
>     * → ChannelPool.init
>     
> * `com.datastax.oss.driver.internal.core.pool`
> 
>     * connect
>     * → addMissingChannels
>     * → channelFactory.connect
>     
> * `com.datastax.oss.driver.internal.core.channel.ChannelFactory`
> 
>     * connect
>     * connect listener that override consistency to LOCAL\_QUORUM if the driver config has default values from its reference.conf, for datastax cloud product \(which Astra Serverless should be true here\)

**Evidence:** anon-1.jsonl:494 · comment 787703047 · PR 13756 · 2026-04-24

Source path: `conf-reference/src/main/resources/cassandra/datastax-driver-4.x.conf`

> CassandraSession Profile default: timeout=PT5S consistency=LOCAL_QUORUM
> CassandraSession Profile akka-projection-cassandra-profile: timeout=PT5S consistency=QUORUM

**Evidence:** anon-1.jsonl:494 · comment 787703047 · PR 13756 · 2026-04-24

Source path: `conf-reference/src/main/resources/cassandra/datastax-driver-4.x.conf`

> List<String> productTypes = supportedOptions.get("PRODUCT_TYPE");
> String productType =
>     productTypes != null && !productTypes.isEmpty()
>         ? productTypes.get(0)
>         : UNKNOWN_PRODUCT_TYPE;
> ChannelFactory.this.productType = productType;
> DriverConfig driverConfig = context.getConfig();
> if (driverConfig instanceof TypesafeDriverConfig
>     && productType.equals(DATASTAX_CLOUD_PRODUCT_TYPE)) {
>   ((TypesafeDriverConfig) driverConfig)
>       .overrideDefaults(
>           ImmutableMap.of(
>               DefaultDriverOption.REQUEST_CONSISTENCY,
>               ConsistencyLevel.LOCAL_QUORUM.name()));
> }

## A1-0488 — Extracted basic.graph configuration redundant because DSE-only

**Source stance:** explanation

**Context:**

> component: conf-reference/src/main/resources/persistence/cassandra.conf; operation: Refactor configs for Cassandra com.datastax.oss:java-driver-core:4.x; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This config \(added by scalac team since last time\) is actually redundant. They are specific to DSE cluster only. Hence I removed from the extracted conf.
> 
> See [

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:495 · comment 787684968 · PR 13756 · 2026-04-24

Source path: `conf-reference/src/main/resources/persistence/cassandra.conf`

**Explicit source context (pr_title):**

> Refactor configs for Cassandra com.datastax.oss:java-driver-core:4.x

## A1-0489 — Lagom to Alpakka Cassandra migration hid changed session configuration path

**Source stance:** explanation

**Context:**

> component: conf-reference/src/main/resources/cassandra/datastax-driver-4.x.conf; operation: Refactor configs for Cassandra com.datastax.oss:java-driver-core:4.x; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Old lagom.persistence.read-side.cassandra overrides differ despite similar constructors

**Source-preserving request, proposal, or question:**

> Why was this missed? I’m not 100% sure but looking at our session init code, it’s understandable that we missed it
> 
> ‌
> 
> Before lagom migration, using lagom persistence
> 
> ```
>   override lazy val cassandraSession: CassandraSession =
>     withCodecs(new CassandraSession(actorSystem), codecs)
> ```
> 
> ‌
> 
> After lagom migration, using alpakka cassandra
> 
> ```
>   lazy val cassandraSession: CassandraSession =
>     CassandraSessionRegistry.get(actorSystem.classicSystem).sessionFor(CassandraSessionSettings()).withCodecs()
> ```
> 
> ‌
> 
> Both looks almost identical, especially that they do not have any special overrides.
> 
> However, old `CassandraSession` is [
> […incidental material or intervening source omitted…]
> which we used to have config set for `lagom.persistence.read-side.cassandra` in `persistence/cassandra.conf` before.
> 
> I’m not 100% if scalac team mistook and thought we used DSE and hence they only set `basic.graph` config

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Commenter explicitly uncertain whether DSE assumption caused omission.

**Evidence:** anon-1.jsonl:496 · comment 787717065 · PR 13756 · 2026-04-24

Source path: `conf-reference/src/main/resources/cassandra/datastax-driver-4.x.conf`

> Why was this missed? I’m not 100% sure but looking at our session init code, it’s understandable that we missed it
> 
> ‌
> 
> Before lagom migration, using lagom persistence
> 
> ```
>   override lazy val cassandraSession: CassandraSession =
>     withCodecs(new CassandraSession(actorSystem), codecs)
> ```
> 
> ‌
> 
> After lagom migration, using alpakka cassandra
> 
> ```
>   lazy val cassandraSession: CassandraSession =
>     CassandraSessionRegistry.get(actorSystem.classicSystem).sessionFor(CassandraSessionSettings()).withCodecs()
> ```
> 
> ‌
> 
> Both looks almost identical, especially that they do not have any special overrides.
> 
> However, old `CassandraSession` is [

**Explicit source context (pr_title):**

> Refactor configs for Cassandra com.datastax.oss:java-driver-core:4.x

**Evidence:** anon-1.jsonl:496 · comment 787717065 · PR 13756 · 2026-04-24

Source path: `conf-reference/src/main/resources/cassandra/datastax-driver-4.x.conf`

> which we used to have config set for `lagom.persistence.read-side.cassandra` in `persistence/cassandra.conf` before.
> 
> I’m not 100% if scalac team mistook and thought we used DSE and hence they only set `basic.graph` config

## A1-0552 — Fetch monthly returns from DB rather than entity

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/MonthlyChangeDataStitcher.scala; operation: Feat/INV-5126 stitch source add marketdata; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Fetch from db is fine, no need to go to entity for this

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:559 · comment 778130318 · PR 13629 · 2026-04-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/MonthlyChangeDataStitcher.scala`

**Explicit source context (pr_title):**

> Feat/INV-5126 stitch source add marketdata

**Evidence:** anon-1.jsonl:559 · comment 778130318 · PR 13629 · 2026-04-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/MonthlyChangeDataStitcher.scala`

**Explicit source context (hunk):**

> +
> +  }
> +
> +  def fetchFromMarketerSvc(fundInfo: EndowusStitchSourceDto, currencyToConvertTo: CurrencyUnit): Future[List[common.MonthlyChange]] = {
> +    instrumentMonthlyChangesJdbcRepository.findByInstrumentIds(Set(fundInfo.idValue), currencyToConvertTo).map(_.values.toList.flatten)
> +  }
> +
> +  private[helpers] def getIndividualMStarMonthlyReturn(
>      fundInfo: MstarStitchSourceDto,

## A1-0812 — Tag filter may ignore condition and include empty tags

**Source stance:** open-question

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/db/jdbc/PortfolioRepository.scala; operation: Feat/BB-2959 portfolio filters enhancement; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> So for `tag` filter, we want to return empty tag in the results, ignoring the input condition?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:824 · comment 742586089 · PR 12884 · 2026-01-22

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/db/jdbc/PortfolioRepository.scala`

**Explicit source context (pr_title):**

> Feat/BB-2959 portfolio filters enhancement

**Evidence:** anon-1.jsonl:824 · comment 742586089 · PR 12884 · 2026-01-22

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/db/jdbc/PortfolioRepository.scala`

**Explicit source context (hunk):**

> case Filter("description", op, value)         => stringIsOrIlike(t.description, op, value)
>      case Filter("optimizedCcy", op, value)        => t.optimizedCcy.map(ccyIsOrIn(_, op, value)).getOrElse(CoerceFalse)
>      case Filter("shortName", op, value)           => stringIsOrIlike(t.name, op, value)
> -    case Filter("tag", op, value)                 => stringIsOrIlike(t.name, op, value)
> +    case Filter("tag", op, value)                 => optional(t.tag, op, value)(stringIsOrIlike)
>      case Filter("cashManagementStyle", op, value) => t.cashManagementStyle.map(enumIsOrIn(CashManagementStyle)(_, op, value)).getOrElse(CoerceFalse)
>      case _                                        => CoerceFalse

## A1-0813 — Reuse optional(t.name,op,value)(stringIsOrIlike) for Option[String]

**Source stance:** suggestion

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/db/jdbc/PortfolioRepository.scala; operation: Feat/BB-2959 portfolio filters enhancement; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Oh looks like it’s the opposite, we need to handle optional because the field is `Option[String]`
> 
> Why don’t we just reuse existing method like this, instead of defining another custom one?
> 
> ```
> optional(t.name, op, value)(stringIsOrIlike)
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:825 · comment 742601667 · PR 12884 · 2026-01-22

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/db/jdbc/PortfolioRepository.scala`

**Explicit source context (pr_title):**

> Feat/BB-2959 portfolio filters enhancement

## A1-0815 — inSetBind already handles empty set

**Source stance:** open-question

**Context:**

> component: silver-commons-jdbc/src/main/scala/com/endowus/silver/commons/jdbc/Filters.scala; operation: Feat/BB-2959 portfolio filters enhancement; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need to check `isEmpty`? `inSetBind` should already does that?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:827 · comment 743470688 · PR 12884 · 2026-01-23

Source path: `silver-commons-jdbc/src/main/scala/com/endowus/silver/commons/jdbc/Filters.scala`

**Explicit source context (pr_title):**

> Feat/BB-2959 portfolio filters enhancement

**Evidence:** anon-1.jsonl:827 · comment 743470688 · PR 12884 · 2026-01-23

Source path: `silver-commons-jdbc/src/main/scala/com/endowus/silver/commons/jdbc/Filters.scala`

**Explicit source context (hunk):**

> +          Try(strs.map(UUID.fromString))
> +        }
> +        .fold(
> +          _ => CoerceFalse,
> +          uuids => column inSetBind uuids
> +        )
> +    case _ => CoerceFalse
> +  }
> +

## A1-0817 — Test empty inSetBind returning false

**Source stance:** requested-change

**Context:**

> component: silver-commons-jdbc/src/main/scala/com/endowus/silver/commons/jdbc/Filters.scala; operation: Feat/BB-2959 portfolio filters enhancement; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Slick implementation already checks seq.isEmpty

**Source-preserving request, proposal, or question:**

> ```
>   def inSet[R](seq: scala.collection.Iterable[B1])(implicit om: o#to[Boolean, R]) =
>     if(seq.isEmpty) om(LiteralColumn(false))
>     else om.column(Library.In, n, ProductNode(ConstArray.from(seq.map{ v => LiteralNode(implicitly[TypedType[B1]], v) })))
>   def inSetBind[R](seq: scala.collection.Iterable[B1])(implicit om: o#to[Boolean, R]) =
>     if(seq.isEmpty) om(LiteralColumn(false))
>     else om.column(Library.In, n, ProductNode(ConstArray.from(seq.map(v => LiteralNode(implicitly[TypedType[B1]], v, vol = true)))))
> ```
> 
> We can add a test for empty too to verify this

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:829 · comment 743515609 · PR 12884 · 2026-01-23

Source path: `silver-commons-jdbc/src/main/scala/com/endowus/silver/commons/jdbc/Filters.scala`

**Explicit source context (pr_title):**

> Feat/BB-2959 portfolio filters enhancement

## A1-0820 — Separate EventTagRecordInput without ordering from required-ordering select record

**Source stance:** suggestion

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/auto/AutoProjectionEventSourceProvider.scala; operation: [NE-363] introduce auto projection; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Slick table should have required auto-increment PK

**Source-preserving request, proposal, or question:**

> nit: ideally we should have separated `EventTagRecordInput` without `ordering` field to be used only in `insert`, and `EventTagRecord` with required `ordering` field to be used only in select queries. Then `EventTagTable` would have required auto-incrementing pkey. I think this should be achievable with Slick

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:832 · comment 744467222 · PR 13219 · 2026-01-26

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/auto/AutoProjectionEventSourceProvider.scala`

**Explicit source context (pr_title):**

> [NE-363] introduce auto projection

## A1-0822 — Slick insert projection takes EventTagRecordInput and returns generated ordering

**Source stance:** suggestion

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/auto/AutoProjectionEventSourceProvider.scala; operation: [NE-363] introduce auto projection; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Normal records always have required ordering, eliminating optional checks

**Source-preserving request, proposal, or question:**

> Maybe something like this
> 
> ```
> case class EventTagRecordInput(...other fields...)
> 
> case class EventTagRecord(
>   ordering: Long,
>   ...other fields...
> )
> 
> object EventTagRecord {
>   def fromInput(input: EventTagRecordInput, ordering: Long): EventTagRecord = ...
> }
> ```
> 
> ‌
> 
> Table with proper required auto-incrementing PK
> 
> ```
> class EventTagTable {
> 
>   def ordering: Rep[Long] = column[Long]("ordering", O.PrimaryKey, O.AutoInc)
>   ...other columns...
> 
>   override def * : ProvenShape[EventTagRecord] =
>     (ordering, persistenceId, eventManifest, event, tag, addedAt).<>((EventTagRecord.apply _).tupled, EventTagRecord.unapply)
> 
>   def projectionForInsert =
>     (persistenceId, eventManifest, event, tag, addedAt).<>((EventTagRecordInput.apply _).tupled, EventTagRecordInput.unapply)
> }
> ```
> 
> ‌
> 
> ```
> trait EventTagDao {
>   def insert(item: EventTagRecordInput): Future[Long]
>   def readNext(n: Long)(tag: String, from: Long): Future[List[EventTagRecord]]
> }
> ```
> 
> ‌
> 
> ```
> class EventTagDaoJdbc extends EventTagDao {
>   def insert(item: EventTagRecordInput): Future[Long] = {
>     val insertQuery = table
>       .map(_.projectionForInsert)
>       .returning(table.map(_.ordering))
>       .into(EventTagRecord.fromInput)
> 
>     db.run(insertQuery += item).map(_.ordering)
>   }
> }
> ```
> 
> ‌
> 
> Then in every usage of EventTagRecord, we have proper required `ordering` field instead of having to check optional.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:834 · comment 744491166 · PR 13219 · 2026-01-26

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/auto/AutoProjectionEventSourceProvider.scala`

**Explicit source context (pr_title):**

> [NE-363] introduce auto projection

## A1-0943 — Compiler warning finds map/flatMap bug mixing DBIO and Future

**Source stance:** observed-defect

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala; operation: Fatal compiler warnings; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Another bug with map vs flatmap, and confusing DBIO vs Future

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:957 · comment 730846176 · PR 13132 · 2025-12-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala`

**Explicit source context (pr_title):**

> Fatal compiler warnings

**Evidence:** anon-1.jsonl:957 · comment 730846176 · PR 13132 · 2025-12-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala`

**Explicit source context (hunk):**

> -          case Some(_) => Future.unit
> -          case None => Future.failed(new Exception(s"Expected some record to be upserted for $TableName, but got None"))
> -        })
> -    )
> +    database.run(instrumentPortfolioSubscribersDataTable.insertOrUpdateAll(data)).flatMap {
> +      case Some(_) => Future.unit
> +      case None    => Future.failed(new Exception(s"Expected some record to be upserted for $TableName, but got None"))
> +    }
>    }

## A1-1047 — Stream DB once and loop locales inside; otherwise mapAsync(1)

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** DB streaming connections precious; avoid concurrent locale streams

**Source-preserving request, proposal, or question:**

> DB connection is precious, let’s stream once and we can loop thru the locales instead?
> 
> If you still want to loop locales outside, then let’s mapAsync\(1\) only so that we don’t open concurrent streaming connections

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1064 · comment 675906191 · PR 12485 · 2025-08-28

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

## A1-1053 — Stream templates before locales and validate tags without collecting

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Current per-locale collection repeats all templates

**Source-preserving request, proposal, or question:**

> Actually here you’re collecting all templates multiple times \(x locales\), then check merged displayTags again.
> 
> Isn’t it better to stream template first, then loop thru the locales? Then you don’t need to collect the templates or their tags at all

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1070 · comment 680165620 · PR 12485 · 2025-09-08

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/translation/AdvisoryDataTranslationLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

## A1-1066 — Stream outside locale so query once like advisory

**Source stance:** requested-change

**Context:**

> component: instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala; operation: Resolve INV-4629: Translation data reconciliation logic; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Stream outside of locale, so that we query once? Similar to advisory one

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1083 · comment 681456016 · PR 12485 · 2025-09-10

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala`

**Explicit source context (pr_title):**

> Resolve INV-4629: Translation data reconciliation logic

**Evidence:** anon-1.jsonl:1083 · comment 681456016 · PR 12485 · 2025-09-10

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/logic/service/TranslationDataLogic.scala`

**Explicit source context (hunk):**

> +
> +    for {
> +      instrumentDataErrorCount <- instrumentJdbcRepository
> +        .streamAllActiveNonBenchmarkWhitelistedInstruments
> +        .map(Instrument.toDto(_, dateTimeProvider.zoneId, FundDocumentConfig.UnmodifiedFundDocumentConfig))
> +        .map(InstrumentTranslatableModel.create)
> +        .mapAsync(parallelism = 2) { translatableModel =>
> +          StreamSource(locales)
> +            .mapAsync(parallelism = 1) { locale =>

## A1-1069 — Timestamp still required because TTL cannot apply to Cassandra key columns

**Source stance:** explanation

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We still need timestamp because TTL cannot be applied to key columns

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1086 · comment 700100981 · PR 12767 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

**Evidence:** anon-1.jsonl:1086 · comment 700100981 · PR 12767 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala`

**Explicit source context (hunk):**

> +          PRIMARY KEY((customer_id, entity_type), timestamp, entity_id)
> +        )
> +    """.stripMargin
> +
> +  def migrateTable(session: CassandraSession, keySpace: String)(implicit executionContext: ExecutionContext): Future[Unit] = {
> +    for {
> +      _ <- session.executeDDL(s"USE $keySpace")
> +      _ <- session.executeDDL(CreateReadRoutingTableCql)
> +    } yield ()

## A1-1070 — Use Cassandra materialized view instead of high-cardinality index

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Cassandra index is not performant on high cardinality columns. We want to use materialized view instead

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1087 · comment 700083141 · PR 12767 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1072 — Monitor query performance and tombstone metrics

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> See if we have metrics for query performance \+ tombstones & attempt to monitor it

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1089 · comment 700101944 · PR 12767 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

**Evidence:** anon-1.jsonl:1089 · comment 700101944 · PR 12767 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala`

**Explicit source context (hunk):**

> +          PRIMARY KEY((customer_id, entity_type), timestamp, entity_id)
> +        )
> +    """.stripMargin
> +
> +  def migrateTable(session: CassandraSession, keySpace: String)(implicit executionContext: ExecutionContext): Future[Unit] = {
> +    for {
> +      _ <- session.executeDDL(s"USE $keySpace")
> +      _ <- session.executeDDL(CreateReadRoutingTableCql)
> +    } yield ()

## A1-1074 — Partition key is entity_type and entity_id

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> nit: PartitionKey should be `(entity_type, entity_id)`
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1091 · comment 700077661 · PR 12767 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

**Evidence:** anon-1.jsonl:1091 · comment 700077661 · PR 12767 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala`

**Explicit source context (hunk):**

> +          PRIMARY KEY((customer_id, entity_type), timestamp, entity_id)
> +        )
> +    """.stripMargin
> +
> +  def migrateTable(session: CassandraSession, keySpace: String)(implicit executionContext: ExecutionContext): Future[Unit] = {
> +    for {
> +      _ <- session.executeDDL(s"USE $keySpace")
> +      _ <- session.executeDDL(CreateReadRoutingTableCql)
> +    } yield ()

## A1-1075 — Compare per-version timestamp PK with per-entity TTL upsert

**Source stance:** suggestion

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s consider 2 approaches:
> 
> 1. Each row is one version
> 
>     * pk `((entity_type, entity_id), timestamp)`
>     * ttl for each row
>     * insert only
>     * every version will create tombstone via ttl
>     * allow us to query by timestamp
>     
> 2. Each row is one entity
> 
>     * pk `((entity_type, entity_id))`
>     * ttl for each row
>     * cassandra insert is upsert by pk \(citation needed\), but def dont want to use update \(which requires read before write\)
>     * every version will create tombstone via insert immediately, and via ttl for last version
>     * cannot query by timestamp
>     
> 
> ‌
> 
> Last time we decide to store version in pk, was in context of pg which doesn’t support TTL, hence we needed the timestamp.
> 
> But with cassandra impl, we don’t need this anymore.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Preserve tombstone and timestamp-query tradeoffs; source says Cassandra insert-upsert needs citation and claims update needs read; not verified conclusion.

**Evidence:** anon-1.jsonl:1092 · comment 700081987 · PR 12767 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1076 — Tune compaction and gc grace for TTL usage

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala; operation: Initial EC POC Idea; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Table-level options must compromise across entity-type TTLs

**Source-preserving request, proposal, or question:**

> Check compaction strategy \(time window?\) \+ gc grace period \(lower?\) config to be suitable with TTL usage. Both support table level config.
> 
> Ideally we want to associate this with TTL, but our TTL is per entity type instead of whole table. So maybe find some middle ground

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1093 · comment 700086152 · PR 12767 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/rrt/ReadRoutingTableDbHandler.scala`

**Explicit source context (pr_title):**

> Initial EC POC Idea

## A1-1297 — Force revoke uses deleteRequest matching stale lock

**Source stance:** requested-change

**Context:**

> component: timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala; operation: [NE-354] introduce database based locking mechanism; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** A revokes stale; C acquires; delayed B must not delete C

**Source-preserving request, proposal, or question:**

> Since this is force revoke, we want to use deleteRequest to ensure we only revoke the one with stale acks?
> 
> We might have race condition, \(even though unlikely\), we might run into situation that:
> 
> * task A and B both get barred and tried to revoke the lock with stale-ack satisfying the condition in `tryUnlockBasedOnExisting`
> * task A successfully revoke that lock
> * before task B manages to call the noop revoke, task C comes in and acquires the lock
> * task B now wrongfully revoke the lock of task C
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1312 · comment 714592873 · PR 12874 · 2025-11-17

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala`

**Explicit source context (pr_title):**

> [NE-354] introduce database based locking mechanism

## A1-1302 — Normal release must match original lock request

**Source stance:** observed-defect

**Context:**

> component: timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala; operation: [NE-354] introduce database based locking mechanism; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Starved A heartbeat lets B revoke/acquire; A completion must not delete B lock; Futures not cancelled

**Source-preserving request, proposal, or question:**

> Since we can’t cancel future, in some extreme scenario \(thread starvation \+ too aggressive `unlockDelay`\) \(or at least in theory\), we might run into a race condition such that:
> 
> * task A acquires the lock and goes on with its long running logic
> * thread starvation / CPU constraints causes the heartbeat ack to miss updates
> * aggressive `unlockDelay` enables other tasks to be able to take over the lock
> * task B revokes the lock of task A - this never cancels the currently running task A
> * task A finally completes, now attempts to release its lock
> 
> Here we call delete instead of deleteRequest, that means task A would remove the task B’s lock
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1317 · comment 715086775 · PR 12874 · 2025-11-18

Source path: `timeseries-impl/src/main/scala/com/endowus/silver/timeseries/impl/logic/util/impl/DistributedLockLogicDbImpl.scala`

**Explicit source context (pr_title):**

> [NE-354] introduce database based locking mechanism

## A1-1400 — Empty journal partition returns empty instead of throw

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala; operation: [INV-4929] feat: limit events size in inspect entity api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> No need to throw if partition is empty, just let it be and the query would simply return empty result

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1416 · comment 700059700 · PR 12775 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala`

**Explicit source context (pr_title):**

> [INV-4929] feat: limit events size in inspect entity api

## A1-1401 — Refactor TypedEventDao query resolution by optional from/to

**Source stance:** suggestion

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala; operation: [INV-4929] feat: limit events size in inspect entity api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I think we can structure the methods a bit better, with simplified logic too.
> 
> Maybe something like this?
> 
> ```scala
> object TypedEventDao {
>   private case class PartitionInfo(partitionNr: Long, highestSequenceNrInPartition: Long)
> }
> ```
> 
> ```scala
> private def resolveQueryInfo(entityTypeName: String, entityId: String, from: Option[Long], to: Option[Long])(implicit ex: ExecutionContext): Future[ResolvedQueryInfo] = {
>   val targetPartitionSize = lookupTargetPartitionSize(entityTypeName)
>   val persistentId = makePersistentId(entityTypeName, entityId)
> 
>   (from, to) match {
>     case (None, None) =>
>       // Event sequenceNr range is not specified, return last batch of events
>       resolvePartitionInfoWithHighestSequenceNr(persistentId, targetPartitionSize)
>         .map(...)
> 
>     case (Some(requestedFrom), _) =>
>       // Honor requested starting sequenceNr, and resolve ending sequenceNr
>       val resolvedPartitionNr = requestedFrom / targetPartitionSize
>       resolvePartitionInfo(persistentId, resolvedPartitionNr)
>         .map(...)
> 
>     case (None, Some(requestedTo)) =>
>       // Honor requested ending sequenceNr, and resolve starting sequenceNr
>       val resolvedPartitionNr = requestedTo / targetPartitionSize
>       resolvePartitionInfo(persistentId, resolvedPartitionNr)
>         .map(...)
>   }
> }
> 
> private def resolvePartitionInfoWithHighestSequenceNr(persistenceId: String, targetPartitionSize: Long): Future[PartitionInfo] = {
>   // TODO: Properly traverse all partitionNr of persistenceId until returned max sequenceNr is smaller than target partition size
>   // Temporary assume all entities have single partition
>   resolvePartitionInfo(persistenceId, partitionNr = 0L)
> }
> 
> private def resolvePartitionInfo(persistenceId: String, partitionNr: Long): Future[PartitionInfo] = {
>   ...
> }
> 
> private def lookupTargetPartitionSize(entityTypeName: String): Long = {
>   // TODO: Proper lookup from corresponding CassandraJournalConfig.targetPartitionSize
>   // Temporary return default value from cassandra-journal.target-partition-size = 500000
>   // taken from akka-persistence-cassandra reference.conf
>   500_000L
> }
> ```
> 
> ‌

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- PartitionInfo required values; temporary single partition and500000 default; TODO actual config lookup and traversal; later sequence formula corrected.

**Evidence:** anon-1.jsonl:1417 · comment 700067588 · PR 12775 · 2025-10-15

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala`

**Explicit source context (pr_title):**

> [INV-4929] feat: limit events size in inspect entity api

## A1-1402 — Compare range with partition lowest sequence rather than1

**Source stance:** open-question

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala; operation: [INV-4929] feat: limit events size in inspect entity api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I suppose by right, instead of `1L`, we should compare with lowest sequence nr in partition? Same for the case below

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1418 · comment 702925929 · PR 12775 · 2025-10-22

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala`

**Explicit source context (pr_title):**

> [INV-4929] feat: limit events size in inspect entity api

## A1-1403 — Correction: sequence numbers do not reset per partition

**Source stance:** explanation

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala; operation: [INV-4929] feat: limit events size in inspect entity api; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Traversal bound must multiply partition number by partition size

**Source-preserving request, proposal, or question:**

> Sorry my bad, the sequence nr doesn’t reset, so `smaller than target partition size` is incorrect. Need to times the partition nr as well

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1419 · comment 702926673 · PR 12775 · 2025-10-22

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala`

**Explicit source context (pr_title):**

> [INV-4929] feat: limit events size in inspect entity api

## A1-1404 — Use inclusive range partition logic consistently with minus one

**Source stance:** requested-change

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala; operation: [INV-4929] feat: limit events size in inspect entity api; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Same here, since we expect to query from <= events <= to, just for consistency, let’s follow same -1 logic here.
> 
> If caller specifies from = multiple of partition size, we simply return the last event of the resolved partition

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1420 · comment 703424888 · PR 12775 · 2025-10-23

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala`

**Explicit source context (pr_title):**

> [INV-4929] feat: limit events size in inspect entity api

## A1-1405 — requestedTo equal partition size belongs partition0

**Source stance:** observed-defect

**Context:**

> component: akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala; operation: [INV-4929] feat: limit events size in inspect entity api; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Compute (requestedTo-1)/targetPartitionSize

**Source-preserving request, proposal, or question:**

> If requestedTo = targetPartitionSize, this will resolve to partition 1, but actually we need partition 0.
> 
> So we need `(requestedTo - 1) / targetPartitionSize`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1421 · comment 703424196 · PR 12775 · 2025-10-23

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/persistence/inspection/dao/TypedEventDao.scala`

**Explicit source context (pr_title):**

> [INV-4929] feat: limit events size in inspect entity api

## A1-1503 — Portfolio repository queries PK portfolioId; validate tenant outside

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcRepository.scala; operation: [BB-2923] feat(advisory)(bff): adding plan upsert flow; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I’d prefer that this repository supports lookup by portfolioId - which is already the pk. Then the `validatePortfolioBelongsToTenant` can take care of the rest of validation logic

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1520 · comment 691911248 · PR 12652 · 2025-10-01

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcRepository.scala`

**Explicit source context (pr_title):**

> [BB-2923] feat(advisory)(bff): adding plan upsert flow

## A1-1600 — Store trading accounts Set instead of composite-key account component

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/jdbc/TenantPortfolioJdbcTable.scala; operation: [BB-2856] feat(advisory): tenant portfolio table; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need to keep account part of composite key? Can we just keep it as set, and key only on tenantId & portfolioId?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1616 · comment 682045789 · PR 12563 · 2025-09-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/jdbc/TenantPortfolioJdbcTable.scala`

**Explicit source context (pr_title):**

> [BB-2856] feat(advisory): tenant portfolio table

## A1-1601 — What lookup use case requires account

**Source stance:** open-question

**Context:**

> component: advisory-api/src/main/scala/com/endowus/silver/advisory/api/AdvisoryServiceE4s.scala; operation: [BB-2856] feat(advisory): tenant portfolio table; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> What is the use case to query by account?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1617 · comment 682044827 · PR 12563 · 2025-09-11

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/AdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> [BB-2856] feat(advisory): tenant portfolio table

**Evidence:** anon-1.jsonl:1617 · comment 682044827 · PR 12563 · 2025-09-11

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/AdvisoryServiceE4s.scala`

**Explicit source context (hunk):**

> +    }
> +
> +    val bulkUpsertPortfolioAssignmentByGroup: EndpointDef[BulkUpsertPortfolioAssignmentByGroupType] = {
> +      val groupId = segment[String]("groupId")
> +      endpoint(
> +        request(Post, path / "api" / "v1" / "portfolio-assignment" / "group" / groupId, jsonRequest[Seq[PortfolioAssignmentRequest]]),
> +        withStatus(ok(emptyResponse))
> +      )
> +    }

## A1-1602 — Group portfolios need mapping support too

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/jdbc/TenantPortfolioJdbcTable.scala; operation: [BB-2856] feat(advisory): tenant portfolio table; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need another table to Group level portfolios?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1618 · comment 682046083 · PR 12563 · 2025-09-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/jdbc/TenantPortfolioJdbcTable.scala`

**Explicit source context (pr_title):**

> [BB-2856] feat(advisory): tenant portfolio table

## A1-1605 — Portfolio assignment table only mapping; Explore visibility elsewhere

**Source stance:** requested-change

**Context:**

> component: advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/tenantportfolio/package.scala; operation: [BB-2856] feat(advisory): tenant portfolio table; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Hiding purchased portfolio differs from deactivation

**Source-preserving request, proposal, or question:**

> Note that once a portfolio is created and have customer buy into it, hiding from explore != deactivate it.
> 
> I’d suggest to keep this table to contain purely the mapping, and we maintain explore concern elsewhere

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1621 · comment 682128921 · PR 12563 · 2025-09-11

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/requests/tenantportfolio/package.scala`

**Explicit source context (pr_title):**

> [BB-2856] feat(advisory): tenant portfolio table

## A1-1606 — Specify both tenant and group mapping design

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/jdbc/TenantPortfolioJdbcTable.scala; operation: [BB-2856] feat(advisory): tenant portfolio table; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Can you be specific on the table design? We definitely need to maintain both tenant and group level mappings.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1622 · comment 682129650 · PR 12563 · 2025-09-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/jdbc/TenantPortfolioJdbcTable.scala`

**Explicit source context (pr_title):**

> [BB-2856] feat(advisory): tenant portfolio table

## A1-1608 — Move bulkUpsert into DbHandler; single upsert may be unnecessary

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcDbHandler.scala; operation: [BB-2856] feat(advisory): tenant portfolio table; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need this upsert? Move the bulkUpsert to DbHandler as well

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1624 · comment 682568954 · PR 12563 · 2025-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> [BB-2856] feat(advisory): tenant portfolio table

**Evidence:** anon-1.jsonl:1624 · comment 682568954 · PR 12563 · 2025-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcDbHandler.scala`

**Explicit source context (hunk):**

> +class PortfolioAssignmentJdbcDbHandler(database: Database)(implicit ctx: ExecutionContext) {
> +
> +  import PortfolioAssignmentJdbcDbHandler._
> +
> +  def bulkUpsert(requests: Seq[PortfolioAssignment]): Future[Unit] = {
> +    if (requests.isEmpty) {
> +      Future.successful(())
> +    } else {
> +      database.run(portfolioAssignments.insertOrUpdateAll(requests)).flatMap {

## A1-1609 — Repository findByTenantId/findByGroupId hide principal type

**Source stance:** requested-change

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcRepository.scala; operation: [BB-2856] feat(advisory): tenant portfolio table; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Repository can provide `findByTenantId` and `findByGroupId`  methods, so that we don’t need to keep the type out

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1625 · comment 682569194 · PR 12563 · 2025-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcRepository.scala`

**Explicit source context (pr_title):**

> [BB-2856] feat(advisory): tenant portfolio table

## A1-1610 — PK portfolioId and index ownerId to enforce one owner

**Source stance:** suggestion

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcTable.scala; operation: [BB-2856] feat(advisory): tenant portfolio table; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Sharing portfolio across groups/tenants technically possible but operationally undesirable

**Source-preserving request, proposal, or question:**

> This key suggests that same portfolioId can be shared between different tenant/group. While that is technically possible, I dont think it makes sense operationally. I think it’s better to enforce pk to be only `portfolioId` here, and add index by this onwer id instead.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1626 · comment 682569494 · PR 12563 · 2025-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcTable.scala`

**Explicit source context (pr_title):**

> [BB-2856] feat(advisory): tenant portfolio table

## A1-1611 — Can concatenate principal type and ID into one column

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcTable.scala; operation: [BB-2856] feat(advisory): tenant portfolio table; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> In theory, we also dont need 2 columns for \(type, id\). Just concat them instead?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1627 · comment 682569656 · PR 12563 · 2025-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcTable.scala`

**Explicit source context (pr_title):**

> [BB-2856] feat(advisory): tenant portfolio table

**Evidence:** anon-1.jsonl:1627 · comment 682569656 · PR 12563 · 2025-09-12

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcTable.scala`

**Explicit source context (hunk):**

> +  def principalType = column[PrincipalType]("principal_type")
> +  def principalId = column[String]("principal_id")
> +  def portfolioId = column[UUID]("portfolio_id")
> +  def fundingSources = column[Set[TradingAccountType]]("funding_sources")
> +
> +  def pk = primaryKey(PortfolioAssignmentJdbcTable.pkName, portfolioId)
> +  def principalIndex = index(name = PortfolioAssignmentJdbcTable.principalIndexName, on = principalId, unique = false)
> +
> +  override def * : ProvenShape[PortfolioAssignment] =

## A1-1612 — PrincipalId-only index may suffice versus composite

**Source stance:** open-question

**Context:**

> component: advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcTable.scala; operation: [BB-2856] feat(advisory): tenant portfolio table; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need composite index, or just principalId is sufficient?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1628 · comment 685050594 · PR 12563 · 2025-09-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcTable.scala`

**Explicit source context (pr_title):**

> [BB-2856] feat(advisory): tenant portfolio table

**Evidence:** anon-1.jsonl:1628 · comment 685050594 · PR 12563 · 2025-09-17

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/portfolioassignment/PortfolioAssignmentJdbcTable.scala`

**Explicit source context (hunk):**

> +  def portfolioId = column[UUID]("portfolio_id")
> +  def fundingSources = column[Set[TradingAccountType]]("funding_sources")
> +
> +  def pk = primaryKey(PortfolioAssignmentJdbcTable.pkName, portfolioId)
> +  def principalIndex = index(name = PortfolioAssignmentJdbcTable.principalIndexName, on = principalId, unique = false)
> +
> +  override def * : ProvenShape[PortfolioAssignment] =
> +    (
> +      principalType,

## A1-1698 — Option-returning query uses take(1) LIMIT1 even if PK already unique

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPricesJdbcRepository.scala; operation: [INV-4676] feat(marketdata): create api to get instrument daily price; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We’re querying by pk so it shouldn’t matter but generally it’s good habit to put `take(1)` \(equivalent to `LIMIT 1`\) in these queries returning Option

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1716 · comment 680227797 · PR 12510 · 2025-09-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPricesJdbcRepository.scala`

**Explicit source context (pr_title):**

> [INV-4676] feat(marketdata): create api to get instrument daily price

## A1-1719 — Use take(1).result.headOption

**Source stance:** requested-change

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/repositories/PlanRecurringTransferScheduleRepository.scala; operation: Resolve INV-4304: Add logic to trigger comms for inter-goal transfers; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> `take(1).result.headOption`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1737 · comment 675436945 · PR 12010 · 2025-08-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/repositories/PlanRecurringTransferScheduleRepository.scala`

**Explicit source context (pr_title):**

> Resolve INV-4304: Add logic to trigger comms for inter-goal transfers

**Evidence:** anon-1.jsonl:1737 · comment 675436945 · PR 12010 · 2025-08-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/repositories/PlanRecurringTransferScheduleRepository.scala`

**Explicit source context (hunk):**

> +  private val schedules = TableQuery[PlanRecurringTransferScheduleTable]
> +
> +  def findScheduleByScheduleId(scheduleId: UUID): Future[Option[PlanRecurringTransferScheduleDbItem]] = {
> +    database.run(
> +      schedules.filter(_.transferScheduleId === scheduleId).take(1).result.headOption
> +    )
> +  }
> +
> +  def streamRecurringTransferSchedulesByEndingOnDate(date: LocalDate): Source[PlanRecurringTransferScheduleDbItem, NotUsed] = {

## A1-1736 — Readside may need one source-target pair rather than duplicate In/Out schedules

**Source stance:** open-question

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringTransferScheduleTable.scala; operation: [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Other schedule data should not differ

**Source-preserving request, proposal, or question:**

> I understand we create the Out transfer schedule in source goal entity, and In transfer schedule in target goal entity. But in readside, we do need to store both of them? The source\+target pairs should be sufficient, since we do not expect the rest of data to differ between the Out/In schedules?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1754 · comment 639845795 · PR 11795 · 2025-06-02

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringTransferScheduleTable.scala`

**Explicit source context (pr_title):**

> [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base

## A1-1737 — Goal recurring-transfer table purpose unclear because trading triggers daily transfers

**Source stance:** open-question

**Context:**

> component: goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringTransferScheduleTable.scala; operation: [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> What would be the use case for this table in goal svc? I rmb the daily recurring transfers are triggered from trading svc?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1755 · comment 639846519 · PR 11795 · 2025-06-02

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringTransferScheduleTable.scala`

**Explicit source context (pr_title):**

> [INV-4302] feat(advisory, goal, trading, projection): inter-goal transfer v2 base

## A1-1817 — Delete charge rows in bounded batches within one stream

**Source stance:** requested-change

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/DailyFeeCalculationManager.scala; operation: [INV-4695] feat(charge): Charge MV & DailyFee tables; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Avoid whole-stream memory and concurrent streams; local short delete acceptable

**Source-preserving request, proposal, or question:**

> So we want to avoid collecting for whole stream and bloat the memory usage, hence I want to perform the deletion in batches within the same stream. We won’t open multiple concurrent streaming connection \+ the deletion should be short-lived & not dependent on other remote calls, this should be ok.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1837 · comment 674435397 · PR 12487 · 2025-08-26

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/DailyFeeCalculationManager.scala`

**Explicit source context (pr_title):**

> [INV-4695] feat(charge): Charge MV & DailyFee tables

## A1-1818 — Sorted stream plus in-memory groupBy documented; raw SQL still considered

**Source stance:** explanation

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/DailyFeeCalculationManager.scala; operation: [INV-4695] feat(charge): Charge MV & DailyFee tables; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I added comments to explain more on the rationale of this sorted stream \+ in-memory groupBy. Still thinking maybe we should just go with raw sql anyway, since it’s more concise, and less wasteful processing.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1838 · comment 674435597 · PR 12487 · 2025-08-26

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/DailyFeeCalculationManager.scala`

**Explicit source context (pr_title):**

> [INV-4695] feat(charge): Charge MV & DailyFee tables

## A1-1820 — Pod waits index drop/create before joining cluster

**Source stance:** explanation

**Context:**

> component: charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/JdbcSchema.scala; operation: [INV-4695] feat(charge): Charge MV & DailyFee tables; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Slow step may restart pod, not rest of cluster

**Source-preserving request, proposal, or question:**

> As discussed, new instance will wait for drop index \+ create new index to complete before moving on with other startup steps \(so it won’t join the cluster either\). If this takes too long, it might get restarted, but shouldn’t affect the rest of cluster.

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1840 · comment 674531144 · PR 12487 · 2025-08-26

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/JdbcSchema.scala`

**Explicit source context (pr_title):**

> [INV-4695] feat(charge): Charge MV & DailyFee tables

## A1-1861 — Daily data per instrument/date row instead of growing JSONB

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; operation: Feat/INV-4001 daily nav and performance; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> On 2nd thought, since our query usage will hit this often, and this daily data will be ever growing for each instrument, it’s better to store each \(instrumentId, date\) as individual rows instead of single jsonb

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1881 · comment 632166223 · PR 11805 · 2025-05-13

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-4001 daily nav and performance

## A1-1862 — Choose numeric decimal precision explicitly

**Source stance:** open-question

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentDailyReturnIndexDataTable.scala; operation: Feat/INV-4001 daily nav and performance; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> How many dp does this need to be? Do we need to override numeric type?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1882 · comment 632586710 · PR 11805 · 2025-05-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentDailyReturnIndexDataTable.scala`

**Explicit source context (pr_title):**

> Feat/INV-4001 daily nav and performance

**Evidence:** anon-1.jsonl:1882 · comment 632586710 · PR 11805 · 2025-05-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentDailyReturnIndexDataTable.scala`

**Explicit source context (hunk):**

> +      InstrumentDailyReturnIndexDataTable.TableName
> +    ) {
> +
> +  def instrumentId = column[String]("instrument_id")
> +  def dailyReturnDate = column[LocalDate]("daily_return_date")
> +  def dailyReturnValue = column[BigDecimal]("daily_return_value", O.SqlType(maxDecimalPoints))
> +  def lastUpdated = column[Instant]("last_updated_at")
> +
> +  def pk = primaryKey(InstrumentDailyReturnIndexDataTable.PkName, (instrumentId, dailyReturnDate))

## A1-1864 — Configure precision before MStar sends more dp

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentDailyReturnIndexDataTable.scala; operation: Feat/INV-4001 daily nav and performance; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Safe until one day they send more dp :rofl: ? Why don’t we just set the dp config?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1884 · comment 632588093 · PR 11805 · 2025-05-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentDailyReturnIndexDataTable.scala`

**Explicit source context (pr_title):**

> Feat/INV-4001 daily nav and performance

**Evidence:** anon-1.jsonl:1884 · comment 632588093 · PR 11805 · 2025-05-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentDailyReturnIndexDataTable.scala`

**Explicit source context (hunk):**

> +      InstrumentDailyReturnIndexDataTable.TableName
> +    ) {
> +
> +  def instrumentId = column[String]("instrument_id")
> +  def dailyReturnDate = column[LocalDate]("daily_return_date")
> +  def dailyReturnValue = column[BigDecimal]("daily_return_value", O.SqlType(maxDecimalPoints))
> +  def lastUpdated = column[Instant]("last_updated_at")
> +
> +  def pk = primaryKey(InstrumentDailyReturnIndexDataTable.PkName, (instrumentId, dailyReturnDate))

## A1-1867 — missingDates collection may OOM; use filterOpt date predicate

**Source stance:** observed-defect

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentDailyReturnIndexDataDbHandler.scala; operation: Feat/INV-4001 daily nav and performance; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This `missingDates` has the hypothetical risk of OOM if it ever gets too big
> 
> Maybe just `filterOpt(startDate)(_.dailyReturnDate >= _)` after matching instrumentId

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1887 · comment 632595032 · PR 11805 · 2025-05-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentDailyReturnIndexDataDbHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-4001 daily nav and performance

## A1-1869 — Latest-date query or DB join/stream instead of per-row lookup

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: Feat/INV-4001 daily nav and performance; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Add a method to return latest date for given instrument? You can also join and stream from db directly, instead of streaming from one table, and lookup for each of them

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1889 · comment 632690060 · PR 11805 · 2025-05-14

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> Feat/INV-4001 daily nav and performance

## A1-1870 — Remove Cassandra PortfolioRepository after PG migration

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/db/PortfolioRepository.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Concern stated in the source:** Data side already PG

**Source-preserving request, proposal, or question:**

> Let’s check again but this `PortfolioRepository` should not be used anymore \(and if it is, we can migrate to the pg version\)
> 
> Then we can get rid of all these tables & projection code. Data side has already switched to pg

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1890 · comment 632601882 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/entities/portfolio/db/PortfolioRepository.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

## A1-1878 — streamAll directly from DB instead of memory-loaded stream

**Source stance:** requested-change

**Context:**

> component: portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala; operation: [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s add streamAll method so that we can stream directly from DB, instead of querying everything into memory then stream from memory

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1898 · comment 632778581 · PR 11812 · 2025-05-14

Source path: `portfolio-impl/src/main/scala/com/endowus/silver/portfolio/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-4190] feat(instrument, portfolio): remove instrument entity from portfolio

## A1-1911 — Query manual prices in PG instead of loading all in memory

**Source stance:** requested-change

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; operation: [INV-4569] feat(marketdata): support source of price update; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> I think we can do this query in PG so that we don’t have to load all prices into memory just to find a few manual entries

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:1931 · comment 664715564 · PR 12355 · 2025-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-4569] feat(marketdata): support source of price update

## A1-1914 — Question need for declaration not persisted as separate column; exact field unspecified

**Source stance:** open-question

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/MarketdataPostgresProfile.scala; operation: [INV-4569] feat(marketdata): support source of price update; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Do we need this? We don’t persist it as separate column right?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- No reliably located hunk excerpt is available for this terse comment; its target remains limited to the path and PR context.

**Evidence:** anon-1.jsonl:1934 · comment 665708620 · PR 12355 · 2025-08-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/MarketdataPostgresProfile.scala`

**Explicit source context (pr_title):**

> [INV-4569] feat(marketdata): support source of price update

## A1-1924 — Extract JSON path priceSource _type via #>> List

**Source stance:** suggestion

**Context:**

> component: marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPricesJdbcRepository.scala; operation: [INV-4569] feat(marketdata): support source of price update; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> We can extract in one go using `#>> List("priceSource", "_type")` I think

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1944 · comment 665709306 · PR 12355 · 2025-08-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPricesJdbcRepository.scala`

**Explicit source context (pr_title):**

> [INV-4569] feat(marketdata): support source of price update

**Evidence:** anon-1.jsonl:1944 · comment 665709306 · PR 12355 · 2025-08-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPricesJdbcRepository.scala`

**Explicit source context (hunk):**

> +          .filter(_.dailyPrice.asColumnOf[JsValue] #>> List("priceSource", "_type") === Manual.toString)
> +          .result
> +      )
> +      .map(_.toList)
>    }
>  
>    def retrieveLatestPrice(instrumentId: String, priceCcy: CurrencyUnit): Future[Option[InstrumentDailyPriceVo]] = {

## A1-1937 — Transaction updated_at uses Instant rather than ZonedDateTime

**Source stance:** requested-change

**Context:**

> component: transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionVo.scala; operation: TT-6084 add updated_at column to transaction table; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s stick with Instant instead of `ZonedDateTime`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.
- Hunk excerpt is context, not comment text. It is mechanically located near the source inline line and can reflect a later revision; it does not settle an open review question.

**Evidence:** anon-1.jsonl:1958 · comment 628758686 · PR 11755 · 2025-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionVo.scala`

**Explicit source context (pr_title):**

> TT-6084 add updated_at column to transaction table

**Evidence:** anon-1.jsonl:1958 · comment 628758686 · PR 11755 · 2025-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionVo.scala`

**Explicit source context (hunk):**

> goalId: Option[UUID],
>    planId: Option[UUID],
> -  transactionData: Transaction
> +  transactionData: Transaction,
> +  updatedAt: Option[Instant],
>  )
>  
>  object TransactionVo {

## A1-2002 — Use RebalancePlan repository streamActivePlansByPortfolioId with effectiveDate

**Source stance:** requested-change

**Context:**

> component: rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/db/plan/PortfolioPlansTable.scala; operation: [INV-1946] feat(rebalance): remove taa entity; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Let’s use existing RebalancePlan table
> 
> Will need to add another method to `RebalancePlanJdbcRepository` to support `streamActivePlansByPortfolioId(portfolioId, effectiveDate)`

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2021 · comment 652296958 · PR 12157 · 2025-07-02

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/db/plan/PortfolioPlansTable.scala`

**Explicit source context (pr_title):**

> [INV-1946] feat(rebalance): remove taa entity

## A1-2020 — Explicit instrumentId query instead of per-instrument unindexed scan

**Source stance:** requested-change

**Context:**

> component: composition-impl/src/main/scala/com/endowus/silver/composition/impl/utils/MstarDataDownloader.scala; operation: [INV-3999] feat(composition): pull mstar data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> Hmm it’s wasteful to call this \(note the no index query\) for every instrument. Why don’t we check just check for the instrumentId explicitly?

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2039 · comment 655841830 · PR 12004 · 2025-07-11

Source path: `composition-impl/src/main/scala/com/endowus/silver/composition/impl/utils/MstarDataDownloader.scala`

**Explicit source context (pr_title):**

> [INV-3999] feat(composition): pull mstar data

## A1-2023 — Use insert not insertOrUpdate to catch initial-state race

**Source stance:** requested-change

**Context:**

> component: composition-impl/src/main/scala/com/endowus/silver/composition/impl/db/jdbc/instrumentData/InstrumentDataJdbcDbHandler.scala; operation: [INV-3999] feat(composition): pull mstar data; trigger: Source-specific review condition as stated in the exact comment below.

**Source-preserving request, proposal, or question:**

> This needs to call `insert` instead of `insertOrUpdate`, otherwise you won’t be able to catch the race condition when initial state is empty

**Conditions and limits:**

- Context component is inline_path metadata; operation is the exact PR title quoted separately from comment evidence.

**Evidence:** anon-1.jsonl:2042 · comment 655807098 · PR 12004 · 2025-07-11

Source path: `composition-impl/src/main/scala/com/endowus/silver/composition/impl/db/jdbc/instrumentData/InstrumentDataJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> [INV-3999] feat(composition): pull mstar data

## A2-0028 — PlanProfileJdbcProjectionV3: Since we have the full PlanProfile in the `PlanProfileTenantIdBackFilledEvt`, let’s use it directly instead of fetching from entity again.

**Source stance:** explanation

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/PlanProfileJdbcProjectionV3.scala; original row 28.

**Concern stated in the source:** The event already contains the full PlanProfile; fetching entity state again is unnecessary for this event.

**Source-preserving request, proposal, or question:**

> Since we have the full PlanProfile in the `PlanProfileTenantIdBackFilledEvt`, let’s use it directly instead of fetching from entity again.
> 
> One day we need to for all these existing events as well, to have separate update query for them that doesn’t rely on fetching whole PlanProfile

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:28 · comment 609335815 · PR 11333 · 2025-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/PlanProfileJdbcProjectionV3.scala`

**Evidence:** anon-2.jsonl:28 · comment 609335815 · PR 11333 · 2025-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/PlanProfileJdbcProjectionV3.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0029 — FeeChargeRequestJdbcProjectionV6: I think we can let DB take care of both the query and update. Something like `UPDATE feeChargeRequests SET tenantId WHERE customerId, planId`

**Source stance:** suggestion

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala; original row 29.

**Source-preserving request, proposal, or question:**

> I think we can let DB take care of both the query and update. Something like `UPDATE feeChargeRequests SET tenantId WHERE customerId, planId`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:29 · comment 609335884 · PR 11333 · 2025-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala`

**Evidence:** anon-2.jsonl:29 · comment 609335884 · PR 11333 · 2025-03-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0030 — FeeChargeRequestJdbcProjectionV6: There’s no need to query this anymore. The `updateTenantId` takes care of all requests with matching customerId/planId

**Source stance:** explanation

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala; original row 30.

**Concern stated in the source:** updateTenantId already covers requests matching customerId/planId.

**Source-preserving request, proposal, or question:**

> There’s no need to query this anymore. The `updateTenantId` takes care of all requests with matching customerId/planId

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:30 · comment 609630992 · PR 11333 · 2025-03-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala`

**Evidence:** anon-2.jsonl:30 · comment 609630992 · PR 11333 · 2025-03-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcProjectionV6.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0031 — BackfillPlanProfileTenantIdTaskTopicSubscriber: I realize we could have made the task keyed by customerId instead, then in this subscriber, we query planProfiles by customerId a...

**Source stance:** suggestion

**Context:**

> PR 11333 ([EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala; original row 31.

**Source-preserving request, proposal, or question:**

> I realize we could have made the task keyed by customerId instead, then in this subscriber, we query planProfiles by customerId and invoke the cmd as usual. It’s one time exercise so this is ok too

**Conditions and limits:**

- The customerId-keyed alternative is explicitly considered optional because this is a one-time exercise.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:31 · comment 609631484 · PR 11333 · 2025-03-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:31 · comment 609631484 · PR 11333 · 2025-03-17

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/task/BackfillPlanProfileTenantIdTaskTopicSubscriber.scala`

**Explicit source context (pr_title):**

> [EN-4538] (charge) Backfill tenant id in plan profile and charge requests table, and ensure tenant id is populated for new plan profiles

## A2-0033 — CommunicationContext: These default fallback looks wrong. Since in theory we can’t reliably fallback without locale \(or TranslationContext\)

**Source stance:** suggestion

**Context:**

> PR 11207 ([EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2), communication-api/src/main/scala/com/endowus/silver/communication/api/context/CommunicationContext.scala; original row 33.

**Concern stated in the source:** Fallback translation cannot reliably work without locale/TranslationContext; translated values should be populated before toSendgridData.

**Source-preserving request, proposal, or question:**

> These default fallback looks wrong. Since in theory we can’t reliably fallback without locale \(or TranslationContext\)
> 
> By the time `communication` svc calls `toSendgridData`, all `translated`values must be populated already, and if not, it is a bug.
> 
> I suppose we can leave these for now, they are only here temporarily until we complete the migration.

**Conditions and limits:**

- Temporary default fallbacks are allowed to remain until migration completes, despite being described as unreliable.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:33 · comment 610633400 · PR 11207 · 2025-03-19

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/context/CommunicationContext.scala`

**Evidence:** anon-2.jsonl:33 · comment 610633400 · PR 11207 · 2025-03-19

Source path: `communication-api/src/main/scala/com/endowus/silver/communication/api/context/CommunicationContext.scala`

**Explicit source context (pr_title):**

> [EN-4396] feat(redemption)(communication) Support B2B redemption emails and migrate to Communicator V2

## A2-0062 — TagTransactionAdvisoryClassification: So why don’t we just start with endpoint that queries v3 repo directly? Why do we query v2 repo, then query again with v3?

**Source stance:** requested-change

**Context:**

> PR 8453 (Feat/INV-2101 transaction backfill scripts), amend-scripts/src/main/scala/transaction/TagTransactionAdvisoryClassification.scala; original row 62.

**Source-preserving request, proposal, or question:**

> So why don’t we just start with endpoint that queries v3 repo directly? Why do we query v2 repo, then query again with v3?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:62 · comment 476110956 · PR 8453 · 2024-02-27

Source path: `amend-scripts/src/main/scala/transaction/TagTransactionAdvisoryClassification.scala`

**Evidence:** anon-2.jsonl:62 · comment 476110956 · PR 8453 · 2024-02-27

Source path: `amend-scripts/src/main/scala/transaction/TagTransactionAdvisoryClassification.scala`

**Explicit source context (pr_title):**

> Feat/INV-2101 transaction backfill scripts

## A2-0076 — FixV3DividendsTransactions: Let’s also add which query we use to arrive at the dataset

**Source stance:** requested-change

**Context:**

> PR 7209 ([INV-1976] feat(amend): Scripts to amend dividends, redemption and deleted order transactions), amend-scripts/src/main/scala/transaction/FixV3DividendsTransactions.scala; original row 76.

**Source-preserving request, proposal, or question:**

> Let’s also add which query we use to arrive at the dataset

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:76 · comment 436522244 · PR 7209 · 2023-10-17

Source path: `amend-scripts/src/main/scala/transaction/FixV3DividendsTransactions.scala`

**Evidence:** anon-2.jsonl:76 · comment 436522244 · PR 7209 · 2023-10-17

Source path: `amend-scripts/src/main/scala/transaction/FixV3DividendsTransactions.scala`

**Explicit source context (pr_title):**

> [INV-1976] feat(amend): Scripts to amend dividends, redemption and deleted order transactions

## A2-0078 — FixV3DividendsTransactions: Why don’t we add more filter here, to reduce the payload size? Also maybe groupBy customerId so that we don’t repeat the query again?

**Source stance:** suggestion

**Context:**

> PR 7209 ([INV-1976] feat(amend): Scripts to amend dividends, redemption and deleted order transactions), amend-scripts/src/main/scala/transaction/FixV3DividendsTransactions.scala; original row 78.

**Concern stated in the source:** Repeated queries and oversized payloads may be avoided by additional filters and grouping by customerId.

**Source-preserving request, proposal, or question:**

> Why don’t we add more filter here, to reduce the payload size? Also maybe groupBy customerId so that we don’t repeat the query again?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:78 · comment 436531435 · PR 7209 · 2023-10-17

Source path: `amend-scripts/src/main/scala/transaction/FixV3DividendsTransactions.scala`

**Evidence:** anon-2.jsonl:78 · comment 436531435 · PR 7209 · 2023-10-17

Source path: `amend-scripts/src/main/scala/transaction/FixV3DividendsTransactions.scala`

**Explicit source context (pr_title):**

> [INV-1976] feat(amend): Scripts to amend dividends, redemption and deleted order transactions

## A2-0190 — BffServiceE4s: Can merge `getGoalCreateTasksByCreatorPendingManager` and `getGoalCreateTasksByCreatorPendingClient` by making FE send `assigneeRole` as query param

**Source stance:** suggestion

**Context:**

> PR 10647 (Feat/AD-2007 b2b approvals bff), bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala; original row 190.

**Source-preserving request, proposal, or question:**

> Can merge `getGoalCreateTasksByCreatorPendingManager` and `getGoalCreateTasksByCreatorPendingClient` by making FE send `assigneeRole` as query param
> 
> So we will 2 EndpointType
> 
> * `GetTasksByCreatorType`
> * `GetTasksByAssigneeType`
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:190 · comment 583101754 · PR 10647 · 2025-01-07

Source path: `bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala`

**Evidence:** anon-2.jsonl:190 · comment 583101754 · PR 10647 · 2025-01-07

Source path: `bff-api/src/main/scala/com/endowus/silver/bff/api/BffServiceE4s.scala`

**Explicit source context (pr_title):**

> Feat/AD-2007 b2b approvals bff

## A2-0230 — RebalancePlanTableV4: Remove all the index on customerId/goalId/tradingAccountType/planCcy - we don’t use them at all.

**Source stance:** explanation

**Context:**

> PR 10592 ([INV-3707] feat(rebalance): Support blacklisting auto-rebalance for specific plan), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalancePlanTableV4.scala; original row 230.

**Concern stated in the source:** customerId/goalId/tradingAccountType/planCcy indices are unused; portfolioId is anticipated for TAA entity removal.

**Source-preserving request, proposal, or question:**

> Remove all the index on customerId/goalId/tradingAccountType/planCcy - we don’t use them at all.
> 
> Add index on portfolioId in anticipation for removal of TAA entity

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:230 · comment 576285462 · PR 10592 · 2024-12-10

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalancePlanTableV4.scala`

**Evidence:** anon-2.jsonl:230 · comment 576285462 · PR 10592 · 2024-12-10

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalancePlanTableV4.scala`

**Explicit source context (pr_title):**

> [INV-3707] feat(rebalance): Support blacklisting auto-rebalance for specific plan

## A2-0236 — InvestmentPlanTableV8: This index is too much I would think. So most of the use cases of recurring investment, I think index on the `NextUpcomingDate` is sufficient. Other condi...

**Source stance:** suggestion

**Context:**

> PR 10251 (Resolve INV-3613: Goal/investment ceate new read side tables), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV8.scala; original row 236.

**Concern stated in the source:** NextUpcomingDate is considered sufficient indexing for recurring investment use cases; other filters can stream/process in memory.

**Source-preserving request, proposal, or question:**

> This index is too much I would think. So most of the use cases of recurring investment, I think index on the `NextUpcomingDate` is sufficient. Other condition, I feel we can just stream and process in stream/memory. No need to expose other columns here

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:236 · comment 560694743 · PR 10251 · 2024-11-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV8.scala`

**Evidence:** anon-2.jsonl:236 · comment 560694743 · PR 10251 · 2024-11-04

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV8.scala`

**Explicit source context (pr_title):**

> Resolve INV-3613: Goal/investment ceate new read side tables

## A2-0237 — GoalTableV4: Do we need all these colums?

**Source stance:** open-question

**Context:**

> PR 10251 (Resolve INV-3613: Goal/investment ceate new read side tables), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalTableV4.scala; original row 237.

**Source-preserving request, proposal, or question:**

> Do we need all these colums?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- The comment questions GoalTableV4 columns but does not list a definitive required projection.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:237 · comment 560695498 · PR 10251 · 2024-11-04

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalTableV4.scala`

**Evidence:** anon-2.jsonl:237 · comment 560695498 · PR 10251 · 2024-11-04

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalTableV4.scala`

**Explicit source context (hunk):**

> +  def pk = primaryKey(GoalTableV4.PrimaryKeyName, goalId)
> +  def indexCustomerId = index(name = GoalTableV4.CustomerIdIndex, on = customerId, unique = false)
> +
> +  override def * : ProvenShape[GoalData] =
> +    (
> +      goalId,
> +      customerId,

**Evidence:** anon-2.jsonl:237 · comment 560695498 · PR 10251 · 2024-11-04

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalTableV4.scala`

**Explicit source context (pr_title):**

> Resolve INV-3613: Goal/investment ceate new read side tables

## A2-0282 — PlanFeeInstructionEntity: The entity state is default with empty fee instructions, it means the plan always exists, just without any data. Modelling it this way means you can’t ...

**Source stance:** open-question

**Context:**

> PR 10030 ([EN-3952] (charge) Create new PlanFeeInstructionEntity), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala; original row 282.

**Concern stated in the source:** Empty default instructions cannot distinguish never-initialized from upserted-then-deleted plan state.

**Source-preserving request, proposal, or question:**

> The entity state is default with empty fee instructions, it means the plan always exists, just without any data. Modelling it this way means you can’t distinguish between a uninitialized plan vs a plan with upserted-then-deleted fee instructions.
> 
> If we care enough about this, then we probably should make state a sealed trait, default with case object NotInitialized, otherwise it’s case class Initialized\(feeInstructions\). Then you can throw for GetCmd/DeleteCmd on NotInitialized. And no-op without error if deleting already deleted fee instruction for Initialized, and even throw if deleting last entry for Initialized \(to ensure there’s always an entry to support the fee rate query\)

**Conditions and limits:**

- The sealed NotInitialized/Initialized state is conditional on caring about that distinction; no-op deletion and last-entry rejection are proposals within that model.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:282 · comment 552218834 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Evidence:** anon-2.jsonl:282 · comment 552218834 · PR 10030 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/instruction/PlanFeeInstructionEntity.scala`

**Explicit source context (pr_title):**

> [EN-3952] (charge) Create new PlanFeeInstructionEntity

## A2-0284 — TenantFeeRangeConfigHistoryTable: Let’s just store jsonb `FeeRange` for history as well?

**Source stance:** suggestion

**Context:**

> PR 9952 ([EN-3951] (charge) Add apis and table for Range configuration setup), charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/feerange/jdbc/TenantFeeRangeConfigHistoryTable.scala; original row 284.

**Source-preserving request, proposal, or question:**

> Let’s just store jsonb `FeeRange` for history as well?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:284 · comment 552087439 · PR 9952 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/feerange/jdbc/TenantFeeRangeConfigHistoryTable.scala`

**Evidence:** anon-2.jsonl:284 · comment 552087439 · PR 9952 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/feerange/jdbc/TenantFeeRangeConfigHistoryTable.scala`

**Explicit source context (pr_title):**

> [EN-3951] (charge) Add apis and table for Range configuration setup

## A2-0285 — TenantFeeRangeConfigDaoJdbc: Do we need to capture “deleted-by” in the `lastUpdatedBy` field?

**Source stance:** open-question

**Context:**

> PR 9952 ([EN-3951] (charge) Add apis and table for Range configuration setup), charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/feerange/jdbc/TenantFeeRangeConfigDaoJdbc.scala; original row 285.

**Source-preserving request, proposal, or question:**

> Do we need to capture “deleted-by” in the `lastUpdatedBy` field?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:285 · comment 552087866 · PR 9952 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/feerange/jdbc/TenantFeeRangeConfigDaoJdbc.scala`

**Evidence:** anon-2.jsonl:285 · comment 552087866 · PR 9952 · 2024-10-14

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/feerange/jdbc/TenantFeeRangeConfigDaoJdbc.scala`

**Explicit source context (pr_title):**

> [EN-3951] (charge) Add apis and table for Range configuration setup

## A2-0299 — Review: Reported config-endpoint verification: cassandra-query-journal/events-by-tag/eventual-consistency-delay returned 20s before the environment override and 7s afterward. Po...

**Source stance:** reported-verification

**Context:**

> PR 10485 ([INV-3738] feat(common): Make eventual-consistency-delay configurable), no inline path; original row 299.

**Concern stated in the source:** The config endpoint reported 20s before the override and 7s after.

**Source-preserving request, proposal, or question:**

> Reported config-endpoint verification: cassandra-query-journal/events-by-tag/eventual-consistency-delay returned 20s before the environment override and 7s afterward. Pod identifiers are incidental.

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

> Before override env var

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

> localhost:10002/config/cassandra-query-journal/events-by-tag/eventual-consistency-delay

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

> 20s

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

> After

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

> 7s

**Evidence:** anon-2.jsonl:299 · comment 571849321 · PR 10485 · 2024-11-29

**Explicit source context (pr_title):**

> [INV-3738] feat(common): Make eventual-consistency-delay configurable

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

## A2-0313 — RecurringInvestmentScheduleHistoryDataEventProcessorV3: `PlanRecurringInvestmentScheduleHistoryTableV3` stores the history audit entries, so we can’t rely on this backfill evt t...

**Source stance:** explanation

**Context:**

> PR 10417 (Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessorV3.scala; original row 313.

**Concern stated in the source:** History audit entries cannot be repaired eventually by a new backfill event, unlike the current schedule table.

**Source-preserving request, proposal, or question:**

> `PlanRecurringInvestmentScheduleHistoryTableV3` stores the history audit entries, so we can’t rely on this backfill evt to correct the data eventually \(unlike `PlanRecurringInvestmentScheduleTableV3`\). The fallback logic must continue to stay even in newer table version \(or we add fallback logic to the db model `PlanRecurringInvestmentScheduleHistory` instead\)
> 
> But regardless, it seems we don’t need to handle backfill evt in the history projection

**Conditions and limits:**

- Keep investmentAmount→fundingInstructions fallback in newer history table versions, or move it to the PlanRecurringInvestmentScheduleHistory DB model. Do not infer backfill eventually fixes audit history.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:313 · comment 570860367 · PR 10417 · 2024-11-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessorV3.scala`

**Evidence:** anon-2.jsonl:313 · comment 570860367 · PR 10417 · 2024-11-27

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryDataEventProcessorV3.scala`

**Explicit source context (pr_title):**

> Resolve INV-3702: New events and handlers to retrospectively update initial investment request and recurring funding instructions.

## A2-0339 — GoalSupportingDataTableV1: How does this work when there are multiple actions on a goal?

**Source stance:** open-question

**Context:**

> PR 10335 (Feat/INV-3508 goal create projections), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala; original row 339.

**Concern stated in the source:** Handling multiple actions on one goal is not explained.

**Source-preserving request, proposal, or question:**

> How does this work when there are multiple actions on a goal?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:339 · comment 564012590 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala`

**Evidence:** anon-2.jsonl:339 · comment 564012590 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create projections

## A2-0346 — GoalEventProcessor: We split new projection, inject `WorkflowEngineServiceSg` and wire it only for SG

**Source stance:** suggestion

**Context:**

> PR 10335 (Feat/INV-3508 goal create projections), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalEventProcessor.scala; original row 346.

**Concern stated in the source:** New SG workflow projections/tables should be wired only in SG until HK approval support exists.

**Source-preserving request, proposal, or question:**

> We split new projection, inject `WorkflowEngineServiceSg` and wire it only for SG
> 
> Tmr when we have approval in HK, change `WorkflowEngineServiceSg` to Base, wire in HK as well.. but further logic changes
> 
> ‌
> 
> Same for table, design is region agnostic, but we wire SG only

**Conditions and limits:**

- HK wiring is a future change requiring a base client and further logic changes; the schema itself is region agnostic.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:346 · comment 564025895 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalEventProcessor.scala`

**Evidence:** anon-2.jsonl:346 · comment 564025895 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/GoalEventProcessor.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create projections

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

## A2-0350 — GoalSupportingDataTableV1: Needs to be composite \(`goalId`, `goalActionContext`, `createdAt`\)

**Source stance:** suggestion

**Context:**

> PR 10335 (Feat/INV-3508 goal create projections), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala; original row 350.

**Concern stated in the source:** The requested key is composite (goalId, goalActionContext, createdAt); GoalSupportingData is a sealed trait.

**Source-preserving request, proposal, or question:**

> Needs to be composite \(`goalId`, `goalActionContext`, `createdAt`\)
> 
> column of GoalSupportingData
> 
> ```
> sealed trait GoalSupportingData {
>   def documentIds: List[UUID]
> }
> 
> case class TaskApprovalDetailsData(details: TaskApprovalDetails) extends GoalSupportingData {
>   def documentIds: List[UUID] = details.documentIds
> }
> 
> case class DirectDocs<blah>(documentIds: List[UUID]) extends GoalSupportingData
> ```
> 
> ‌

**Conditions and limits:**

- Keep this composite-key proposal separate from the later auto-increment/index proposal in row 358.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:350 · comment 564024165 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala`

**Evidence:** anon-2.jsonl:350 · comment 564024165 · PR 10335 · 2024-11-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create projections

## A2-0358 — GoalSupportingDataTableV1: Let’s try auto increment id and index on goalId

**Source stance:** suggestion

**Context:**

> PR 10335 (Feat/INV-3508 goal create projections), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala; original row 358.

**Source-preserving request, proposal, or question:**

> Let’s try auto increment id and index on goalId

**Conditions and limits:**

- Source proposes an auto-increment id with goalId index, distinct from row 350 composite-key suggestion.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:358 · comment 564837941 · PR 10335 · 2024-11-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala`

**Evidence:** anon-2.jsonl:358 · comment 564837941 · PR 10335 · 2024-11-14

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataTableV1.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create projections

## A2-0365 — GoalSupportingDataJdbcDbHandler: I suppose this would return 0, if row already exists? Do we log error or something cuz we don’t expect that to happen?

**Source stance:** open-question

**Context:**

> PR 10335 (Feat/INV-3508 goal create projections), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataJdbcDbHandler.scala; original row 365.

**Concern stated in the source:** An unexpected duplicate insert returning 0 may need error logging; outcome remains a question.

**Source-preserving request, proposal, or question:**

> I suppose this would return 0, if row already exists? Do we log error or something cuz we don’t expect that to happen?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:365 · comment 565310581 · PR 10335 · 2024-11-15

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataJdbcDbHandler.scala`

**Evidence:** anon-2.jsonl:365 · comment 565310581 · PR 10335 · 2024-11-15

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create projections

## A2-0367 — GoalSupportingDataJdbcDbHandler: Need index on goalId?

**Source stance:** open-question

**Context:**

> PR 10335 (Feat/INV-3508 goal create projections), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataJdbcDbHandler.scala; original row 367.

**Source-preserving request, proposal, or question:**

> Need index on goalId?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:367 · comment 565325170 · PR 10335 · 2024-11-15

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataJdbcDbHandler.scala`

**Evidence:** anon-2.jsonl:367 · comment 565325170 · PR 10335 · 2024-11-15

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/GoalSupportingDataJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3508 goal create projections

## A2-0371 — InstrumentBalanceRepository: ```

**Source stance:** explanation

**Context:**

> PR 10367 ([INV-3683] feat(goal)(trading): Validate empty goal & no pending trades/transfers before goal deactivation), trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/db/instrumentBalance/InstrumentBalanceRepository.scala; original row 371.

**Concern stated in the source:** Cassandra access must specify at least customerId, the partition key, to avoid an unsafe scan.

**Source-preserving request, proposal, or question:**

> ```
> PRIMARY KEY((customerId), planId, broker, accountNumber, instrumentId)
> ```
> 
> Very important to specify at least `customerId` otherwise we might cause blow up in Cassandra

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:371 · comment 564825467 · PR 10367 · 2024-11-14

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/db/instrumentBalance/InstrumentBalanceRepository.scala`

**Evidence:** anon-2.jsonl:371 · comment 564825467 · PR 10367 · 2024-11-14

Source path: `trading-impl/src/main/scala/com/endowus/silver/trading/impl/entities/plan/db/instrumentBalance/InstrumentBalanceRepository.scala`

**Explicit source context (pr_title):**

> [INV-3683] feat(goal)(trading): Validate empty goal & no pending trades/transfers before goal deactivation

## A2-0414 — BaseAdvisoryServiceE4s: Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for c...

**Source stance:** suggestion

**Context:**

> PR 10182 ([INV-3430] feat(bff, advisory): Portfolio Builder Fund List), advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala; original row 414.

**Concern stated in the source:** Tenant-specific APIs can use tenant tracing context after BFF auth/RBAC; faId is unnecessary until any future FA-specific RF need.

**Source-preserving request, proposal, or question:**

> Should we create another API object for all these tenant specific endpoints? Their logic should extract the tenant from tracing context, and use it for corp profile lookup.
> 
> This means for now, we do not need to have `faId` in the query params. On BFF, it would be an authenticated proxy endpoints with appropriate RBAC resource. Once that passes, `advisory` just need to proceed with the tenantId.
> 
> In future, if we ever need to support fa specific RF, an optional `faId` can be added?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:414 · comment 558075298 · PR 10182 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Evidence:** anon-2.jsonl:414 · comment 558075298 · PR 10182 · 2024-10-28

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/BaseAdvisoryServiceE4s.scala`

**Explicit source context (pr_title):**

> [INV-3430] feat(bff, advisory): Portfolio Builder Fund List

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

## A2-0469 — BffServiceImpl: In on-behalf operations:

**Source stance:** suggestion

**Context:**

> PR 10258 ([INV-3639] feat(bff): Capture and propagate Customer/Employee context in BFF), bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala; original row 469.

**Concern stated in the source:** In on-behalf operations:

* auth user would be employee, which we would set into context using EmployeeProvider
* and the request \(either payload or query param\) should specify the customer, which we would use to validate proper ownership/relationship in guards

‌

Once it reaches the handler \(logic layer\), it is up to the domain to decide how they want to implement it. Example:

1. they could use an endpoint in BE that expects customerId in either payload or query param \(and hence we can simply reuse it completely, and define it as proxy endpoint in BFF\)
2. they could set context using CustomerProvider, and call the endpoint in BE that expects customerId from context instead \(and if not available, 500 error is rightfully thrown\)

I would prefer \(1\) instead and we stick to setting TenantId/CustomerId/EmployeeId context by auth only.

**Source-preserving request, proposal, or question:**

> In on-behalf operations:
> 
> * auth user would be employee, which we would set into context using EmployeeProvider
> * and the request \(either payload or query param\) should specify the customer, which we would use to validate proper ownership/relationship in guards
> 
> ‌
> 
> Once it reaches the handler \(logic layer\), it is up to the domain to decide how they want to implement it. Example:
> 
> 1. they could use an endpoint in BE that expects customerId in either payload or query param \(and hence we can simply reuse it completely, and define it as proxy endpoint in BFF\)
> 2. they could set context using CustomerProvider, and call the endpoint in BE that expects customerId from context instead \(and if not available, 500 error is rightfully thrown\)
> 
> I would prefer \(1\) instead and we stick to setting TenantId/CustomerId/EmployeeId context by auth only.

**Conditions and limits:**

- Two on-behalf designs are presented; the preferred one leaves auth context tied to authentication and sends target customerId explicitly in payload/query.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:469 · comment 560709898 · PR 10258 · 2024-11-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala`

**Evidence:** anon-2.jsonl:469 · comment 560709898 · PR 10258 · 2024-11-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala`

**Explicit source context (pr_title):**

> [INV-3639] feat(bff): Capture and propagate Customer/Employee context in BFF

## A2-0476 — BffServiceImpl: Ok so my above example would be when FA performs operation on-behalf of customer, so employee would be there.

**Source stance:** suggestion

**Context:**

> PR 10258 ([INV-3639] feat(bff): Capture and propagate Customer/Employee context in BFF), bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala; original row 476.

**Concern stated in the source:** Ok so my above example would be when FA performs operation on-behalf of customer, so employee would be there.

For same endpoint to support PartnerOps user, I will need to change this `manageCustomer` guard’s logic:

* extract customerId from endpoint request properties
* query `tenantClient <- tenantService.Api.getClientById()(customerId)`
* validate:

    * if `requestWithAuthResponse.employeeIdFromToken` is available, its value must match `tenantClient.managerId`
    * else `requestWithAuthResponse.authResponse.identity.issuer.tenant.id` must match `tenantClient.tenantId`
    

‌

**Source-preserving request, proposal, or question:**

> Ok so my above example would be when FA performs operation on-behalf of customer, so employee would be there.
> 
> For same endpoint to support PartnerOps user, I will need to change this `manageCustomer` guard’s logic:
> 
> * extract customerId from endpoint request properties
> * query `tenantClient <- tenantService.Api.getClientById()(customerId)`
> * validate:
> 
>     * if `requestWithAuthResponse.employeeIdFromToken` is available, its value must match `tenantClient.managerId`
>     * else `requestWithAuthResponse.authResponse.identity.issuer.tenant.id` must match `tenantClient.tenantId`
>     
> 
> ‌

**Conditions and limits:**

- Employee token branch must match managerId; otherwise authenticated identity tenant must match tenantClient.tenantId.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:476 · comment 560738494 · PR 10258 · 2024-11-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala`

**Evidence:** anon-2.jsonl:476 · comment 560738494 · PR 10258 · 2024-11-04

Source path: `bff-impl/src/main/scala/com/endowus/silver/bff/impl/BffServiceImpl.scala`

**Explicit source context (pr_title):**

> [INV-3639] feat(bff): Capture and propagate Customer/Employee context in BFF

## A2-0484 — PortfolioStatsJdbcTable: I don’t create these index in V2:

**Source stance:** explanation

**Context:**

> PR 10219 ([INV-3618] feat(projection)(performance): Add validation for PortfolioStats to be older than 2007 before generating simulation result), projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcTable.scala; original row 484.

**Concern stated in the source:** I don’t create these index in V2:

* portfolioId: 1st field in composite pk, no need additional index
* effectiveDate: not very useful field to query alone without portfolioId
* statsCcy: not very good field to index, as we only have a handful of ccy

‌

**Source-preserving request, proposal, or question:**

> I don’t create these index in V2:
> 
> * portfolioId: 1st field in composite pk, no need additional index
> * effectiveDate: not very useful field to query alone without portfolioId
> * statsCcy: not very good field to index, as we only have a handful of ccy
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:484 · comment 556612117 · PR 10219 · 2024-10-23

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcTable.scala`

**Evidence:** anon-2.jsonl:484 · comment 556612117 · PR 10219 · 2024-10-23

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcTable.scala`

**Explicit source context (pr_title):**

> [INV-3618] feat(projection)(performance): Add validation for PortfolioStats to be older than 2007 before generating simulation result

## A2-0489 — HkAdvisedPortfolioOfferingsManager: Let’s set effectiveDate as well, for all these query using portfolioId

**Source stance:** suggestion

**Context:**

> PR 10077 ([INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkAdvisedPortfolioOfferingsManager.scala; original row 489.

**Concern stated in the source:** Let’s set effectiveDate as well, for all these query using portfolioId

**Source-preserving request, proposal, or question:**

> Let’s set effectiveDate as well, for all these query using portfolioId

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:489 · comment 551482637 · PR 10077 · 2024-10-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkAdvisedPortfolioOfferingsManager.scala`

**Evidence:** anon-2.jsonl:489 · comment 551482637 · PR 10077 · 2024-10-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkAdvisedPortfolioOfferingsManager.scala`

**Explicit source context (pr_title):**

> [INV-3441] feat(composition): use instrument EndowusAssetClassType map to calculate taa and aaa

## A2-0559 — DistributionCalculatorHelperHk: Pagination will actually run the query twice \(count and actual result\). Best if we simply add an endpoint for this

**Source stance:** suggestion

**Context:**

> PR 10121 (TT-5089 remove cache customer status for HK trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculatorHelperHk.scala; original row 559.

**Concern stated in the source:** Pagination will actually run the query twice \(count and actual result\). Best if we simply add an endpoint for this

**Source-preserving request, proposal, or question:**

> Pagination will actually run the query twice \(count and actual result\). Best if we simply add an endpoint for this

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:559 · comment 549741886 · PR 10121 · 2024-10-07

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculatorHelperHk.scala`

**Evidence:** anon-2.jsonl:559 · comment 549741886 · PR 10121 · 2024-10-07

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/distro/DistributionCalculatorHelperHk.scala`

**Explicit source context (pr_title):**

> TT-5089 remove cache customer status for HK trailer rebate

## A2-0594 — MstarDailyPerformance: The `<currency>` should always be there, cuz it’s data. If that is missing, then sth is wrong w MStar

**Source stance:** explanation

**Context:**

> PR 10085 ([INV-3509] feat(composition)(marketdata): Handle missing data from MStar. Retry if unexpected exception), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mstar/xmls/MstarDailyPerformance.scala; original row 594.

**Concern stated in the source:** The `<currency>` should always be there, cuz it’s data. If that is missing, then sth is wrong w MStar

The attribute `@_CurrencyId` is only available if query with ISIN \(due to possibility of multiple share classes\). If query with MStarId, it won’t be there :thumbsup:

**Source-preserving request, proposal, or question:**

> The `<currency>` should always be there, cuz it’s data. If that is missing, then sth is wrong w MStar
> 
> The attribute `@_CurrencyId` is only available if query with ISIN \(due to possibility of multiple share classes\). If query with MStarId, it won’t be there :thumbsup:

**Conditions and limits:**

- <currency> is expected in data; @_CurrencyId exists only for ISIN lookup because share classes may differ, and is absent for MStarId lookup.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:594 · comment 546818241 · PR 10085 · 2024-09-30

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mstar/xmls/MstarDailyPerformance.scala`

**Evidence:** anon-2.jsonl:594 · comment 546818241 · PR 10085 · 2024-09-30

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mstar/xmls/MstarDailyPerformance.scala`

**Explicit source context (pr_title):**

> [INV-3509] feat(composition)(marketdata): Handle missing data from MStar. Retry if unexpected exception

## A2-0609 — InstrumentMStarDataJdbcDbHandler: In this pattern, the dbHandler should be the one incrementing the version, and outer logic can consider only actual data change

**Source stance:** suggestion

**Context:**

> PR 9911 (Feat/INV-3336 marketdata cleanup phase 3), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarDataJdbcDbHandler.scala; original row 609.

**Concern stated in the source:** In this pattern, the dbHandler should be the one incrementing the version, and outer logic can consider only actual data change

‌

**Source-preserving request, proposal, or question:**

> In this pattern, the dbHandler should be the one incrementing the version, and outer logic can consider only actual data change
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:609 · comment 538051839 · PR 9911 · 2024-09-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarDataJdbcDbHandler.scala`

**Evidence:** anon-2.jsonl:609 · comment 538051839 · PR 9911 · 2024-09-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarDataJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3336 marketdata cleanup phase 3

## A2-0610 — ServiceLogicImpl: I mean move this outside too. No need to bulkUpsert this for every ccy cuz this table doesn’t care about marketCcy

**Source stance:** suggestion

**Context:**

> PR 9911 (Feat/INV-3336 marketdata cleanup phase 3), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; original row 610.

**Concern stated in the source:** I mean move this outside too. No need to bulkUpsert this for every ccy cuz this table doesn’t care about marketCcy

Same for below method and the subscriber

**Source-preserving request, proposal, or question:**

> I mean move this outside too. No need to bulkUpsert this for every ccy cuz this table doesn’t care about marketCcy
> 
> Same for below method and the subscriber

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:610 · comment 538049671 · PR 9911 · 2024-09-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:610 · comment 538049671 · PR 9911 · 2024-09-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> Feat/INV-3336 marketdata cleanup phase 3

## A2-0611 — InstrumentMStarDataJdbcDbHandler: This should be `expectedPreviousUpdatedTimestamp`

**Source stance:** suggestion

**Context:**

> PR 9911 (Feat/INV-3336 marketdata cleanup phase 3), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarDataJdbcDbHandler.scala; original row 611.

**Concern stated in the source:** This should be `expectedPreviousUpdatedTimestamp`

**Source-preserving request, proposal, or question:**

> This should be `expectedPreviousUpdatedTimestamp`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:611 · comment 538048704 · PR 9911 · 2024-09-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarDataJdbcDbHandler.scala`

**Evidence:** anon-2.jsonl:611 · comment 538048704 · PR 9911 · 2024-09-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarDataJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3336 marketdata cleanup phase 3

## A2-0663 — ProductPortfolioRepository: Nit: can move a little closer to this method so that they stay in pair \(similar to those with stockRatio\)

**Source stance:** suggestion

**Context:**

> PR 9715 ([INV-3238] feat(advisory): create apis for goal modify flow), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala; original row 663.

**Concern stated in the source:** Nit: can move a little closer to this method so that they stay in pair \(similar to those with stockRatio\)

Also I think can overload with same name `findProductPortfolio`

```
def findProductPortfolio(
    advisoryTag: AdvisoryTag,
    riskTarget: ModelPortfolioRiskTarget,
    tradingAccountType: TradingAccountType
  ): Future[ProductPortfolio]
```

‌

**Source-preserving request, proposal, or question:**

> Nit: can move a little closer to this method so that they stay in pair \(similar to those with stockRatio\)
> 
> Also I think can overload with same name `findProductPortfolio`
> 
> ```
> def findProductPortfolio(
>     advisoryTag: AdvisoryTag,
>     riskTarget: ModelPortfolioRiskTarget,
>     tradingAccountType: TradingAccountType
>   ): Future[ProductPortfolio]
> ```
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:663 · comment 532701036 · PR 9715 · 2024-08-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Evidence:** anon-2.jsonl:663 · comment 532701036 · PR 9715 · 2024-08-20

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Explicit source context (pr_title):**

> [INV-3238] feat(advisory): create apis for goal modify flow

## A2-0696 — Review: Since we do not support topping up unit dividend on top of existing \(cash or unit\) dividend at all, let’s also check the trigger endpoint of unit dividend, and add que...

**Source stance:** suggestion

**Context:**

> PR 9784 (Resolve INV-3403: Add checks in handlers and populate necessary data in commands for duplicate distributions.), no inline path; original row 696.

**Concern stated in the source:** Since we do not support topping up unit dividend on top of existing \(cash or unit\) dividend at all, let’s also check the trigger endpoint of unit dividend, and add query readside of DividendEntity there and reject such request if any entries already exist

**Source-preserving request, proposal, or question:**

> Since we do not support topping up unit dividend on top of existing \(cash or unit\) dividend at all, let’s also check the trigger endpoint of unit dividend, and add query readside of DividendEntity there and reject such request if any entries already exist

**Conditions and limits:**

- Unit dividends cannot top up existing cash or unit dividends; trigger endpoint should reject any readside entry.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:696 · comment 532121285 · PR 9784 · 2024-08-19

**Evidence:** anon-2.jsonl:696 · comment 532121285 · PR 9784 · 2024-08-19

**Explicit source context (pr_title):**

> Resolve INV-3403: Add checks in handlers and populate necessary data in commands for duplicate distributions.

## A2-0697 — InstrumentPortfolioSubscribersDataRepository: Let’s do Source because this List will grow for popular instrument

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala; original row 697.

**Concern stated in the source:** Let’s do Source because this List will grow for popular instrument

**Source-preserving request, proposal, or question:**

> Let’s do Source because this List will grow for popular instrument

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:697 · comment 524603079 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Evidence:** anon-2.jsonl:697 · comment 524603079 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0700 — PortfolioMonthlyChangesHelper: Let’s move to pg for this readside, using IN across partition in cassandra is dangerous

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala; original row 700.

**Concern stated in the source:** Let’s move to pg for this readside, using IN across partition in cassandra is dangerous

**Source-preserving request, proposal, or question:**

> Let’s move to pg for this readside, using IN across partition in cassandra is dangerous

**Conditions and limits:**

- The proposed Postgres readside move is specifically motivated by Cassandra IN across partitions.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:700 · comment 524612654 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Evidence:** anon-2.jsonl:700 · comment 524612654 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0709 — InstrumentPortfolioSubscribersDataTable: Instant requested; exact field unavailable

**Source stance:** requested-change

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataTable.scala; original row 709.

**Source-preserving request, proposal, or question:**

> Instant

**Conditions and limits:**

- The literal requested type is Instant in InstrumentPortfolioSubscribersDataTable. With no hunk, the exact timestamp column or old type remains unresolved.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:709 · comment 524602479 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataTable.scala`

**Evidence:** anon-2.jsonl:709 · comment 524602479 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataTable.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0711 — PortfolioMarketDataEventProcessor: Let’s move this to PortfolioTopicSubscriber. Eventually we should also handle `ModelPortfolioDeactivatedMsg` and delete from repo

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/portfolio/processors/PortfolioMarketDataEventProcessor.scala; original row 711.

**Concern stated in the source:** Let’s move this to PortfolioTopicSubscriber. Eventually we should also handle `ModelPortfolioDeactivatedMsg` and delete from repo

**Source-preserving request, proposal, or question:**

> Let’s move this to PortfolioTopicSubscriber. Eventually we should also handle `ModelPortfolioDeactivatedMsg` and delete from repo

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:711 · comment 524607269 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/portfolio/processors/PortfolioMarketDataEventProcessor.scala`

**Evidence:** anon-2.jsonl:711 · comment 524607269 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/portfolio/processors/PortfolioMarketDataEventProcessor.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0716 — PortfolioMonthlyChangesDataTable: Instant

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesDataTable.scala; original row 716.

**Source-preserving request, proposal, or question:**

> Instant

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Instant requested in PortfolioMonthlyChangesDataTable updatedAt.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:716 · comment 524603775 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesDataTable.scala`

**Evidence:** anon-2.jsonl:716 · comment 524603775 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesDataTable.scala`

**Explicit source context (hunk):**

> +  def updatedAt = column[Instant]("updated_at")
> +
> +  def pk = primaryKey(PKName, (portfolioId, effectiveDate, marketdataCcy))
> +
> +  override def * : ProvenShape[PortfolioMonthlyChanges] = (
> +    portfolioId,
> +    effectiveDate,

**Evidence:** anon-2.jsonl:716 · comment 524603775 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesDataTable.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0718 — PortfolioMonthlyChangesHelper: I think there are 2 types of race conditions we might see here:

**Source stance:** observed-defect

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala; original row 718.

**Concern stated in the source:** I think there are 2 types of race conditions we might see here:

1. We get event that instrument mc is updated, and we trigger this method which will query instrument mc from readside - that might not have latest data yet… cuz they are 2 independent projections

    * We override the data for the instrument being updated, but it’s not bullet proof, e.g. db projection is super lagged for some reason
    
        * event of instrumentA, its data A2 is overridden on top of existing readside A1 & B1
        * then event of instrumentB, its data B2 is overridden on top of stale A1 & B1
        
    
2. Multiple instruments might be updated at once, each of them triggering this method… their upsert might override each other

    * This was protected with Portfolio entity last time. So we might need some impl of optimistic locking here
    

‌

**Source-preserving request, proposal, or question:**

> I think there are 2 types of race conditions we might see here:
> 
> 1. We get event that instrument mc is updated, and we trigger this method which will query instrument mc from readside - that might not have latest data yet… cuz they are 2 independent projections
> 
>     * We override the data for the instrument being updated, but it’s not bullet proof, e.g. db projection is super lagged for some reason
>     
>         * event of instrumentA, its data A2 is overridden on top of existing readside A1 & B1
>         * then event of instrumentB, its data B2 is overridden on top of stale A1 & B1
>         
>     
> 2. Multiple instruments might be updated at once, each of them triggering this method… their upsert might override each other
> 
>     * This was protected with Portfolio entity last time. So we might need some impl of optimistic locking here
>     
> 
> ‌

**Conditions and limits:**

- Two separate races remain: independent projection lag can pair new B2 with stale A1 despite per-event override, and concurrent instrument-triggered portfolio upserts can overwrite each other. Optimistic locking is proposed as entity replacement protection.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:718 · comment 524670185 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Evidence:** anon-2.jsonl:718 · comment 524670185 · PR 9603 · 2024-07-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/helpers/PortfolioMonthlyChangesHelper.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0720 — InstrumentMonthlyChangesJdbcRepository: Maybe Set for instruments

**Source stance:** open-question

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala; original row 720.

**Source-preserving request, proposal, or question:**

> Maybe Set for instruments

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:720 · comment 531323170 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Evidence:** anon-2.jsonl:720 · comment 531323170 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0721 — package: Let’s add updatedAt instant here, and use for both model and db. No need to split cuz we have single source that is the db

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/common/package.scala; original row 721.

**Concern stated in the source:** Let’s add updatedAt instant here, and use for both model and db. No need to split cuz we have single source that is the db

**Source-preserving request, proposal, or question:**

> Let’s add updatedAt instant here, and use for both model and db. No need to split cuz we have single source that is the db

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:721 · comment 531321610 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/common/package.scala`

**Evidence:** anon-2.jsonl:721 · comment 531321610 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/common/package.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0724 — PortfolioMonthlyChangesJdbcHandler: This should be set by caller

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesJdbcHandler.scala; original row 724.

**Source-preserving request, proposal, or question:**

> This should be set by caller

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Caller-owned timestamp/value is requested, but the displayed excerpt does not pinpoint the intended field; do not invent it.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:724 · comment 531322416 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesJdbcHandler.scala`

**Evidence:** anon-2.jsonl:724 · comment 531322416 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesJdbcHandler.scala`

**Explicit source context (hunk):**

> +    )
> +  }
> +
> +  def createTableIfNotExists: Future[Unit] = {
> +    database.run(
> +      sqlStatements(
> +        adjustCompositePkIfNotExists(

**Evidence:** anon-2.jsonl:724 · comment 531322416 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesJdbcHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0729 — PortfolioMonthlyChangesJdbcRepository: just `find`

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesJdbcRepository.scala; original row 729.

**Source-preserving request, proposal, or question:**

> just `find`

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:729 · comment 531326226 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesJdbcRepository.scala`

**Evidence:** anon-2.jsonl:729 · comment 531326226 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesJdbcRepository.scala`

**Explicit source context (hunk):**

> +
> +  def find(portfolioId: UUID, effectiveDate: LocalDate, marketDataCcy: CurrencyUnit): Future[Option[PortfolioMonthlyChanges]] = {
> +    database.run(
> +      portfolioMarketDataChangesDataTable
> +        .filter(_.portfolioId === portfolioId)
> +        .filter(_.effectiveDate === effectiveDate)
> +        .filter(_.marketdataCcy === marketDataCcy)

**Evidence:** anon-2.jsonl:729 · comment 531326226 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/PortfolioMonthlyChangesJdbcRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0730 — InstrumentMonthlyChangesJdbcRepository: Move filter up, and select specific columns

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala; original row 730.

**Concern stated in the source:** Move filter up, and select specific columns

**Source-preserving request, proposal, or question:**

> Move filter up, and select specific columns

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:730 · comment 531324498 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Evidence:** anon-2.jsonl:730 · comment 531324498 · PR 9603 · 2024-08-15

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0737 — InstrumentPricesJdbcHandler: Just instrumentId and priceCcy right? Also let’s assert `data` has same instrumentId and priceCcy

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPricesJdbcHandler.scala; original row 737.

**Concern stated in the source:** Just instrumentId and priceCcy right? Also let’s assert `data` has same instrumentId and priceCcy

**Source-preserving request, proposal, or question:**

> Just instrumentId and priceCcy right? Also let’s assert `data` has same instrumentId and priceCcy

**Conditions and limits:**

- Assert data instrumentId and priceCcy match those passed to the operation.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:737 · comment 531598146 · PR 9603 · 2024-08-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPricesJdbcHandler.scala`

**Evidence:** anon-2.jsonl:737 · comment 531598146 · PR 9603 · 2024-08-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPricesJdbcHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0741 — InstrumentMonthlyChangesJdbcRepository: map first, then just need `.distinct`

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala; original row 741.

**Concern stated in the source:** map first, then just need `.distinct`

**Source-preserving request, proposal, or question:**

> map first, then just need `.distinct`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:741 · comment 531597392 · PR 9603 · 2024-08-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Evidence:** anon-2.jsonl:741 · comment 531597392 · PR 9603 · 2024-08-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0742 — InstrumentMonthlyChangesJdbcRepository: Maybe rename:

**Source stance:** suggestion

**Context:**

> PR 9603 (Feat/INV-3271 marketdata portfolio entity phase 1), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala; original row 742.

**Source-preserving request, proposal, or question:**

> Maybe rename:
> 
> * `UpdatedInstrumentMonthlyChangesPortfolio` as `PortfolioIdWithCcy`
> * `streamUpdatedInstrumentMonthlyChangesFrom` as `streamPortfoliosHavingUpdatedInstrumentMonthlyChanges`
> * `instrumentMonthlyChangesUpdatedAt` as `instrumentMonthlyChangesUpdatedFrom`
> 
> ‌

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:742 · comment 531597177 · PR 9603 · 2024-08-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Evidence:** anon-2.jsonl:742 · comment 531597177 · PR 9603 · 2024-08-16

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3271 marketdata portfolio entity phase 1

## A2-0788 — InstrumentPortfolioSubscribersDataRepository: Let’s not put repository yet in this PR. Do join between this and mc table so we can dedupe in DB

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala; original row 788.

**Concern stated in the source:** Let’s not put repository yet in this PR. Do join between this and mc table so we can dedupe in DB

**Source-preserving request, proposal, or question:**

> Let’s not put repository yet in this PR. Do join between this and mc table so we can dedupe in DB

**Conditions and limits:**

- Join in DB should deduplicate instrument/MC records before repository surface is added.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:788 · comment 526840443 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Evidence:** anon-2.jsonl:788 · comment 526840443 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0789 — InstrumentPriceTable: `(instrumentId, priceCcy, priceDate)`

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPriceTable.scala; original row 789.

**Source-preserving request, proposal, or question:**

> `(instrumentId, priceCcy, priceDate)`

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Hunk supplies the exact InstrumentPriceTable primary key (instrumentId, priceCcy, priceDate).
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:789 · comment 526841260 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPriceTable.scala`

**Evidence:** anon-2.jsonl:789 · comment 526841260 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPriceTable.scala`

**Explicit source context (hunk):**

> +
> +
> +  def pk = primaryKey(PKName, (instrumentId, priceCcy, priceDate))
> +
> +  override def * : ProvenShape[InstrumentDailyPriceVo] = (
> +    instrumentId,
> +    priceDate,

**Evidence:** anon-2.jsonl:789 · comment 526841260 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPriceTable.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0792 — InstrumentPortfolioSubscribersDataJdbcHandler: Take VO instead of individual fields. Set updatedAt outside

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala; original row 792.

**Concern stated in the source:** Take VO instead of individual fields. Set updatedAt outside

**Source-preserving request, proposal, or question:**

> Take VO instead of individual fields. Set updatedAt outside

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:792 · comment 526840233 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala`

**Evidence:** anon-2.jsonl:792 · comment 526840233 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataJdbcHandler.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0793 — InstrumentMarketDataJdbcProjection: Consider skipping old events, and sync to db separately to save cost processing old events we don’t care

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataJdbcProjection.scala; original row 793.

**Concern stated in the source:** Consider skipping old events, and sync to db separately to save cost processing old events we don’t care

**Source-preserving request, proposal, or question:**

> Consider skipping old events, and sync to db separately to save cost processing old events we don’t care

**Conditions and limits:**

- Skipping costly historical events and syncing DB separately is a proposal, not a verified safe migration sequence.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:793 · comment 526841921 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataJdbcProjection.scala`

**Evidence:** anon-2.jsonl:793 · comment 526841921 · PR 9689 · 2024-08-01

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/processors/InstrumentMarketDataJdbcProjection.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0796 — InstrumentPortfolioSubscribersDataRepository: Just `streamInstrumentPortfolioSubscribers` ?

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala; original row 796.

**Source-preserving request, proposal, or question:**

> Just `streamInstrumentPortfolioSubscribers` ?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:796 · comment 528897605 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Evidence:** anon-2.jsonl:796 · comment 528897605 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Explicit source context (hunk):**

> +  private val instrumentPortfolioSubscribersDataTable = TableQuery[InstrumentPortfolioSubscribersDataTable]
> +
> +  def streamInstrumentPortfolioSubscribers(instrumentId: String): Source[InstrumentPortfolioSubscribersDataVo, NotUsed] = {
> +    Slick.source(
> +      instrumentPortfolioSubscribersDataTable
> +        .filter(_.instrumentId === instrumentId)
> +        .result

**Evidence:** anon-2.jsonl:796 · comment 528897605 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentPortfolioSubscribersDataRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0799 — InstrumentMonthlyChangesJdbcRepository: We don’t need the monthly changes in the result of this query? Otherwise this query is still n\*m.

**Source stance:** suggestion

**Context:**

> PR 9689 (Feat/INV-3361 instrument price monthly changes jdbc migration), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala; original row 799.

**Concern stated in the source:** We don’t need the monthly changes in the result of this query? Otherwise this query is still n\*m.

Maybe just remove all these unused repository methods, and add them in your other PR that you actually use them

**Source-preserving request, proposal, or question:**

> We don’t need the monthly changes in the result of this query? Otherwise this query is still n\*m.
> 
> Maybe just remove all these unused repository methods, and add them in your other PR that you actually use them

**Conditions and limits:**

- Returning unnecessary monthly changes still creates n*m output; unused repository methods should wait for the consuming PR.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:799 · comment 528898306 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Evidence:** anon-2.jsonl:799 · comment 528898306 · PR 9689 · 2024-08-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangesJdbcRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-3361 instrument price monthly changes jdbc migration

## A2-0821 — ProductPortfolioRepository: Maybe we can keep this method generic, but only handle for CoreEnhanced for now…

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala; original row 821.

**Concern stated in the source:** Maybe we can keep this method generic, but only handle for CoreEnhanced for now…

```
def findProductPortfolio(
  advisoryTag: AdvisoryTag,
  riskTarget: ModelPortfolioRiskTarget,
  tradingAccountType: TradingAccountType
): Future[ProductPortfolio] = {
  findAllActiveForAdvisoryTag(advisoryTag)
    .filter(p => filterForTradingAccountType(advisoryTag, tradingAccountType, p))
    .filter(p => filterForRiskTarget(advisoryTag, riskTarget, p))
    .runWith(Sink.headOption)
    .flatMap({
      case Some(productPortfolio) => Future.successful(productPortfolio)
      case None =>
        Future
          .failed(BadRequest(s"Unable to find $advisoryTag portfolio for trading account $tradingAccountType with risk target of $riskTarget"))
    })
}

private def filterForRiskTarget(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget, p: ProductPortfolio): Boolean = {
  advisoryTag match {
    case AdvisoryTag.CORE_ENHANCED =>
      ProductPortfolio.extractCoreEnhancedMetaData(p).exists(_.riskTarget == riskTarget)
    case _ => false
  }
}
```

‌

I want to keep the method signature as close to the lookup by targetStockRatio one so it’s easier to switch later for Flagship/Esg/Factors/FlagshipDpm

**Source-preserving request, proposal, or question:**

> Maybe we can keep this method generic, but only handle for CoreEnhanced for now…
> 
> ```
> def findProductPortfolio(
>   advisoryTag: AdvisoryTag,
>   riskTarget: ModelPortfolioRiskTarget,
>   tradingAccountType: TradingAccountType
> ): Future[ProductPortfolio] = {
>   findAllActiveForAdvisoryTag(advisoryTag)
>     .filter(p => filterForTradingAccountType(advisoryTag, tradingAccountType, p))
>     .filter(p => filterForRiskTarget(advisoryTag, riskTarget, p))
>     .runWith(Sink.headOption)
>     .flatMap({
>       case Some(productPortfolio) => Future.successful(productPortfolio)
>       case None =>
>         Future
>           .failed(BadRequest(s"Unable to find $advisoryTag portfolio for trading account $tradingAccountType with risk target of $riskTarget"))
>     })
> }
> 
> private def filterForRiskTarget(advisoryTag: AdvisoryTag, riskTarget: ModelPortfolioRiskTarget, p: ProductPortfolio): Boolean = {
>   advisoryTag match {
>     case AdvisoryTag.CORE_ENHANCED =>
>       ProductPortfolio.extractCoreEnhancedMetaData(p).exists(_.riskTarget == riskTarget)
>     case _ => false
>   }
> }
> ```
> 
> ‌
> 
> I want to keep the method signature as close to the lookup by targetStockRatio one so it’s easier to switch later for Flagship/Esg/Factors/FlagshipDpm

**Conditions and limits:**

- Initial proposed generic signature handles only CoreEnhanced and otherwise returns false; row 837 proposes completing other productlines via ProductPortfolio.riskTarget.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:821 · comment 523845974 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Evidence:** anon-2.jsonl:821 · comment 523845974 · PR 9605 · 2024-07-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0837 — ProductPortfolioRepository: On 2nd thought, I suppose for other productlines, we can simply check against `ProductPortfolio.riskTarget`. Then this impl will be complete

**Source stance:** suggestion

**Context:**

> PR 9605 ([INV-3236] feat(advisory): create advisory endpoints for goal create), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala; original row 837.

**Concern stated in the source:** On 2nd thought, I suppose for other productlines, we can simply check against `ProductPortfolio.riskTarget`. Then this impl will be complete

**Source-preserving request, proposal, or question:**

> On 2nd thought, I suppose for other productlines, we can simply check against `ProductPortfolio.riskTarget`. Then this impl will be complete

**Conditions and limits:**

- This is a second-thought extension to row 821, not proof all productlines were already handled.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:837 · comment 524565992 · PR 9605 · 2024-07-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Evidence:** anon-2.jsonl:837 · comment 524565992 · PR 9605 · 2024-07-24

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

**Explicit source context (pr_title):**

> [INV-3236] feat(advisory): create advisory endpoints for goal create

## A2-0924 — FeeManager: As discussed, let’s try to refactor and move this decision to outer level \(similar to fee estimation query\), cuz we already have all the planProfiles and customerI...

**Source stance:** suggestion

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala; original row 924.

**Concern stated in the source:** As discussed, let’s try to refactor and move this decision to outer level \(similar to fee estimation query\), cuz we already have all the planProfiles and customerId there

**Source-preserving request, proposal, or question:**

> As discussed, let’s try to refactor and move this decision to outer level \(similar to fee estimation query\), cuz we already have all the planProfiles and customerId there

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:924 · comment 520050194 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala`

**Evidence:** anon-2.jsonl:924 · comment 520050194 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/FeeManager.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0925 — CustomerFeeQueryService: This query service is used for both the notification and admin. Maybe we want to add flag such that admin can estimate the fee but notification won’t send?

**Source stance:** open-question

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerFeeQueryService.scala; original row 925.

**Concern stated in the source:** This query service is used for both the notification and admin. Maybe we want to add flag such that admin can estimate the fee but notification won’t send?

**Source-preserving request, proposal, or question:**

> This query service is used for both the notification and admin. Maybe we want to add flag such that admin can estimate the fee but notification won’t send?

**Conditions and limits:**

- Admin fee estimation and customer notification have different needs; optional flag is proposed.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:925 · comment 520050569 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerFeeQueryService.scala`

**Evidence:** anon-2.jsonl:925 · comment 520050569 · PR 9546 · 2024-07-11

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/utils/CustomerFeeQueryService.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0942 — FeeChargeRequestJdbcRepository: Looks like we also need to upversion this table to add new column for skip details? I suppose for immediate data query needs, we can safely rely ...

**Source stance:** suggestion

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcRepository.scala; original row 942.

**Concern stated in the source:** Looks like we also need to upversion this table to add new column for skip details? I suppose for immediate data query needs, we can safely rely on the status column. But let’s have a followup task when time allows.

**Source-preserving request, proposal, or question:**

> Looks like we also need to upversion this table to add new column for skip details? I suppose for immediate data query needs, we can safely rely on the status column. But let’s have a followup task when time allows.

**Conditions and limits:**

- Immediate queries may use status column; a later table version should add skip details.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:942 · comment 520381714 · PR 9546 · 2024-07-12

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcRepository.scala`

**Evidence:** anon-2.jsonl:942 · comment 520381714 · PR 9546 · 2024-07-12

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcRepository.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0944 — FeeChargeRequestJdbcRepository: We also need to handle the skipped event in `FeeChargeRequestJdbcProjectionV6`

**Source stance:** explanation

**Context:**

> PR 9546 ([EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles), charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcRepository.scala; original row 944.

**Concern stated in the source:** We also need to handle the skipped event in `FeeChargeRequestJdbcProjectionV6`

**Source-preserving request, proposal, or question:**

> We also need to handle the skipped event in `FeeChargeRequestJdbcProjectionV6`

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:944 · comment 520392380 · PR 9546 · 2024-07-12

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcRepository.scala`

**Evidence:** anon-2.jsonl:944 · comment 520392380 · PR 9546 · 2024-07-12

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcRepository.scala`

**Explicit source context (pr_title):**

> [EN-3615][EN-3616] feat(charge, redemption) skip comms & fee charge to RF plans for certain corporate profiles

## A2-0970 — NonAltsFeeManager: There’s a small performance boost here cuz [person] queries tradable-goals by customerId first, and we only care about checking TAA if a plan does not exist i...

**Source stance:** suggestion

**Context:**

> PR 9467 (Resolve INV-3214: Changes to charge cash only fee for fixed maturity product plans.), charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/NonAltsFeeManager.scala; original row 970.

**Concern stated in the source:** There’s a small performance boost here cuz [person] queries tradable-goals by customerId first, and we only care about checking TAA if a plan does not exist in the list. `chargePlanIfEligible` OTOH is already at plan level.

I suppose we can refactor a bit more to reuse this code.

* this customer method checks using `getTradableCustomerGoals`
* then pass whether `isCashOnlyFee` may require overridden or not into `chargePlanIfEligible`
* and `chargePlanIfEligible` will fetch TAA if needed

‌

**Source-preserving request, proposal, or question:**

> There’s a small performance boost here cuz [person] queries tradable-goals by customerId first, and we only care about checking TAA if a plan does not exist in the list. `chargePlanIfEligible` OTOH is already at plan level.
> 
> I suppose we can refactor a bit more to reuse this code.
> 
> * this customer method checks using `getTradableCustomerGoals`
> * then pass whether `isCashOnlyFee` may require overridden or not into `chargePlanIfEligible`
> * and `chargePlanIfEligible` will fetch TAA if needed
> 
> ‌

**Conditions and limits:**

- Customer-level path first checks getTradableCustomerGoals; plan-level path fetches TAA only as needed to override isCashOnlyFee.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:970 · comment 516099105 · PR 9467 · 2024-07-01

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/NonAltsFeeManager.scala`

> There’s a small performance boost here cuz

**Evidence:** anon-2.jsonl:970 · comment 516099105 · PR 9467 · 2024-07-01

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/NonAltsFeeManager.scala`

> queries tradable-goals by customerId first, and we only care about checking TAA if a plan does not exist in the list. `chargePlanIfEligible` OTOH is already at plan level.
> 
> I suppose we can refactor a bit more to reuse this code.
> 
> * this customer method checks using `getTradableCustomerGoals`
> * then pass whether `isCashOnlyFee` may require overridden or not into `chargePlanIfEligible`
> * and `chargePlanIfEligible` will fetch TAA if needed
> 
> ‌

**Evidence:** anon-2.jsonl:970 · comment 516099105 · PR 9467 · 2024-07-01

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/NonAltsFeeManager.scala`

**Explicit source context (pr_title):**

> Resolve INV-3214: Changes to charge cash only fee for fixed maturity product plans.

## A2-0978 — ServiceLogicImpl: This logic actually works for 1st time trigger too. Maybe we just rename, accept `requestedBy` and `reason` as query params, so we can use in both places?

**Source stance:** suggestion

**Context:**

> PR 9470 ([INV-3038] feat(rebalance): Trigger missed dpc), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; original row 978.

**Concern stated in the source:** This logic actually works for 1st time trigger too. Maybe we just rename, accept `requestedBy` and `reason` as query params, so we can use in both places?

**Source-preserving request, proposal, or question:**

> This logic actually works for 1st time trigger too. Maybe we just rename, accept `requestedBy` and `reason` as query params, so we can use in both places?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:978 · comment 516555452 · PR 9470 · 2024-07-02

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:978 · comment 516555452 · PR 9470 · 2024-07-02

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-3038] feat(rebalance): Trigger missed dpc

## A2-1021 — BaseGoalService: Can we remove this param `status`…. currently logic only supports query live or all status… and why would a goal be tradable if it’s not live…

**Source stance:** suggestion

**Context:**

> PR 9433 (Resolve INV-3212: Changes to handle special handling instruments with modification/redemption blocks.), goal-api/src/main/scala/com/endowus/silver/goal/api/BaseGoalService.scala; original row 1021.

**Concern stated in the source:** Can we remove this param `status`…. currently logic only supports query live or all status… and why would a goal be tradable if it’s not live…

**Source-preserving request, proposal, or question:**

> Can we remove this param `status`…. currently logic only supports query live or all status… and why would a goal be tradable if it’s not live…

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1021 · comment 513992990 · PR 9433 · 2024-06-27

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/BaseGoalService.scala`

**Evidence:** anon-2.jsonl:1021 · comment 513992990 · PR 9433 · 2024-06-27

Source path: `goal-api/src/main/scala/com/endowus/silver/goal/api/BaseGoalService.scala`

**Explicit source context (pr_title):**

> Resolve INV-3212: Changes to handle special handling instruments with modification/redemption blocks.

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

## A2-1061 — GoalBasedStatementInfoDbDto: Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.

**Source stance:** explanation

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala; original row 1061.

**Concern stated in the source:** Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.

Based on my understanding, it seems these new fields are not needed anyway. The new design will anyway cause it to be reprinted cuz we have the new page split for AllInvestmentGoals pages \+ the ordering for other goal pages. Other than that, once new design is printed, these isDpm flags are no longer useful, cuz goal cannot change its dpm flag.

**Source-preserving request, proposal, or question:**

> Yea so I think adding these new fields to `*DbDto` can cause confusion for existing data if we don’t retrospectively update them.
> 
> Based on my understanding, it seems these new fields are not needed anyway. The new design will anyway cause it to be reprinted cuz we have the new page split for AllInvestmentGoals pages \+ the ordering for other goal pages. Other than that, once new design is printed, these isDpm flags are no longer useful, cuz goal cannot change its dpm flag.

**Conditions and limits:**

- New format already forces reprinting through page splitting/order changes; mutable persisted isDpm fields are considered unnecessary and confusing without retrospective data updates.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1061 · comment 502499163 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Evidence:** anon-2.jsonl:1061 · comment 502499163 · PR 9052 · 2024-05-21

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1066 — GoalBasedStatementInfoDbDto: Let’s add these fields into the list of data-loss fields in the comment in `GoalBasedStatementPageDataDbDto`, together with explanation, e.g. isDpm ...

**Source stance:** suggestion

**Context:**

> PR 9052 ([INV-3010] : update monthly statement to include dpm section), report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala; original row 1066.

**Concern stated in the source:** Let’s add these fields into the list of data-loss fields in the comment in `GoalBasedStatementPageDataDbDto`, together with explanation, e.g. isDpm flag is immutable for a goal \+ dpm/non-dpm total are just convenient summary data for display

**Source-preserving request, proposal, or question:**

> Let’s add these fields into the list of data-loss fields in the comment in `GoalBasedStatementPageDataDbDto`, together with explanation, e.g. isDpm flag is immutable for a goal \+ dpm/non-dpm total are just convenient summary data for display

**Conditions and limits:**

- Document intentional data-loss fields: immutable per-goal isDpm and derived DPM/non-DPM display counts.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1066 · comment 503071608 · PR 9052 · 2024-05-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Evidence:** anon-2.jsonl:1066 · comment 503071608 · PR 9052 · 2024-05-22

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/goalBased/model/GoalBasedStatementInfoDbDto.scala`

**Explicit source context (pr_title):**

> [INV-3010] : update monthly statement to include dpm section

## A2-1097 — InstrumentJdbcEventProcessor: Let’s use Cassandra projection manager?

**Source stance:** open-question

**Context:**

> PR 9014 (Resolve INV-2980: BE changes needed for admin instrument screens), instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessor.scala; original row 1097.

**Source-preserving request, proposal, or question:**

> Let’s use Cassandra projection manager?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1097 · comment 499485542 · PR 9014 · 2024-05-09

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:1097 · comment 499485542 · PR 9014 · 2024-05-09

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessor.scala`

**Explicit source context (pr_title):**

> Resolve INV-2980: BE changes needed for admin instrument screens

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

## A2-1139 — package: Do we need this case class? Let’s just use query params?

**Source stance:** suggestion

**Context:**

> PR 9228 (Feat/INV-3064 instrument fund document), instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/package.scala; original row 1139.

**Source-preserving request, proposal, or question:**

> Do we need this case class? Let’s just use query params?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1139 · comment 504109557 · PR 9228 · 2024-05-27

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/package.scala`

**Evidence:** anon-2.jsonl:1139 · comment 504109557 · PR 9228 · 2024-05-27

Source path: `instrument-api/src/main/scala/com/endowus/silver/instrument/api/commons/package.scala`

**Explicit source context (pr_title):**

> Feat/INV-3064 instrument fund document

## A2-1168 — PortfolioVersionUpgradeRebalanceRequestsGenerator: Let’s log the `tradingRestrictions` here so we can query for more details if needed

**Source stance:** suggestion

**Context:**

> PR 9142 (Feat/INV-3035 trading restriction dpc), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala; original row 1168.

**Concern stated in the source:** Let’s log the `tradingRestrictions` here so we can query for more details if needed

**Source-preserving request, proposal, or question:**

> Let’s log the `tradingRestrictions` here so we can query for more details if needed

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1168 · comment 502180463 · PR 9142 · 2024-05-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala`

**Evidence:** anon-2.jsonl:1168 · comment 502180463 · PR 9142 · 2024-05-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/managers/PortfolioVersionUpgradeRebalanceRequestsGenerator.scala`

**Explicit source context (pr_title):**

> Feat/INV-3035 trading restriction dpc

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

## A2-1233 — Review: Oh I didnt realize we already released on `trading` svc side… I guess it’s not worth the effort to rename and bump new table version for everything :sweat_smile:

**Source stance:** suggestion

**Context:**

> PR 9074 (TT-4204 autofund details), no inline path; original row 1233.

**Concern stated in the source:** Oh I didnt realize we already released on `trading` svc side… I guess it’s not worth the effort to rename and bump new table version for everything :sweat_smile:

**Source-preserving request, proposal, or question:**

> Oh I didnt realize we already released on `trading` svc side… I guess it’s not worth the effort to rename and bump new table version for everything :sweat_smile:

**Conditions and limits:**

- Already-released trading schema makes a rename plus all table-version bumps disproportionate; this is a historical rollout compromise.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1233 · comment 498473299 · PR 9074 · 2024-05-06

**Evidence:** anon-2.jsonl:1233 · comment 498473299 · PR 9074 · 2024-05-06

**Explicit source context (pr_title):**

> TT-4204 autofund details

## A2-1235 — InvestmentRequestTopicSubscriberV3: There can be eventual consistency delay here no? So might end up with stale version of transaction in the repository

**Source stance:** open-question

**Context:**

> PR 8923 (TT-4220 pass deposit tx id to investment and transaction), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala; original row 1235.

**Concern stated in the source:** There can be eventual consistency delay here no? So might end up with stale version of transaction in the repository

**Source-preserving request, proposal, or question:**

> There can be eventual consistency delay here no? So might end up with stale version of transaction in the repository

**Conditions and limits:**

- Repository transaction lookup may be stale because of eventual consistency.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1235 · comment 498410518 · PR 8923 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Evidence:** anon-2.jsonl:1235 · comment 498410518 · PR 8923 · 2024-05-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/InvestmentRequestTopicSubscriberV3.scala`

**Explicit source context (pr_title):**

> TT-4220 pass deposit tx id to investment and transaction

## A2-1242 — InvestmentPlanTableV6: FYI, there’s a bug with V6. We will release V7 soon….

**Source stance:** explanation

**Context:**

> PR 8984 (TT-4211 investment auto fund model), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV6.scala; original row 1242.

**Concern stated in the source:** FYI, there’s a bug with V6. We will release V7 soon….

**Source-preserving request, proposal, or question:**

> FYI, there’s a bug with V6. We will release V7 soon….

**Conditions and limits:**

- V6 bug and upcoming V7 are mentioned without the bug details; source does not establish the replacement is released.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1242 · comment 498398999 · PR 8984 · 2024-05-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV6.scala`

**Evidence:** anon-2.jsonl:1242 · comment 498398999 · PR 8984 · 2024-05-06

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV6.scala`

**Explicit source context (pr_title):**

> TT-4211 investment auto fund model

## A2-1301 — InvestmentPlanTableV7: Maybe just `schedule.map(s => s.fundingInstructions.getOrElse(PlanAccountPlanFundingInstructions(s.investmentAmount)))`

**Source stance:** suggestion

**Context:**

> PR 9071 ([EN-3328] Fix funding instructions fallback in investment plan and bump to v7), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV7.scala; original row 1301.

**Concern stated in the source:** Maybe just `schedule.map(s => s.fundingInstructions.getOrElse(PlanAccountPlanFundingInstructions(s.investmentAmount)))`

No need to double wrap the Option

**Source-preserving request, proposal, or question:**

> Maybe just `schedule.map(s => s.fundingInstructions.getOrElse(PlanAccountPlanFundingInstructions(s.investmentAmount)))`
> 
> No need to double wrap the Option

**Conditions and limits:**

- Resolve schedule funding instructions without wrapping Option twice; use PlanAccountPlanFundingInstructions(s.investmentAmount) fallback inside schedule.map.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1301 · comment 498008564 · PR 9071 · 2024-05-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV7.scala`

**Evidence:** anon-2.jsonl:1301 · comment 498008564 · PR 9071 · 2024-05-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentPlanTableV7.scala`

**Explicit source context (pr_title):**

> [EN-3328] Fix funding instructions fallback in investment plan and bump to v7

## A2-1303 — HkAdvisedPortfolioMaaManager: Yea this is existing. portfolio-offerings will be used during add goal / modify goal flow, and we show in portfolio ccy there.

**Source stance:** explanation

**Context:**

> PR 9051 ([INV-2978] feat(advisory): Move MAA endpoints to base. Add MAA for FlagshipDpm in HK), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkAdvisedPortfolioMaaManager.scala; original row 1303.

**Concern stated in the source:** Yea this is existing. portfolio-offerings will be used during add goal / modify goal flow, and we show in portfolio ccy there.

Here we simply reuse the offerings lookup, but query performance in displayCcy for MAA.

**Source-preserving request, proposal, or question:**

> Yea this is existing. portfolio-offerings will be used during add goal / modify goal flow, and we show in portfolio ccy there.
> 
> Here we simply reuse the offerings lookup, but query performance in displayCcy for MAA.

**Conditions and limits:**

- Offerings remain portfolio currency in add/modify flow, while MAA reuses offerings lookup and requests performance in displayCcy.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1303 · comment 497686791 · PR 9051 · 2024-05-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkAdvisedPortfolioMaaManager.scala`

**Evidence:** anon-2.jsonl:1303 · comment 497686791 · PR 9051 · 2024-05-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/HkAdvisedPortfolioMaaManager.scala`

**Explicit source context (pr_title):**

> [INV-2978] feat(advisory): Move MAA endpoints to base. Add MAA for FlagshipDpm in HK

## A2-1309 — AuroraJdbcSchema: keep the `v6` so it’s not confusing when we add v7

**Source stance:** explanation

**Context:**

> PR 8963 ([EN-3107] feat(investment): Migrate investment plan jdbc to v6), investment-impl/src/main/scala/com/endowus/silver/investment/impl/db/AuroraJdbcSchema.scala; original row 1309.

**Source-preserving request, proposal, or question:**

> keep the `v6` so it’s not confusing when we add v7

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1309 · comment 494481439 · PR 8963 · 2024-04-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/db/AuroraJdbcSchema.scala`

**Evidence:** anon-2.jsonl:1309 · comment 494481439 · PR 8963 · 2024-04-22

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/db/AuroraJdbcSchema.scala`

**Explicit source context (pr_title):**

> [EN-3107] feat(investment): Migrate investment plan jdbc to v6

## A2-1353 — RebalanceRequestJdbcRepositoryImpl: Let’s just import `import com.endowus.silver.rebalance.impl.db.RebalancePostgresProfile.api._` ?

**Source stance:** suggestion

**Context:**

> PR 8969 (Resolve INV-2969: Add rebalance config readside.), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala; original row 1353.

**Source-preserving request, proposal, or question:**

> Let’s just import `import com.endowus.silver.rebalance.impl.db.RebalancePostgresProfile.api._` ?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1353 · comment 494562717 · PR 8969 · 2024-04-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala`

**Evidence:** anon-2.jsonl:1353 · comment 494562717 · PR 8969 · 2024-04-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala`

**Explicit source context (hunk):**

>  import com.endowus.silver.rebalance.api.enums.RebalanceRequestStatus
>  import com.endowus.silver.rebalance.api.enums.RebalanceRequestStatus.RebalanceRequestStatus
> -import com.endowus.silver.rebalance.impl.entities.rebalancer.db.jdbc.RebalancePostgresProfile.api._
> +import com.endowus.silver.rebalance.impl.db.RebalancePostgresProfile
> +import com.endowus.silver.rebalance.impl.db.RebalancePostgresProfile.api._
>  import com.typesafe.scalalogging.LazyLogging
>  import play.api.libs.json.JsValue

**Evidence:** anon-2.jsonl:1353 · comment 494562717 · PR 8969 · 2024-04-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala`

**Explicit source context (pr_title):**

> Resolve INV-2969: Add rebalance config readside.

## A2-1360 — MarketDataUploader: I suppose it’s also good to log for prices we have in our DB but not in MStar.

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1360.

**Concern stated in the source:** I suppose it’s also good to log for prices we have in our DB but not in MStar.

Speaking of this, the instrument source should probably filter for those we know prices are available in MStar. I think for now, we can start with `instrument.pricingDetails.pricingSource`

**Source-preserving request, proposal, or question:**

> I suppose it’s also good to log for prices we have in our DB but not in MStar.
> 
> Speaking of this, the instrument source should probably filter for those we know prices are available in MStar. I think for now, we can start with `instrument.pricingDetails.pricingSource`

**Conditions and limits:**

- Reconcile prices in DB but absent MStar too; source selection should require known MStar pricingSource.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1360 · comment 493343432 · PR 8931 · 2024-04-17

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1360 · comment 493343432 · PR 8931 · 2024-04-17

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1365 — MarketDataUploader: Don’t we need to include `startDate` in this method? Otherwise we will have lots of warn log complaining missing price in MStar, since we compare limited MSt...

**Source stance:** open-question

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1365.

**Concern stated in the source:** Don’t we need to include `startDate` in this method? Otherwise we will have lots of warn log complaining missing price in MStar, since we compare limited MStar data vs full DB data

**Source-preserving request, proposal, or question:**

> Don’t we need to include `startDate` in this method? Otherwise we will have lots of warn log complaining missing price in MStar, since we compare limited MStar data vs full DB data

**Conditions and limits:**

- Both MStar and DB sides must share startDate or limited MStar data versus full DB creates spurious missing-price warnings.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1365 · comment 494951071 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1365 · comment 494951071 · PR 8931 · 2024-04-23

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1375 — MarketDataUploader: I think this cassandra table already have priceDate in its clustering key. We should be able to add a method in repository to filter in database itself

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala; original row 1375.

**Concern stated in the source:** I think this cassandra table already have priceDate in its clustering key. We should be able to add a method in repository to filter in database itself

**Source-preserving request, proposal, or question:**

> I think this cassandra table already have priceDate in its clustering key. We should be able to add a method in repository to filter in database itself

**Conditions and limits:**

- priceDate clustering key allows database-side filtering; source says this is believed to exist, not independently verified.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1375 · comment 495203334 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Evidence:** anon-2.jsonl:1375 · comment 495203334 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/utils/MarketDataUploader.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1379 — InstrumentPriceRepository: Let’s just add an overloading of existing `retrievePrices` that takes required `startDate`. Then we can leave to caller to decide which one to call?

**Source stance:** suggestion

**Context:**

> PR 8931 ([INV-2849] create a reconcile job to check instrument prices), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPriceRepository.scala; original row 1379.

**Concern stated in the source:** Let’s just add an overloading of existing `retrievePrices` that takes required `startDate`. Then we can leave to caller to decide which one to call?

**Source-preserving request, proposal, or question:**

> Let’s just add an overloading of existing `retrievePrices` that takes required `startDate`. Then we can leave to caller to decide which one to call?

**Conditions and limits:**

- Overload retrievePrices with required startDate and let callers choose.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1379 · comment 495248952 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPriceRepository.scala`

**Evidence:** anon-2.jsonl:1379 · comment 495248952 · PR 8931 · 2024-04-24

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/prices/InstrumentPriceRepository.scala`

**Explicit source context (pr_title):**

> [INV-2849] create a reconcile job to check instrument prices

## A2-1409 — JdbcSchema: Maybe change this to follow the new pattern in which we have separate DbHandler class supporting createTable/upsert/delete and Repository class supporting queries

**Source stance:** suggestion

**Context:**

> PR 8792 (Feat/INV-2730/flagship dpm offerring min required amts), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/db/JdbcSchema.scala; original row 1409.

**Concern stated in the source:** Maybe change this to follow the new pattern in which we have separate DbHandler class supporting createTable/upsert/delete and Repository class supporting queries

**Source-preserving request, proposal, or question:**

> Maybe change this to follow the new pattern in which we have separate DbHandler class supporting createTable/upsert/delete and Repository class supporting queries

**Conditions and limits:**

- The proposed project pattern separates create/upsert/delete DbHandler from query Repository.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1409 · comment 488865874 · PR 8792 · 2024-04-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/db/JdbcSchema.scala`

**Evidence:** anon-2.jsonl:1409 · comment 488865874 · PR 8792 · 2024-04-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/db/JdbcSchema.scala`

**Explicit source context (pr_title):**

> Feat/INV-2730/flagship dpm offerring min required amts

## A2-1410 — JdbcSchema: Otherwise, if you don’t want to change too much in this PR, let’s just use `ProductPortfolioJdbcRepository#createTable` here?

**Source stance:** suggestion

**Context:**

> PR 8792 (Feat/INV-2730/flagship dpm offerring min required amts), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/db/JdbcSchema.scala; original row 1410.

**Concern stated in the source:** Otherwise, if you don’t want to change too much in this PR, let’s just use `ProductPortfolioJdbcRepository#createTable` here?

**Source-preserving request, proposal, or question:**

> Otherwise, if you don’t want to change too much in this PR, let’s just use `ProductPortfolioJdbcRepository#createTable` here?

**Conditions and limits:**

- Using existing ProductPortfolioJdbcRepository#createTable is an accepted smaller alternative to row 1409 refactor.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1410 · comment 488866178 · PR 8792 · 2024-04-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/db/JdbcSchema.scala`

**Evidence:** anon-2.jsonl:1410 · comment 488866178 · PR 8792 · 2024-04-04

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/db/JdbcSchema.scala`

**Explicit source context (pr_title):**

> Feat/INV-2730/flagship dpm offerring min required amts

## A2-1417 — PortfolioSuitabilityAnalysisResponse: Let’s just match by index or use id in a Map instead of new response type

**Source stance:** suggestion

**Context:**

> PR 8834 (Feat/INV-2861 dpm portfolio suitability), compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/portfolioSuitabilityAnalysis/PortfolioSuitabilityAnalysisResponse.scala; original row 1417.

**Source-preserving request, proposal, or question:**

> Let’s just match by index or use id in a Map instead of new response type

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1417 · comment 488849464 · PR 8834 · 2024-04-04

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/portfolioSuitabilityAnalysis/PortfolioSuitabilityAnalysisResponse.scala`

**Evidence:** anon-2.jsonl:1417 · comment 488849464 · PR 8834 · 2024-04-04

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/requests/hk/portfolioSuitabilityAnalysis/PortfolioSuitabilityAnalysisResponse.scala`

**Explicit source context (pr_title):**

> Feat/INV-2861 dpm portfolio suitability

## A2-1425 — PortfolioSuitabilityAnalysisLogic: We should be able to query CRA profile and extract this once for whole input, instead of doing this every batch?

**Source stance:** suggestion

**Context:**

> PR 8834 (Feat/INV-2861 dpm portfolio suitability), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala; original row 1425.

**Source-preserving request, proposal, or question:**

> We should be able to query CRA profile and extract this once for whole input, instead of doing this every batch?

**Conditions and limits:**

- One CRA lookup/extraction per whole request is preferred to every batch.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1425 · comment 489182391 · PR 8834 · 2024-04-05

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala`

**Evidence:** anon-2.jsonl:1425 · comment 489182391 · PR 8834 · 2024-04-05

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/service/PortfolioSuitabilityAnalysisLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-2861 dpm portfolio suitability

## A2-1439 — BaseServiceLogicImpl: Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless

**Source stance:** explanation

**Context:**

> PR 8906 ([INV-2906] feat(goal): Use Plan readside table for getPlansByCustomerId), goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala; original row 1439.

**Concern stated in the source:** Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless

**Source-preserving request, proposal, or question:**

> Yes all the usage of this API mostly just check if plan exists.. and in general, if you query by not entity-id, you should expect EC regardless

**Conditions and limits:**

- Non-entity-id plan lookup should be expected eventually consistent; consumers mostly check existence.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1439 · comment 491283491 · PR 8906 · 2024-04-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1439 · comment 491283491 · PR 8906 · 2024-04-12

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-2906] feat(goal): Use Plan readside table for getPlansByCustomerId

## A2-1454 — Review: Can we also delete the cassandra readside \+ projection too :pray:

**Source stance:** suggestion

**Context:**

> PR 8677 ([EN-3097] Remove cassandra readside dependency in goal svc), no inline path; original row 1454.

**Source-preserving request, proposal, or question:**

> Can we also delete the cassandra readside \+ projection too :pray:

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1454 · comment 481432330 · PR 8677 · 2024-03-13

**Evidence:** anon-2.jsonl:1454 · comment 481432330 · PR 8677 · 2024-03-13

**Explicit source context (pr_title):**

> [EN-3097] Remove cassandra readside dependency in goal svc

## A2-1457 — PlanRecurringInvestmentScheduleHistoryTableV3: Actually for these tables, we should just drop `investmentAmount` and make `fundingInstructions` required column?

**Source stance:** open-question

**Context:**

> PR 8687 ([EN-3098] Bump plan and recurring schedule pg readside table for new funding instructions field), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleHistoryTableV3.scala; original row 1457.

**Source-preserving request, proposal, or question:**

> Actually for these tables, we should just drop `investmentAmount` and make `fundingInstructions` required column?

**Conditions and limits:**

- New readside tables may drop investmentAmount and require fundingInstructions; this is phrased as a question.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1457 · comment 484816055 · PR 8687 · 2024-03-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleHistoryTableV3.scala`

**Evidence:** anon-2.jsonl:1457 · comment 484816055 · PR 8687 · 2024-03-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleHistoryTableV3.scala`

**Explicit source context (pr_title):**

> [EN-3098] Bump plan and recurring schedule pg readside table for new funding instructions field

## A2-1458 — PlanPostgresProfile: just `fundingInstructionsMapper`

**Source stance:** suggestion

**Context:**

> PR 8687 ([EN-3098] Bump plan and recurring schedule pg readside table for new funding instructions field), goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanPostgresProfile.scala; original row 1458.

**Source-preserving request, proposal, or question:**

> just `fundingInstructionsMapper`

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1458 · comment 486607440 · PR 8687 · 2024-03-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanPostgresProfile.scala`

**Evidence:** anon-2.jsonl:1458 · comment 486607440 · PR 8687 · 2024-03-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanPostgresProfile.scala`

**Explicit source context (hunk):**

>      implicit val recurrenceEndDetailsMapper: BaseColumnType[RecurrenceEndDetails] = jsMapperOf[RecurrenceEndDetails]
>      implicit val recurrenceEndConfigMapper: BaseColumnType[RecurrenceEndConfig] = jsMapperOf[RecurrenceEndConfig]
> +    implicit val fundingInstructionsMapper: BaseColumnType[FundingInstructions] = jsMapperOf[FundingInstructions]
>  
>    }
>  }

**Evidence:** anon-2.jsonl:1458 · comment 486607440 · PR 8687 · 2024-03-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanPostgresProfile.scala`

**Explicit source context (pr_title):**

> [EN-3098] Bump plan and recurring schedule pg readside table for new funding instructions field

## A2-1460 — Review: HK model portfolios are updated more frequently I think, so better to let POps and IO know to stop until we finish migrating data \+ switch the repository

**Source stance:** suggestion

**Context:**

> PR 8854 (Resolve INV-2731: Wire TemplateJdbcHandlerV4 in Hk.), no inline path; original row 1460.

**Concern stated in the source:** HK model portfolios are updated more frequently I think, so better to let POps and IO know to stop until we finish migrating data \+ switch the repository

**Source-preserving request, proposal, or question:**

> HK model portfolios are updated more frequently I think, so better to let POps and IO know to stop until we finish migrating data \+ switch the repository

**Conditions and limits:**

- HK portfolio updates should pause until data migration and repository switch finish; IO/POps coordination is requested.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1460 · comment 488800935 · PR 8854 · 2024-04-04

**Evidence:** anon-2.jsonl:1460 · comment 488800935 · PR 8854 · 2024-04-04

**Explicit source context (pr_title):**

> Resolve INV-2731: Wire TemplateJdbcHandlerV4 in Hk.

## A2-1487 — Review: Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)

**Source stance:** suggestion

**Context:**

> PR 8795 ([PLATFORM-1092] Postgres read side table migration: Stop writing to gcp readside table for transaction), no inline path; original row 1487.

**Concern stated in the source:** Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)

* I believe the `V3` in existing `TransactionJdbcRepositoryV3` / `TransactionJdbcEventProcessorV3` / `TransactionJdbcProjectionV3` refers to the entity V3, not the version of table or projection. I suppose we should have named them `TransactionV3XXX` instead of `TransactionXXXV3`
* Now that the entity migration has completed successfully, I think we can switch the naming as follow:

    * `TransactionV3JdbcRepositoryV4`: ideally we should split this into single repository and versioned dbHandler \(similar to other services\), but we will clean this next time
    * `TransactionV3JdbcProjectionV2`
    

‌

**Source-preserving request, proposal, or question:**

> Existing naming in `transaction` svc is a bit confusing \(introduced by the multiple versions of entity migration\)
> 
> * I believe the `V3` in existing `TransactionJdbcRepositoryV3` / `TransactionJdbcEventProcessorV3` / `TransactionJdbcProjectionV3` refers to the entity V3, not the version of table or projection. I suppose we should have named them `TransactionV3XXX` instead of `TransactionXXXV3`
> * Now that the entity migration has completed successfully, I think we can switch the naming as follow:
> 
>     * `TransactionV3JdbcRepositoryV4`: ideally we should split this into single repository and versioned dbHandler \(similar to other services\), but we will clean this next time
>     * `TransactionV3JdbcProjectionV2`
>     
> 
> ‌

**Conditions and limits:**

- Entity V3 and table/projection version numbers are independent. Proposed naming: TransactionV3JdbcRepositoryV4, TransactionV3JdbcProjectionV2; handler/repository split deferred.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1487 · comment 484744191 · PR 8795 · 2024-03-25

**Evidence:** anon-2.jsonl:1487 · comment 484744191 · PR 8795 · 2024-03-25

**Explicit source context (pr_title):**

> [PLATFORM-1092] Postgres read side table migration: Stop writing to gcp readside table for transaction

## A2-1511 — BrokerAccountDividendDataTable: Missing table name?

**Source stance:** open-question

**Context:**

> PR 8708 ([PLATFORM-1074] Postgres read side table migration: Stop writing to gcp readside table for dividend), dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/db/jdbc/BrokerAccountDividendDataTable.scala; original row 1511.

**Source-preserving request, proposal, or question:**

> Missing table name?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1511 · comment 482752555 · PR 8708 · 2024-03-18

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/db/jdbc/BrokerAccountDividendDataTable.scala`

**Evidence:** anon-2.jsonl:1511 · comment 482752555 · PR 8708 · 2024-03-18

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/db/jdbc/BrokerAccountDividendDataTable.scala`

**Explicit source context (hunk):**

>    val SchemaName = "dividend"
> -  private val TableVersion = 0
> +  private val TableVersion = 1
>    val TableName = s"broker_account_dividends_v$TableVersion"
> +  val IndexNameCustomerId = s"idx_${TableName}_customer_id"
> +  val IndexNameBroker = s"idx_${TableName}_broker"
>  }

**Evidence:** anon-2.jsonl:1511 · comment 482752555 · PR 8708 · 2024-03-18

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/db/jdbc/BrokerAccountDividendDataTable.scala`

**Explicit source context (pr_title):**

> [PLATFORM-1074] Postgres read side table migration: Stop writing to gcp readside table for dividend

## A2-1513 — RedemptionPlanJdbcDbHandlerV3: Can you help me extract const for these 2 indices too :pray:

**Source stance:** suggestion

**Context:**

> PR 8735 (PLATFORM-1094: Switch off gcp for redemption svc), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/db/jdbc/RedemptionPlanJdbcDbHandlerV3.scala; original row 1513.

**Source-preserving request, proposal, or question:**

> Can you help me extract const for these 2 indices too :pray:

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1513 · comment 483156808 · PR 8735 · 2024-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/db/jdbc/RedemptionPlanJdbcDbHandlerV3.scala`

**Evidence:** anon-2.jsonl:1513 · comment 483156808 · PR 8735 · 2024-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/db/jdbc/RedemptionPlanJdbcDbHandlerV3.scala`

**Explicit source context (hunk):**

> +        pkName = RedemptionPlanTableV3.PkName,
>          indexNames = List(
> -          s"redemption_plan_v${tableVersion}_customer_id_idx",
> -          s"redemption_plan_v${tableVersion}_plan_id_idx"
> +          RedemptionPlanTableV3.CustomerIdIndexName,
> +          RedemptionPlanTableV3.PlanIdIndexName
>          )

**Evidence:** anon-2.jsonl:1513 · comment 483156808 · PR 8735 · 2024-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/db/jdbc/RedemptionPlanJdbcDbHandlerV3.scala`

**Explicit source context (pr_title):**

> PLATFORM-1094: Switch off gcp for redemption svc

## A2-1514 — RedemptionPlanTableV3: Not sure why we didn’t just key by planId… and if we already have composite key like this, we don’t need additional index for customerId / planId… but thi...

**Source stance:** suggestion

**Context:**

> PR 8735 (PLATFORM-1094: Switch off gcp for redemption svc), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/db/jdbc/RedemptionPlanTableV3.scala; original row 1514.

**Concern stated in the source:** Not sure why we didn’t just key by planId… and if we already have composite key like this, we don’t need additional index for customerId / planId… but this is existing code, we’ll clean this up next time we upversion this table.

**Source-preserving request, proposal, or question:**

> Not sure why we didn’t just key by planId… and if we already have composite key like this, we don’t need additional index for customerId / planId… but this is existing code, we’ll clean this up next time we upversion this table.

**Conditions and limits:**

- Composite key may already remove need for customerId/planId indexes; current cleanup is deferred until next table version.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1514 · comment 483157442 · PR 8735 · 2024-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/db/jdbc/RedemptionPlanTableV3.scala`

**Evidence:** anon-2.jsonl:1514 · comment 483157442 · PR 8735 · 2024-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/db/jdbc/RedemptionPlanTableV3.scala`

**Explicit source context (pr_title):**

> PLATFORM-1094: Switch off gcp for redemption svc

## A2-1515 — RedemptionRequestJdbcDbHandlerV3: Can you help me rename this to V4 as well?

**Source stance:** suggestion

**Context:**

> PR 8735 (PLATFORM-1094: Switch off gcp for redemption svc), redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/db/jdbc/RedemptionRequestJdbcDbHandlerV3.scala; original row 1515.

**Source-preserving request, proposal, or question:**

> Can you help me rename this to V4 as well?

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1515 · comment 483157671 · PR 8735 · 2024-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/db/jdbc/RedemptionRequestJdbcDbHandlerV3.scala`

**Evidence:** anon-2.jsonl:1515 · comment 483157671 · PR 8735 · 2024-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/db/jdbc/RedemptionRequestJdbcDbHandlerV3.scala`

**Explicit source context (hunk):**

>  import scala.concurrent.{ExecutionContext, Future}
>  
> -class RedemptionRequestJdbcDbHandlerV3(tableVersion: Int, dateTimeProvider: DateTimeProvider, database: Database)(implicit ec: ExecutionContext) extends StrictLogging {
> +class RedemptionRequestJdbcDbHandlerV4(dateTimeProvider: DateTimeProvider, database: Database)(implicit ec: ExecutionContext) extends StrictLogging {
>  
> -  private val redemptionRequestTable = TableQuery(tag => new RedemptionRequestTableV3(tableVersion, tag))
> +  private val redemptionRequestTable = TableQuery[RedemptionRequestTableV4]

**Evidence:** anon-2.jsonl:1515 · comment 483157671 · PR 8735 · 2024-03-19

Source path: `redemption-impl/src/main/scala/com/endowus/silver/redemption/impl/entities/plan/db/jdbc/RedemptionRequestJdbcDbHandlerV3.scala`

**Explicit source context (pr_title):**

> PLATFORM-1094: Switch off gcp for redemption svc

## A2-1538 — HkAdvisoryService: These should be named `locale` to match the query parameter too?

**Source stance:** suggestion

**Context:**

> PR 8429 (Resolve INV-2639: New endpoints for HK fund smart Instruments.), advisory-api/src/main/scala/com/endowus/silver/advisory/api/HkAdvisoryService.scala; original row 1538.

**Source-preserving request, proposal, or question:**

> These should be named `locale` to match the query parameter too?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1538 · comment 480505968 · PR 8429 · 2024-03-11

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/HkAdvisoryService.scala`

**Evidence:** anon-2.jsonl:1538 · comment 480505968 · PR 8429 · 2024-03-11

Source path: `advisory-api/src/main/scala/com/endowus/silver/advisory/api/HkAdvisoryService.scala`

**Explicit source context (pr_title):**

> Resolve INV-2639: New endpoints for HK fund smart Instruments.

## A2-1542 — InstrumentTopHoldingsCache: Why don’t we follow same pattern as other caches here? Just take locale as query input instead? I suppose we might eventually have localisation suppo...

**Source stance:** open-question

**Context:**

> PR 8429 (Resolve INV-2639: New endpoints for HK fund smart Instruments.), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentTopHoldingsCache.scala; original row 1542.

**Concern stated in the source:** Why don’t we follow same pattern as other caches here? Just take locale as query input instead? I suppose we might eventually have localisation support for holdings data too?

**Source-preserving request, proposal, or question:**

> Why don’t we follow same pattern as other caches here? Just take locale as query input instead? I suppose we might eventually have localisation support for holdings data too?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1542 · comment 480519456 · PR 8429 · 2024-03-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentTopHoldingsCache.scala`

**Evidence:** anon-2.jsonl:1542 · comment 480519456 · PR 8429 · 2024-03-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/cache/InstrumentTopHoldingsCache.scala`

**Explicit source context (pr_title):**

> Resolve INV-2639: New endpoints for HK fund smart Instruments.

## A2-1554 — RebalanceRequestTable: We missed a `v` for version here, but it’s consistent in V4 too :sweat_smile: we will change this when we upversion  this table again in future

**Source stance:** explanation

**Context:**

> PR 8646 (PLATFORM-535: Rebalance readside turn off gcp), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestTable.scala; original row 1554.

**Source-preserving request, proposal, or question:**

> We missed a `v` for version here, but it’s consistent in V4 too :sweat_smile: we will change this when we upversion  this table again in future

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Missing v in existing index names is deliberately deferred until next upversion to preserve V4 consistency.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1554 · comment 481364880 · PR 8646 · 2024-03-13

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestTable.scala`

**Evidence:** anon-2.jsonl:1554 · comment 481364880 · PR 8646 · 2024-03-13

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestTable.scala`

**Explicit source context (hunk):**

> -  def indexGoalId = index(name = s"idx_rebalance_request_${version}_goal_id", on = goalId, unique = false)
> -  def indexPlanId = index(name = s"idx_rebalance_request_${version}_plan_id", on = planId, unique = false)
> -  def indexStatusReason = index(name = s"idx_rebalance_request_${version}_status_reason", on = (status, reason), unique = false)
> +  def indexCustomerId = index(name = RebalanceRequestTableV4.customerIdIndex, on = customerId, unique = false)
> +  def indexGoalId = index(name = RebalanceRequestTableV4.goalIdIndex, on = goalId, unique = false)
> +  def indexPlanId = index(name = RebalanceRequestTableV4.planIdIndex, on = planId, unique = false)
> +  def indexStatusReason = index(name = RebalanceRequestTableV4.statusReasonIndex, on = (status, reason), unique = false)

**Evidence:** anon-2.jsonl:1554 · comment 481364880 · PR 8646 · 2024-03-13

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestTable.scala`

**Explicit source context (pr_title):**

> PLATFORM-535: Rebalance readside turn off gcp

## A2-1566 — TransactionJdbcProjectionV2: Let’s not mix the naming, it can be confusing for future readers:

**Source stance:** suggestion

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala; original row 1566.

**Concern stated in the source:** Let’s not mix the naming, it can be confusing for future readers:

* `transaction-jdbc-handler-v1` is projection on V2 entity
* `transaction-jdbc-handler-v2` is projection on V3 entity to pipe data to V2

‌

I think let’s just use a bit more descriptive name to indicate that it’s projection from v3 entity to v2 repo. Maybe `transaction-v3-projection-to-v2-repo-v1`… last v1 is the version of the projection

Do same for the v1\_3 projection.

**Source-preserving request, proposal, or question:**

> Let’s not mix the naming, it can be confusing for future readers:
> 
> * `transaction-jdbc-handler-v1` is projection on V2 entity
> * `transaction-jdbc-handler-v2` is projection on V3 entity to pipe data to V2
> 
> ‌
> 
> I think let’s just use a bit more descriptive name to indicate that it’s projection from v3 entity to v2 repo. Maybe `transaction-v3-projection-to-v2-repo-v1`… last v1 is the version of the projection
> 
> Do same for the v1\_3 projection.

**Conditions and limits:**

- Projection source entity version and target repository version must be explicit; example transaction-v3-projection-to-v2-repo-v1 keeps last v1 as projection version.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1566 · comment 479020069 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala`

**Evidence:** anon-2.jsonl:1566 · comment 479020069 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1567 — TransactionJdbcProjectionV2 dependency name: transactionJdbcRepositoryV2

**Source stance:** requested-change

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala; original row 1567.

**Source-preserving request, proposal, or question:**

> Let’s also name this as `transactionJdbcRepositoryV2` to make it clearer

**Conditions and limits:**

- Use the explicit name transactionJdbcRepositoryV2 in this projection context. This is a naming clarification, not a new table-version or runtime migration request.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1567 · comment 479027346 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala`

**Evidence:** anon-2.jsonl:1567 · comment 479027346 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/entities/transactionV3/jdbc/TransactionJdbcProjectionV2.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1569 — JdbcSchema: You still need to create V2 and V1\_3 until we completely remove the 2 projections right? Otherwise this will scream if we deploy to new dynamic env \(or if it’s res...

**Source stance:** suggestion

**Context:**

> PR 8122 (Feat/INV-2203 clean up transaction old entities), transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/JdbcSchema.scala; original row 1569.

**Concern stated in the source:** You still need to create V2 and V1\_3 until we completely remove the 2 projections right? Otherwise this will scream if we deploy to new dynamic env \(or if it’s reset\)

**Source-preserving request, proposal, or question:**

> You still need to create V2 and V1\_3 until we completely remove the 2 projections right? Otherwise this will scream if we deploy to new dynamic env \(or if it’s reset\)

**Conditions and limits:**

- V2/V1_3 schemas must still be created while their projections exist, including fresh/reset dynamic environments.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1569 · comment 479078276 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/JdbcSchema.scala`

**Evidence:** anon-2.jsonl:1569 · comment 479078276 · PR 8122 · 2024-03-06

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/JdbcSchema.scala`

**Explicit source context (pr_title):**

> Feat/INV-2203 clean up transaction old entities

## A2-1576 — RebateDistributionRequestJdbcRepository: We should just move this to `queryRequestsForPeriod`? Then you don’t need the zeroRebateCount

**Source stance:** suggestion

**Context:**

> PR 8587 ([INV-1996] feat(rebate): dry run fixes), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepository.scala; original row 1576.

**Source-preserving request, proposal, or question:**

> We should just move this to `queryRequestsForPeriod`? Then you don’t need the zeroRebateCount

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1576 · comment 479485483 · PR 8587 · 2024-03-07

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepository.scala`

**Evidence:** anon-2.jsonl:1576 · comment 479485483 · PR 8587 · 2024-03-07

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepository.scala`

**Explicit source context (pr_title):**

> [INV-1996] feat(rebate): dry run fixes

## A2-1580 — RebateDistributionRequestJdbcRepositoryTest: Is it duplicate test? It’s not mockDb btw, it’s real embedded pg

**Source stance:** open-question

**Context:**

> PR 8587 ([INV-1996] feat(rebate): dry run fixes), rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepositoryTest.scala; original row 1580.

**Source-preserving request, proposal, or question:**

> Is it duplicate test? It’s not mockDb btw, it’s real embedded pg

**Conditions and limits:**

- Test uses actual embedded Postgres, not mockDb; duplication is a question.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1580 · comment 479855723 · PR 8587 · 2024-03-08

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepositoryTest.scala`

**Evidence:** anon-2.jsonl:1580 · comment 479855723 · PR 8587 · 2024-03-08

Source path: `rebate-impl/src/test/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepositoryTest.scala`

**Explicit source context (pr_title):**

> [INV-1996] feat(rebate): dry run fixes

## A2-1583 — InstrumentState: Didn’t realize we are using same model in state and db… it should be cheap enough to convert back to DTO and use all the existing methods there?

**Source stance:** suggestion

**Context:**

> PR 8583 ([INV-2368] feat(instrument): Log warn for illiquid alts), instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala; original row 1583.

**Concern stated in the source:** Didn’t realize we are using same model in state and db… it should be cheap enough to convert back to DTO and use all the existing methods there?

**Source-preserving request, proposal, or question:**

> Didn’t realize we are using same model in state and db… it should be cheap enough to convert back to DTO and use all the existing methods there?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1583 · comment 479465028 · PR 8583 · 2024-03-07

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala`

**Evidence:** anon-2.jsonl:1583 · comment 479465028 · PR 8583 · 2024-03-07

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/ces/InstrumentState.scala`

**Explicit source context (pr_title):**

> [INV-2368] feat(instrument): Log warn for illiquid alts

## A2-1596 — RebateDistributionRequestJdbcRepository: This should be named `queryRequestsForPeriod`? Also let’s reuse it for all the methods here?

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepository.scala; original row 1596.

**Source-preserving request, proposal, or question:**

> This should be named `queryRequestsForPeriod`? Also let’s reuse it for all the methods here?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1596 · comment 476102169 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepository.scala`

**Evidence:** anon-2.jsonl:1596 · comment 476102169 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1597 — RebateDistributionRequestTable: Nit: no need `table` in table name

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestTable.scala; original row 1597.

**Source-preserving request, proposal, or question:**

> Nit: no need `table` in table name

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1597 · comment 476102231 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestTable.scala`

**Evidence:** anon-2.jsonl:1597 · comment 476102231 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestTable.scala`

**Explicit source context (hunk):**

> +  private val dbVersion: Int = 4
> +  val schemaName = "rebate"
> +  val tableName = s"rebate_distribution_request_v${dbVersion}"
> +  val pkName = s"${tableName}_pk"
> +  val indexPrefix = s"${tableName}_idx"
> +  val customerIndexName = s"${indexPrefix}_customer_id"
> +  val compositeFromDateToDateIndexName = s"${indexPrefix}_from_date_to_date"

**Evidence:** anon-2.jsonl:1597 · comment 476102231 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestTable.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1598 — RebateDistributionRequestTable: This table can get quite large. I’m not sure if using so many columns in composite key would have significant performance impact or not, as compa...

**Source stance:** open-question

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestTable.scala; original row 1598.

**Concern stated in the source:** This table can get quite large. I’m not sure if using so many columns in composite key would have significant performance impact or not, as compared to maybe just keyed on rebateRequestId and add index for fromDate / toDate / instrumentId / customerId

**Source-preserving request, proposal, or question:**

> This table can get quite large. I’m not sure if using so many columns in composite key would have significant performance impact or not, as compared to maybe just keyed on rebateRequestId and add index for fromDate / toDate / instrumentId / customerId

**Conditions and limits:**

- Composite-key performance versus rebateRequestId plus date/instrument/customer indices is an open design question, not a demonstrated benchmark.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1598 · comment 476103834 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestTable.scala`

**Evidence:** anon-2.jsonl:1598 · comment 476103834 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestTable.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1599 — RebateDistributionSummaryTable: Nit table name

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionSummaryTable.scala; original row 1599.

**Source-preserving request, proposal, or question:**

> Nit table name

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1599 · comment 476104970 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionSummaryTable.scala`

**Evidence:** anon-2.jsonl:1599 · comment 476104970 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionSummaryTable.scala`

**Explicit source context (hunk):**

> +  private val dbVersion: Int = 2
> +  val schemaName = "rebate"
> +  val tableName = s"rebate_distribution_summary_v${dbVersion}"
> +  val pkName = s"${tableName}_pk"
> +
> +  case class RebateDistributionSummary(
> +    broker: Broker,

**Evidence:** anon-2.jsonl:1599 · comment 476104970 · PR 8353 · 2024-02-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionSummaryTable.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1614 — RebateDistributionRequestJdbcRepository: Use `queryRequestsForPeriod` here too?

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepository.scala; original row 1614.

**Source-preserving request, proposal, or question:**

> Use `queryRequestsForPeriod` here too?

**Conditions and limits:**

- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1614 · comment 478111723 · PR 8353 · 2024-03-04

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepository.scala`

**Evidence:** anon-2.jsonl:1614 · comment 478111723 · PR 8353 · 2024-03-04

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/db/jdbc/RebateDistributionRequestJdbcRepository.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1620 — RebateDistributionCommunicationsManager: Each customer wouldn’t have too many trailer rebates per quarter, so I suppose it’s ok to run this aggregation in memory. But we potenti...

**Source stance:** suggestion

**Context:**

> PR 8353 (Feat/INV-1996/automate trailer rebate), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala; original row 1620.

**Concern stated in the source:** Each customer wouldn’t have too many trailer rebates per quarter, so I suppose it’s ok to run this aggregation in memory. But we potentially can push this down to database query and it would be more memory efficient \+ faster computation there.

Example in BQ. Then we can enrich the instrument \+ mandatory rebate data bits on the fly

```
SELECT
  r.customerId,
  r.broker,
  SUM(r.distributedRebateAmount),
  ARRAY_AGG(DISTINCT r.instrumentId)
FROM
  silver_raw_dataset.rebate_distribution_requests r
WHERE
  r.fromDate >= '2023-07-01'
  AND r.toDate <= '2023-09-30'
GROUP BY
  r.customerId,
  r.broker
ORDER BY
  r.customerId,
  r.broker
```

‌

**Source-preserving request, proposal, or question:**

> Each customer wouldn’t have too many trailer rebates per quarter, so I suppose it’s ok to run this aggregation in memory. But we potentially can push this down to database query and it would be more memory efficient \+ faster computation there.
> 
> Example in BQ. Then we can enrich the instrument \+ mandatory rebate data bits on the fly
> 
> ```
> SELECT
>   r.customerId,
>   r.broker,
>   SUM(r.distributedRebateAmount),
>   ARRAY_AGG(DISTINCT r.instrumentId)
> FROM
>   silver_raw_dataset.rebate_distribution_requests r
> WHERE
>   r.fromDate >= '2023-07-01'
>   AND r.toDate <= '2023-09-30'
> GROUP BY
>   r.customerId,
>   r.broker
> ORDER BY
>   r.customerId,
>   r.broker
> ```
> 
> ‌

**Conditions and limits:**

- Per-customer quarterly data is small enough for in-memory aggregation, but database grouping customerId/broker, SUM(distributedRebateAmount), ARRAY_AGG(DISTINCT instrumentId) and later streaming enrichment is an optimization proposal.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1620 · comment 478118131 · PR 8353 · 2024-03-04

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Evidence:** anon-2.jsonl:1620 · comment 478118131 · PR 8353 · 2024-03-04

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/logic/managers/RebateDistributionCommunicationsManager.scala`

**Explicit source context (pr_title):**

> Feat/INV-1996/automate trailer rebate

## A2-1624 — InstrumentTable: [person] [person] let’s create tix, if not already, to completely get rid of V1 instrument repository \+ its entity later

**Source stance:** suggestion

**Context:**

> PR 8384 ([PLATFORM-1067] Postgres read side table migration: Stop writing to gcp readside table for instrument), instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/db/jdbc/InstrumentTable.scala; original row 1624.

**Concern stated in the source:** [person] [person] let’s create tix, if not already, to completely get rid of V1 instrument repository \+ its entity later

**Source-preserving request, proposal, or question:**

> [person] [person] let’s create tix, if not already, to completely get rid of V1 instrument repository \+ its entity later

**Conditions and limits:**

- Complete removal of V1 instrument repository/entity is future ticketed work.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1624 · comment 474051966 · PR 8384 · 2024-02-21

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/db/jdbc/InstrumentTable.scala`

> let’s create tix, if not already, to completely get rid of V1 instrument repository \+ its entity later

**Evidence:** anon-2.jsonl:1624 · comment 474051966 · PR 8384 · 2024-02-21

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/db/jdbc/InstrumentTable.scala`

**Explicit source context (pr_title):**

> [PLATFORM-1067] Postgres read side table migration: Stop writing to gcp readside table for instrument

## A2-1630 — Review: * advisory.corporate\_customer\_v2

**Source stance:** explanation

**Context:**

> PR 8480 ([INV-2529] feat(advisory)(marketdata)(rebalance)(transaction): Dual write for non-readside tables to both GCP and AWS), no inline path; original row 1630.

**Concern stated in the source:** * advisory.corporate\_customer\_v2

    * Dual write
    * Will add pg migration job to copy existing data
    * Will raise another PR to switch repository to aurora after migration job. Keep dual write until data team has migrate
    
* marketdata.instrument\_mstar\_data\_v1

    * Dual write
    * Will trigger endpoint to sync for all instruments
    * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
    
* rebalance.rpc\_communication\_details\_table\_v1

    * Dual write
    * Will add pg migration job to copy existing data
    * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
    
* rebalance.plan\_market\_value\_projection\_v1

    * Dual write
    * ~~Wait one day for timeseries to publish latest MV for all plans~~ Will add pg migration job to copy existing data, cuz the subscriber has filtering logic, so it would take longer than 1d to fully sync naturally
    * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
    
* transaction.fx\_rates\_v1

    * Dual write
    * Will add pg migration job to copy existing data
    * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
    

‌

**Source-preserving request, proposal, or question:**

> * advisory.corporate\_customer\_v2
> 
>     * Dual write
>     * Will add pg migration job to copy existing data
>     * Will raise another PR to switch repository to aurora after migration job. Keep dual write until data team has migrate
>     
> * marketdata.instrument\_mstar\_data\_v1
> 
>     * Dual write
>     * Will trigger endpoint to sync for all instruments
>     * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
>     
> * rebalance.rpc\_communication\_details\_table\_v1
> 
>     * Dual write
>     * Will add pg migration job to copy existing data
>     * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
>     
> * rebalance.plan\_market\_value\_projection\_v1
> 
>     * Dual write
>     * ~~Wait one day for timeseries to publish latest MV for all plans~~ Will add pg migration job to copy existing data, cuz the subscriber has filtering logic, so it would take longer than 1d to fully sync naturally
>     * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
>     
> * transaction.fx\_rates\_v1
> 
>     * Dual write
>     * Will add pg migration job to copy existing data
>     * Will raise another PR to switch repository to aurora after sync, and also stop writing to GCP
>     
> 
> ‌

**Conditions and limits:**

- Five distinct migrations are preserved verbatim. corporate_customer_v2 keeps dual-write until data team migration; instrument_mstar_data_v1 syncs all instruments; other tables use jobs. plan_market_value_projection_v1 explicitly replaces the struck-through one-day natural-sync plan because subscriber filtering delays full sync.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1630 · comment 476601635 · PR 8480 · 2024-02-28

**Evidence:** anon-2.jsonl:1630 · comment 476601635 · PR 8480 · 2024-02-28

**Explicit source context (pr_title):**

> [INV-2529] feat(advisory)(marketdata)(rebalance)(transaction): Dual write for non-readside tables to both GCP and AWS

## A2-1639 — RegionalCustomerTopicCustomer: Btw should we use jdbc readside instead? Eventually we want to get rid of these cassandra readside for general query needs

**Source stance:** open-question

**Context:**

> PR 8215 ([INV-1959] feat(goal): Listen to customer deactivated msg), goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala; original row 1639.

**Concern stated in the source:** Btw should we use jdbc readside instead? Eventually we want to get rid of these cassandra readside for general query needs

**Source-preserving request, proposal, or question:**

> Btw should we use jdbc readside instead? Eventually we want to get rid of these cassandra readside for general query needs

**Conditions and limits:**

- JDBC readside is preferred for general queries as Cassandra readside removal target.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1639 · comment 473484402 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Evidence:** anon-2.jsonl:1639 · comment 473484402 · PR 8215 · 2024-02-20

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/subscribers/RegionalCustomerTopicCustomer.scala`

**Explicit source context (pr_title):**

> [INV-1959] feat(goal): Listen to customer deactivated msg

## A2-1658 — SgAdvisoryLevelClassificationLogic: Should be fast enough cuz compliance won’t need to make any additional lookup or db call. Inter-service calls should be fast within the k8s c...

**Source stance:** suggestion

**Context:**

> PR 8193 (Feat/INV-2101 execution advisory transaction tagging), compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/SgAdvisoryLevelClassificationLogic.scala; original row 1658.

**Concern stated in the source:** Should be fast enough cuz compliance won’t need to make any additional lookup or db call. Inter-service calls should be fast within the k8s cluster.

We don’t need lighting speed for asset transfer either, but wiring this will help to lock down the the touch points of this API, easier to control later

**Source-preserving request, proposal, or question:**

> Should be fast enough cuz compliance won’t need to make any additional lookup or db call. Inter-service calls should be fast within the k8s cluster.
> 
> We don’t need lighting speed for asset transfer either, but wiring this will help to lock down the the touch points of this API, easier to control later

**Conditions and limits:**

- Compliance classification is expected fast because no extra DB/remote lookup; API wiring locks touch points rather than chasing asset-transfer latency.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1658 · comment 465913381 · PR 8193 · 2024-01-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/SgAdvisoryLevelClassificationLogic.scala`

**Evidence:** anon-2.jsonl:1658 · comment 465913381 · PR 8193 · 2024-01-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/advisorylevel/SgAdvisoryLevelClassificationLogic.scala`

**Explicit source context (pr_title):**

> Feat/INV-2101 execution advisory transaction tagging

## A2-1683 — GoalNameSuggestionHelper: Pending confirmation from [person] on the translation. [person] can you help to move this to cache/db lookup in your PR :pray:

**Source stance:** suggestion

**Context:**

> PR 8124 ([INV-2485] feat(advisory)(instrument)(portfolio): Add optional locale param for endpoints serving data requires localisation to FE), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/GoalNameSuggestionHelper.scala; original row 1683.

**Source-preserving request, proposal, or question:**

> Pending confirmation from [person] on the translation. [person] can you help to move this to cache/db lookup in your PR :pray:

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Translation remains pending confirmation; cache/DB lookup for default locale goal names is requested for another PR.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1683 · comment 463366885 · PR 8124 · 2024-01-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/GoalNameSuggestionHelper.scala`

> Pending confirmation from

**Evidence:** anon-2.jsonl:1683 · comment 463366885 · PR 8124 · 2024-01-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/GoalNameSuggestionHelper.scala`

> on the translation.

**Evidence:** anon-2.jsonl:1683 · comment 463366885 · PR 8124 · 2024-01-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/GoalNameSuggestionHelper.scala`

> can you help to move this to cache/db lookup in your PR :pray:

**Evidence:** anon-2.jsonl:1683 · comment 463366885 · PR 8124 · 2024-01-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/GoalNameSuggestionHelper.scala`

**Explicit source context (hunk):**

>  
>    private val DefaultMultiFundFundSmartName = "My Fund Smart Goal"
> -  case class Input(instruments: Seq[InstrumentInfoDtoV2], existingGoalNames: Seq[String])
> +  private val DefaultMultiFundFundSmartNameByLocale: Map[Locale, String] = Map(Locale.ZH_HANT_HK -> "æççè²¡ç®æ¨")
> +
> +  private def getDefaultMultiFundFundSmartName(locale: Option[Locale]): String = {
> +    locale.flatMap(DefaultMultiFundFundSmartNameByLocale.get).getOrElse(DefaultMultiFundFundSmartName)

**Evidence:** anon-2.jsonl:1683 · comment 463366885 · PR 8124 · 2024-01-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/productline/goalcreate/GoalNameSuggestionHelper.scala`

**Explicit source context (pr_title):**

> [INV-2485] feat(advisory)(instrument)(portfolio): Add optional locale param for endpoints serving data requires localisation to FE

## A2-1693 — JdbcSchema: Hmm this looks weird. Ideally we want this `TemplateJdbcDbHandlerV4` injected, or move the `createTableIfNotExists` to its companion object. And templateV4 should be...

**Source stance:** suggestion

**Context:**

> PR 8017 (Feature/PLATFORM-1115 Advisory service PG readside migration), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/db/JdbcSchema.scala; original row 1693.

**Concern stated in the source:** Hmm this looks weird. Ideally we want this `TemplateJdbcDbHandlerV4` injected, or move the `createTableIfNotExists` to its companion object. And templateV4 should be created only in aurora. But extra empty table is gcpcloud is fine for now

We can clean this up later

**Source-preserving request, proposal, or question:**

> Hmm this looks weird. Ideally we want this `TemplateJdbcDbHandlerV4` injected, or move the `createTableIfNotExists` to its companion object. And templateV4 should be created only in aurora. But extra empty table is gcpcloud is fine for now
> 
> We can clean this up later

**Conditions and limits:**

- TemplateJdbcDbHandlerV4 should be injected or companion-createTable; Aurora-only intended, but an extra empty GCP table is explicitly accepted temporarily.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1693 · comment 460275266 · PR 8017 · 2024-01-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/db/JdbcSchema.scala`

**Evidence:** anon-2.jsonl:1693 · comment 460275266 · PR 8017 · 2024-01-11

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/db/JdbcSchema.scala`

**Explicit source context (pr_title):**

> Feature/PLATFORM-1115 Advisory service PG readside migration

## A2-1706 — AuroraJdbcSchema: Can we change to use

**Source stance:** suggestion

**Context:**

> PR 7993 (PLATFORM-1095: Charge service fee_charge_requests pg migration), charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/AuroraJdbcSchema.scala; original row 1706.

**Concern stated in the source:** Can we change to use

```
database.run(FeeChargeRequestJdbcDbHandlerV4.createTable)
```

Then we can drop the createTable method in the dbHandler too

**Source-preserving request, proposal, or question:**

> Can we change to use
> 
> ```
> database.run(FeeChargeRequestJdbcDbHandlerV4.createTable)
> ```
> 
> Then we can drop the createTable method in the dbHandler too

**Conditions and limits:**

- Schema should choose database.run(FeeChargeRequestJdbcDbHandlerV4.createTable), allowing handler createTable instance method removal.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1706 · comment 457961243 · PR 7993 · 2024-01-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/AuroraJdbcSchema.scala`

**Evidence:** anon-2.jsonl:1706 · comment 457961243 · PR 7993 · 2024-01-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/AuroraJdbcSchema.scala`

**Explicit source context (pr_title):**

> PLATFORM-1095: Charge service fee_charge_requests pg migration

## A2-1711 — CustomerAdvisoryProfileJdbcEventProjectionV2: Yea this should give us zero impact for now, cuz we don’t expect `ExpiryDateOverriddenEvt` or `CraExpiredEvt` in prod yet. And data...

**Source stance:** explanation

**Context:**

> PR 7935 ([INV-2418] feat(advisory): Add V2 for customer_advisory_profile tables with new columns for annualIncome/liquidNetWorth/craQuestionnaire), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcEventProjectionV2.scala; original row 1711.

**Concern stated in the source:** Yea this should give us zero impact for now, cuz we don’t expect `ExpiryDateOverriddenEvt` or `CraExpiredEvt` in prod yet. And data team can do a simple check between v1 and v2 table to identify missing records, if at all.

Going forward though, we will certainly start seeing `CraExpiredEvt`. We should look into handle this better, if we ever. need to upversion this table again - which in theory should be ok, cuz we already capture all the fields.

**Source-preserving request, proposal, or question:**

> Yea this should give us zero impact for now, cuz we don’t expect `ExpiryDateOverriddenEvt` or `CraExpiredEvt` in prod yet. And data team can do a simple check between v1 and v2 table to identify missing records, if at all.
> 
> Going forward though, we will certainly start seeing `CraExpiredEvt`. We should look into handle this better, if we ever. need to upversion this table again - which in theory should be ok, cuz we already capture all the fields.

**Conditions and limits:**

- No immediate impact depends on ExpiryDateOverriddenEvt/CraExpiredEvt not yet existing in prod; future upversions must handle CraExpiredEvt, and data-team V1/V2 diff may detect gaps.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1711 · comment 456731490 · PR 7935 · 2023-12-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcEventProjectionV2.scala`

**Evidence:** anon-2.jsonl:1711 · comment 456731490 · PR 7935 · 2023-12-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/hk/profile/CustomerAdvisoryProfileJdbcEventProjectionV2.scala`

**Explicit source context (pr_title):**

> [INV-2418] feat(advisory): Add V2 for customer_advisory_profile tables with new columns for annualIncome/liquidNetWorth/craQuestionnaire

## A2-1712 — RebalanceApplication: Can you help to put a comment here to remind us about the mismatch between table version and readside version, to avoid future confusion :pray:

**Source stance:** suggestion

**Context:**

> PR 7899 (PLATFORM-1097: Rebalance service pg readside migration), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala; original row 1712.

**Source-preserving request, proposal, or question:**

> Can you help to put a comment here to remind us about the mismatch between table version and readside version, to avoid future confusion :pray:

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Hunk example explicitly documents rebalance_plan_v2→projection v1, keeping independent table/projection versions.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1712 · comment 455418391 · PR 7899 · 2023-12-21

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Evidence:** anon-2.jsonl:1712 · comment 455418391 · PR 7899 · 2023-12-21

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Explicit source context (hunk):**

> +
> +    // NOTE: Projection version and table versions might differ. In this case, rebalance_plan_v2 -> projection v1
> +    val rebalancePlanJdbcProjection: RebalancePlanJdbcProjection =
> +      new RebalancePlanJdbcProjection(1, jdbcDatabase, jdbcDatabaseConfig, persistentEntityRefProvider, rebalancePlanJdbcRepository, dateTimeProvider)
> +    rebalancePlanJdbcProjection.start()
> +    val auroraRebalancePlanJdbcProjection: RebalancePlanJdbcProjection =
> +      new RebalancePlanJdbcProjection(2, auroraJdbcDatabase, auroraJdbcDatabaseConfig, persistentEntityRefProvider, auroraRebalancePlanJdbcRepository, dateTimeProvider)

**Evidence:** anon-2.jsonl:1712 · comment 455418391 · PR 7899 · 2023-12-21

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Explicit source context (pr_title):**

> PLATFORM-1097: Rebalance service pg readside migration

## A2-1713 — RebalanceApplication: Actually do we need a new `AuroraJdbcSchema` that doesn’t take in `planMarketValueJdbcHandler` and `rpcCommunicationDetailsJdbcRepository` as we haven’t mi...

**Source stance:** open-question

**Context:**

> PR 7899 (PLATFORM-1097: Rebalance service pg readside migration), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala; original row 1713.

**Concern stated in the source:** Actually do we need a new `AuroraJdbcSchema` that doesn’t take in `planMarketValueJdbcHandler` and `rpcCommunicationDetailsJdbcRepository` as we haven’t migrated them yet?

Currently this works, as they both actually has the GCP jdbc database, and hence not doing anything as tables exist there. But this could be a little confusing

**Source-preserving request, proposal, or question:**

> Actually do we need a new `AuroraJdbcSchema` that doesn’t take in `planMarketValueJdbcHandler` and `rpcCommunicationDetailsJdbcRepository` as we haven’t migrated them yet?
> 
> Currently this works, as they both actually has the GCP jdbc database, and hence not doing anything as tables exist there. But this could be a little confusing

**Conditions and limits:**

- Reusing JdbcSchema can misleadingly ignore its injected database if child handlers are independently injected with GCP.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1713 · comment 455419194 · PR 7899 · 2023-12-21

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Evidence:** anon-2.jsonl:1713 · comment 455419194 · PR 7899 · 2023-12-21

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Explicit source context (pr_title):**

> PLATFORM-1097: Rebalance service pg readside migration

## A2-1714 — RebalanceApplication: So here we are using same class JdbcSchema for both gcpcloud and aurora. It has `planMarketValueJdbcHandler` and `rpcCommunicationDetailsJdbcRepository`, w...

**Source stance:** suggestion

**Context:**

> PR 7899 (PLATFORM-1097: Rebalance service pg readside migration), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala; original row 1714.

**Concern stated in the source:** So here we are using same class JdbcSchema for both gcpcloud and aurora. It has `planMarketValueJdbcHandler` and `rpcCommunicationDetailsJdbcRepository`, which in turn have a `database` injected \(which is from gcpcloud\)

Regardless of whether the JdbcSchema instance is for gcpcloud or aurora, these 2 tables are always for gcpcloud. I thought this would be confusing.

Though it’s noop now, however, maybe it’s better to create a new class `AuroraJdbcSchema` class without these 2 tables?

**Source-preserving request, proposal, or question:**

> So here we are using same class JdbcSchema for both gcpcloud and aurora. It has `planMarketValueJdbcHandler` and `rpcCommunicationDetailsJdbcRepository`, which in turn have a `database` injected \(which is from gcpcloud\)
> 
> Regardless of whether the JdbcSchema instance is for gcpcloud or aurora, these 2 tables are always for gcpcloud. I thought this would be confusing.
> 
> Though it’s noop now, however, maybe it’s better to create a new class `AuroraJdbcSchema` class without these 2 tables?

**Conditions and limits:**

- Suggested AuroraJdbcSchema omits not-yet-migrated plan MV/RPC details tables; row 1715 later accepts shared schema after createTable execution semantics change.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1714 · comment 455691688 · PR 7899 · 2023-12-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Evidence:** anon-2.jsonl:1714 · comment 455691688 · PR 7899 · 2023-12-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/RebalanceApplication.scala`

**Explicit source context (pr_title):**

> PLATFORM-1097: Rebalance service pg readside migration

## A2-1715 — AuroraJdbcSchema: Ah yes, creating them as empty is ok. My previous comment was in context of either the repository or the dbHandler having injected database.

**Source stance:** suggestion

**Context:**

> PR 7899 (PLATFORM-1097: Rebalance service pg readside migration), rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/db/AuroraJdbcSchema.scala; original row 1715.

**Concern stated in the source:** Ah yes, creating them as empty is ok. My previous comment was in context of either the repository or the dbHandler having injected database.

‌

Good examples:

```
_ <- database.run(someDbHandlerOrRepositoryInstanceWithoutInjectedDatabase.createTable)
_ <- database.run(SomeDbHandlerOrRepositoryCompanionObject.createTable)
```

In these cases, the Schema class with its injected database will decide where to create these tables. Hence we will create them in correct place \(even tho non-read-side ones will be empty cuz we haven’t migrated\)

‌

Potentially confusing example \(previous version of this PR\):

```
_ <- someDbHandlerOrRepositoryInstanceWithInjectedDatabase.createTable
```

Here, the injected database of Schema is ignored, and the dbHandler/repository will use its own injected database. And in this specific case, `rpcCommunicationDetailsJdbcRepository` and `planMarketValueJdbcHandler` both have only 1 instance using GCP jdbcDatabase.

‌

Either way, current PR looks good to me!

**Source-preserving request, proposal, or question:**

> Ah yes, creating them as empty is ok. My previous comment was in context of either the repository or the dbHandler having injected database.
> 
> ‌
> 
> Good examples:
> 
> ```
> _ <- database.run(someDbHandlerOrRepositoryInstanceWithoutInjectedDatabase.createTable)
> _ <- database.run(SomeDbHandlerOrRepositoryCompanionObject.createTable)
> ```
> 
> In these cases, the Schema class with its injected database will decide where to create these tables. Hence we will create them in correct place \(even tho non-read-side ones will be empty cuz we haven’t migrated\)
> 
> ‌
> 
> Potentially confusing example \(previous version of this PR\):
> 
> ```
> _ <- someDbHandlerOrRepositoryInstanceWithInjectedDatabase.createTable
> ```
> 
> Here, the injected database of Schema is ignored, and the dbHandler/repository will use its own injected database. And in this specific case, `rpcCommunicationDetailsJdbcRepository` and `planMarketValueJdbcHandler` both have only 1 instance using GCP jdbcDatabase.
> 
> ‌
> 
> Either way, current PR looks good to me!

**Conditions and limits:**

- The database controlling createTable matters: Schema.database.run(action) creates in chosen schema DB even if tables are empty, whereas child.createTable with injected DB silently targets child GCP. Current PR is accepted after that clarification.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1715 · comment 456713630 · PR 7899 · 2023-12-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/db/AuroraJdbcSchema.scala`

**Evidence:** anon-2.jsonl:1715 · comment 456713630 · PR 7899 · 2023-12-27

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/db/AuroraJdbcSchema.scala`

**Explicit source context (pr_title):**

> PLATFORM-1097: Rebalance service pg readside migration

## A2-1723 — InvestmentRequestJdbcDbHandler: Yea this is just direct copy paste from the old InvestmentRequestJdbcRepository. I didn’t bother cuz we will remove it soon, once data side has s...

**Source stance:** explanation

**Context:**

> PR 7846 ([INV-2326] feat(investment): Enforce auto cancellation on cutoff date. Support illiquid alts initial investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentRequestJdbcDbHandler.scala; original row 1723.

**Source-preserving request, proposal, or question:**

> Yea this is just direct copy paste from the old InvestmentRequestJdbcRepository. I didn’t bother cuz we will remove it soon, once data side has switched

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Direct-copied legacy DB handler is accepted temporarily until data-side switch/removal.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1723 · comment 453802845 · PR 7846 · 2023-12-15

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentRequestJdbcDbHandler.scala`

**Evidence:** anon-2.jsonl:1723 · comment 453802845 · PR 7846 · 2023-12-15

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentRequestJdbcDbHandler.scala`

**Explicit source context (hunk):**

> +        pkName = s"investment_request_pk_v${tableVersion}",
> +        indexNames = List(
> +          s"idx_investment_request_v${tableVersion}_plan_id",
> +          s"idx_investment_request_v${tableVersion}_status"
> +        )
> +      )
> +    )

**Evidence:** anon-2.jsonl:1723 · comment 453802845 · PR 7846 · 2023-12-15

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentRequestJdbcDbHandler.scala`

**Explicit source context (pr_title):**

> [INV-2326] feat(investment): Enforce auto cancellation on cutoff date. Support illiquid alts initial investment

## A2-1725 — InvestmentRequestJdbcRepository: Hmm status filter is behaving same as before. I just move the createdAt check to logic layer, cuz we need to check cutOffDate first.

**Source stance:** explanation

**Context:**

> PR 7846 ([INV-2326] feat(investment): Enforce auto cancellation on cutoff date. Support illiquid alts initial investment), investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentRequestJdbcRepository.scala; original row 1725.

**Concern stated in the source:** Hmm status filter is behaving same as before. I just move the createdAt check to logic layer, cuz we need to check cutOffDate first.

Performance wise, yes we will have more data to process, but I think should be cuz number of pending investment shouldn’t be too large?

**Source-preserving request, proposal, or question:**

> Hmm status filter is behaving same as before. I just move the createdAt check to logic layer, cuz we need to check cutOffDate first.
> 
> Performance wise, yes we will have more data to process, but I think should be cuz number of pending investment shouldn’t be too large?

**Conditions and limits:**

- createdAt check moves to logic after cutoff check; status filtering is unchanged, with increased pending-data processing considered acceptable but not benchmarked.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1725 · comment 454316925 · PR 7846 · 2023-12-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentRequestJdbcRepository.scala`

**Evidence:** anon-2.jsonl:1725 · comment 454316925 · PR 7846 · 2023-12-18

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentRequestJdbcRepository.scala`

**Explicit source context (pr_title):**

> [INV-2326] feat(investment): Enforce auto cancellation on cutoff date. Support illiquid alts initial investment

## A2-1727 — InstrumentHoldingDaoJdbc: Yea as we checked, Slick insertOrUpdateAll will always upsert and return the batch size

**Source stance:** explanation

**Context:**

> PR 7862 ([INV-2423] feat(rebate): Batch upsert holdings), rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/db/jdbc/InstrumentHoldingDaoJdbc.scala; original row 1727.

**Source-preserving request, proposal, or question:**

> Yea as we checked, Slick insertOrUpdateAll will always upsert and return the batch size

**Conditions and limits:**

- Reported checked Slick insertOrUpdateAll always upserts and returns batch size; do not treat return count as inserted-only rows.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1727 · comment 454345471 · PR 7862 · 2023-12-18

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/db/jdbc/InstrumentHoldingDaoJdbc.scala`

**Evidence:** anon-2.jsonl:1727 · comment 454345471 · PR 7862 · 2023-12-18

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/db/jdbc/InstrumentHoldingDaoJdbc.scala`

**Explicit source context (pr_title):**

> [INV-2423] feat(rebate): Batch upsert holdings

## A2-1737 — ServiceLogicImpl: Not really, but since I query plan here, I thought I might as well check. We need to add similar check to advisory ProductLine manager too, another PR

**Source stance:** explanation

**Context:**

> PR 7789 ([INV-2326] feat(advisory)(instrument)(investment)(rebalance): Add support instrument subscription cutoff. Improve tradability checks), investment-impl/src/main/scala/com/endowus/silver/investment/impl/logic/service/impl/ServiceLogicImpl.scala; original row 1737.

**Source-preserving request, proposal, or question:**

> Not really, but since I query plan here, I thought I might as well check. We need to add similar check to advisory ProductLine manager too, another PR

**Conditions and limits:**

- The separately quoted inline hunk supplies code context for this terse comment; do not infer from the hunk that the suggestion was implemented or that an unnamed target is certain.
- Deactivated-plan check is opportunistically added after plan lookup; analogous advisory ProductLine manager check is future work.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1737 · comment 452602428 · PR 7789 · 2023-12-12

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1737 · comment 452602428 · PR 7789 · 2023-12-12

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

>  
>      for {
> +      plan <- goalSvc.getPlanById(goalId = goalId, planId = planId).invoke()
> +      _ = if (plan.deactivatedAt.nonEmpty) {
> +        throw new InvestmentSvcException(
> +          s"Plan $planId of goal $goalId is already deactivated",
> +          InvestmentSvcErrorType.INVALID_REQUEST

**Evidence:** anon-2.jsonl:1737 · comment 452602428 · PR 7789 · 2023-12-12

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-2326] feat(advisory)(instrument)(investment)(rebalance): Add support instrument subscription cutoff. Improve tradability checks

## A2-1743 — Review: We can put new optional field in domain, and required field in DTO. And map in the from/toDto methods? No need migration or anything.

**Source stance:** suggestion

**Context:**

> PR 7686 (Feat/INV-2227 fund private document support), no inline path; original row 1743.

**Concern stated in the source:** We can put new optional field in domain, and required field in DTO. And map in the from/toDto methods? No need migration or anything.

**Source-preserving request, proposal, or question:**

> We can put new optional field in domain, and required field in DTO. And map in the from/toDto methods? No need migration or anything.

**Conditions and limits:**

- Optional domain field with required DTO can map defaults in conversion without migration; this is a source-specific new fund-document field proposal.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1743 · comment 448665378 · PR 7686 · 2023-11-29

**Evidence:** anon-2.jsonl:1743 · comment 448665378 · PR 7686 · 2023-11-29

**Explicit source context (pr_title):**

> Feat/INV-2227 fund private document support

## A2-1779 — ServiceLogicImpl: I think the intention was to dump all current data into repository, without having to process every event, cuz we only care about last value of each price date.

**Source stance:** suggestion

**Context:**

> PR 7623 ([PLATFORM-1101] Postgres read side table migration: Create aurora tables for marketdata), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; original row 1779.

**Concern stated in the source:** I think the intention was to dump all current data into repository, without having to process every event, cuz we only care about last value of each price date.

Since it’s not directly affecting your PR, I would just leave it as is.

**Source-preserving request, proposal, or question:**

> I think the intention was to dump all current data into repository, without having to process every event, cuz we only care about last value of each price date.
> 
> Since it’s not directly affecting your PR, I would just leave it as is.

**Conditions and limits:**

- Repository dump intends latest value per price date without replaying every historical event; existing code is accepted as outside current PR.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.
- No inline hunk is available in the source row; the comment does not identify any omitted symbol more precisely.

**Evidence:** anon-2.jsonl:1779 · comment 450174361 · PR 7623 · 2023-12-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1779 · comment 450174361 · PR 7623 · 2023-12-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [PLATFORM-1101] Postgres read side table migration: Create aurora tables for marketdata

## A2-1780 — ServiceLogicImpl: We can already trust data from this repo, no need to go entity if repo says no annual yield

**Source stance:** suggestion

**Context:**

> PR 7742 ([INV-2374] feat(marketdata): Reduce sentry noise when syncing annual yield), marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala; original row 1780.

**Source-preserving request, proposal, or question:**

> We can already trust data from this repo, no need to go entity if repo says no annual yield

**Conditions and limits:**

- Annual-yield repo is trusted; absent annual yield should not force entity fallback.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1780 · comment 450190446 · PR 7742 · 2023-12-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1780 · comment 450190446 · PR 7742 · 2023-12-04

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/logic/service/ServiceLogicImpl.scala`

**Explicit source context (pr_title):**

> [INV-2374] feat(marketdata): Reduce sentry noise when syncing annual yield

## A2-1793 — TemplateData: Yes, I haven’t upversioned and switched to aurora config yet so put the fallback here so that it can work with v3 table :see_no_evil:

**Source stance:** explanation

**Context:**

> PR 7533 ([INV-2214][INV-2216][INV-2218] feat(advisory)(marketdata): Support for FundSmart FundDetails/FundSelection/Collections API), advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/template/TemplateData.scala; original row 1793.

**Concern stated in the source:** Yes, I haven’t upversioned and switched to aurora config yet so put the fallback here so that it can work with v3 table :see_no_evil:

**Source-preserving request, proposal, or question:**

> Yes, I haven’t upversioned and switched to aurora config yet so put the fallback here so that it can work with v3 table :see_no_evil:

**Conditions and limits:**

- Fallback currently supports V3 table until table upversion and Aurora configuration switch.
- PR title and inline path identify source component/operation context only; quoted PR title is metadata, not a claim that the comment proposal was implemented.

**Evidence:** anon-2.jsonl:1793 · comment 444570098 · PR 7533 · 2023-11-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/template/TemplateData.scala`

**Evidence:** anon-2.jsonl:1793 · comment 444570098 · PR 7533 · 2023-11-14

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/template/TemplateData.scala`

**Explicit source context (pr_title):**

> [INV-2214][INV-2216][INV-2218] feat(advisory)(marketdata): Support for FundSmart FundDetails/FundSelection/Collections API

## A3-0001 — InstrumentMstarData JSONB, instrumentId-only lookup, cron sync and annual-yield API transition

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala; PR: Feat/INV-2229 marketdata ex dividend bond yield

**Source-preserving request, proposal, or question:**

> Just store the whole `InstrumentMstarData` as jsonb? So if we add new fields, we just sync all and it will just work, no need to upversion table?
> 
> Our usage would be to look up by instrumentId only anyway.
> 
> 
> 
> Forget about updating only annual yield from event processor - that guy also takes data from a cron sync anyway. Don’t need to worry about about data out-of-sync. And we should switch API to get annual yield from this new table shortly after this.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- The annual-yield event-processor/cron and follow-on API-table proposal is preserved together as one linked storage-and-rollout case.
- Related source rows 1807, 1814, 1819: Storage proposal and tolerated multiple-column/VO alternatives are source-specific and not one mandatory representation.

**Evidence:** anon-2.jsonl:1807 · comment 442778319 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala`

> Just store the whole `InstrumentMstarData` as jsonb? So if we add new fields, we just sync all and it will just work, no need to upversion table?
> 
> Our usage would be to look up by instrumentId only anyway.
> 
> ‌
> 
> Forget about updating only annual yield from event processor - that guy also takes data from a cron sync anyway. Don’t need to worry about about data out-of-sync. And we should switch API to get annual yield from this new table shortly after this.

**Evidence:** anon-2.jsonl:1807 · comment 442778319 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala`

**Explicit source context (hunk):**

> +  def instrumentId = column[String]("instrument_id")
> +  def instrumentMstarData = column[InstrumentMstarData]("instrument_mstar_data")
> +  def lastUpdated = column[Instant]("last_updated_at")
> +
> +  def pk = primaryKey(InstrumentMstarDataTable.PKName, instrumentId)
> +
> +  override def * : ProvenShape[InstrumentMstarDataVo] = (

## A3-0005 — InstrumentMStarAddMarketDataTable.scala: DTO is flat with bunch of optional fields. DB doesn’t have to be

**Source stance:** explanation

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala; PR: Feat/INV-2229 marketdata ex dividend bond yield

**Source-preserving request, proposal, or question:**

> DTO is flat with bunch of optional fields. DB doesn’t have to be

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1811 · comment 442779420 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala`

**Evidence:** anon-2.jsonl:1811 · comment 442779420 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala`

**Explicit source context (hunk):**

> +  def instrumentId = column[String]("instrument_id")
> +  def instrumentMstarData = column[InstrumentMstarData]("instrument_mstar_data")
> +  def lastUpdated = column[Instant]("last_updated_at")
> +
> +  def pk = primaryKey(InstrumentMstarDataTable.PKName, instrumentId)
> +
> +  override def * : ProvenShape[InstrumentMstarDataVo] = (

## A3-0006 — InstrumentMStarAddMarketDataTable.scala: Miscomm then lol. I guess because you wanted to update annual yield via processor?

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala; PR: Feat/INV-2229 marketdata ex dividend bond yield

**Concern stated in the source:** I guess because you wanted to update annual yield via processor?

**Source-preserving request, proposal, or question:**

> Miscomm then lol. I guess because you wanted to update annual yield via processor?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1812 · comment 442780745 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala`

**Evidence:** anon-2.jsonl:1812 · comment 442780745 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/InstrumentMStarAddMarketDataTable.scala`

**Explicit source context (hunk):**

> +  def instrumentId = column[String]("instrument_id")
> +  def instrumentMstarData = column[InstrumentMstarData]("instrument_mstar_data")
> +  def lastUpdated = column[Instant]("last_updated_at")
> +
> +  def pk = primaryKey(InstrumentMstarDataTable.PKName, instrumentId)
> +
> +  override def * : ProvenShape[InstrumentMstarDataVo] = (

## A3-0008 — InstrumentMstarDataVo.scala: We don’t need this VO right? Just store `InstrumentMstarData` directly

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/model/InstrumentMstarDataVo.scala; PR: Feat/INV-2229 marketdata ex dividend bond yield

**Source-preserving request, proposal, or question:**

> We don’t need this VO right? Just store `InstrumentMstarData` directly

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 1807, 1814, 1819: Storage proposal and tolerated multiple-column/VO alternatives are source-specific and not one mandatory representation.

**Evidence:** anon-2.jsonl:1814 · comment 442801220 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/model/InstrumentMstarDataVo.scala`

**Evidence:** anon-2.jsonl:1814 · comment 442801220 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/model/InstrumentMstarDataVo.scala`

**Explicit source context (hunk):**

> +
> +import java.time.Instant
> +
> +case class InstrumentMstarDataVo(
> +  instrumentId: String,
> +  instrumentMstarData: InstrumentMstarData,
> +  lastUpdated: Instant

## A3-0009 — MarketdataPostgresProfile.scala: Can remove this one

**Source stance:** requested-change

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/MarketdataPostgresProfile.scala; PR: Feat/INV-2229 marketdata ex dividend bond yield

**Source-preserving request, proposal, or question:**

> Can remove this one

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- The comment's target is identified only by the accompanying hunk.

**Evidence:** anon-2.jsonl:1815 · comment 442801405 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/MarketdataPostgresProfile.scala`

**Evidence:** anon-2.jsonl:1815 · comment 442801405 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/jdbc/MarketdataPostgresProfile.scala`

**Explicit source context (hunk):**

> +
> +  override val api: MarketdataExtendedApi = new MarketdataExtendedApi {}
> +
> +  val maxDecimalPoints = "NUMERIC(30,12)"
> +
> +  trait MarketdataExtendedApi extends ExtendedApi {
> +    implicit val currencyStringMapper: BaseColumnType[CurrencyUnit] =

## A3-0012 — InstrumentMstarDataVo.scala: You still can use multiple columns extracting data from `InstrumentMstarData`. But ok it doesn’t matter. I guess we also have this \*VO / \*Data in ot

**Source stance:** explanation

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/model/InstrumentMstarDataVo.scala; PR: Feat/INV-2229 marketdata ex dividend bond yield

**Source-preserving request, proposal, or question:**

> You still can use multiple columns extracting data from `InstrumentMstarData`. But ok it doesn’t matter. I guess we also have this \*VO / \*Data in other places.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 1807, 1814, 1819: Storage proposal and tolerated multiple-column/VO alternatives are source-specific and not one mandatory representation.

**Evidence:** anon-2.jsonl:1819 · comment 442806030 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/model/InstrumentMstarDataVo.scala`

**Evidence:** anon-2.jsonl:1819 · comment 442806030 · PR 7443 · 2023-11-08

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/db/model/InstrumentMstarDataVo.scala`

**Explicit source context (hunk):**

> +
> +import java.time.Instant
> +
> +case class InstrumentMstarDataVo(
> +  instrumentId: String,
> +  instrumentMstarData: InstrumentMstarData,
> +  lastUpdated: Instant

## A3-0023 — InstrumentV2JdbcRepository.scala: So we change this back to exact match rather than contain?

**Source stance:** open-question

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcRepository.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> So we change this back to exact match rather than contain?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1831 · comment 439499383 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcRepository.scala`

**Evidence:** anon-2.jsonl:1831 · comment 439499383 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcRepository.scala`

**Explicit source context (hunk):**

> +    db.run {
> +      for {
> +        result <- instruments
> +          .filter(_.tradingRestrictions @> tradingRestrictions.bind)
> +          .result
> +      } yield result.toList
> +    }

## A3-0025 — InstrumentJdbcEventProcessorV2.scala: follow the pattern we have in other services with JdbcSchema

**Source stance:** requested-change

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessorV2.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> Let’s follow the pattern we have in other services with JdbcSchema

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:1833 · comment 439499518 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessorV2.scala`

## A3-0026 — InstrumentV2JdbcDbHandler.scala: We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> We don’t really need transaction for readside so we can inject db here, and return Future… it’s easier to use and mock in test if needed

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1834 · comment 439499719 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala`

**Evidence:** anon-2.jsonl:1834 · comment 439499719 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/v2/db/jdbc/InstrumentV2JdbcDbHandler.scala`

**Explicit source context (hunk):**

> +  private val instruments = TableQuery[InstrumentV2Table]
> +
> +  def upsert(instrument: Instrument): Future[Unit] = {
> +    db.run(instruments.insertOrUpdate(instrument)).flatMap {
> +      case 0 | 1 => Future.unit
> +      case n     => Future.failed(new Exception(s"Expected 0 or 1 updated, but got $n"))
> +    }

## A3-0027 — InstrumentJdbcEventProcessorV2.scala: It’s just a bit cleaner to group them together, both those with event processor and those pure CRUD

**Source stance:** explanation

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessorV2.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> It’s just a bit cleaner to group them together, both those with event processor and those pure CRUD

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1835 · comment 439501224 · PR 7211 · 2023-10-27

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/jdbc/InstrumentJdbcEventProcessorV2.scala`

## A3-0028 — InstrumentDbEventProcessorNew.scala: we can remove already. BQ is currently using pg instruments\_v4

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/InstrumentDbEventProcessorNew.scala; PR: Resolve INV-2127: New read side table instrument entity v2

**Source-preserving request, proposal, or question:**

> I think we can remove already. BQ is currently using pg instruments\_v4

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:1837 · comment 440529544 · PR 7211 · 2023-10-31

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/processors/InstrumentDbEventProcessorNew.scala`

## A3-0032 — DailyMvAuditEntry array_agg/customerId optimization deferred over Slick GROUP BY issues

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvAuditEntryJdbcRepository.scala; PR: [INV-2015] feat(charge): Support estimated daily fee

**Concern stated in the source:** so that we can reduce the number of calls, but there are issues with slick and aggregate function with group by [<url> data-inline-card='' }  so I’m not taking chances

**Source-preserving request, proposal, or question:**

> We potentially can aggregate more in db layer, e.g.
> 
> ```
> SELECT customerId, array_agg(businessDate)
> ```
> 
> so that we can reduce the number of calls, but there are issues with slick and aggregate function with group by [<url> data-inline-card='' }  so I’m not taking chances

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- The array_agg/group-by optimization is explicitly deferred due to Slick issues, not required.

**Evidence:** anon-2.jsonl:1842 · comment 438138531 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvAuditEntryJdbcRepository.scala`

**Evidence:** anon-2.jsonl:1842 · comment 438138531 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvAuditEntryJdbcRepository.scala`

**Explicit source context (hunk):**

> +  implicit private val session: SlickSession = SlickSession.forDbAndProfile(database, ChargeServicePostgresProfile)
> +
> +  private val dailyMvAuditEntries = TableQuery[DailyMvAuditEntryTable]
> +
> +  def streamCustomerUpdatedMvBusinessDates(feeType: FeeType, from: Instant, to: Instant, businessDateCutOff: LocalDate): Source[CustomerUpdatedMvBusinessDate, NotUsed] = {
> +    Slick.source {
> +      dailyMvAuditEntries

## A3-0033 — DailyMvPersistenceHelper.scala: Extract this logic out of `PlanTimeSeriesTopicSubscriber` and let it handle updating both dailyMV and dailyMVAuditEntry tables

**Source stance:** requested-change

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvPersistenceHelper.scala; PR: [INV-2015] feat(charge): Support estimated daily fee

**Source-preserving request, proposal, or question:**

> Extract this logic out of `PlanTimeSeriesTopicSubscriber` and let it handle updating both dailyMV and dailyMVAuditEntry tables

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1843 · comment 438139789 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvPersistenceHelper.scala`

**Evidence:** anon-2.jsonl:1843 · comment 438139789 · PR 7266 · 2023-10-23

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvPersistenceHelper.scala`

**Explicit source context (hunk):**

> +      .maximumSize(20000)
> +      .buildAsyncFuture { case (goalId, planId) => queryPlanProfileDetail(goalId, planId) }
> +
> +  def batchUpsert(
> +    customerId: UUID,
> +    goalId: UUID,
> +    planId: UUID,

## A3-0038 — DailyMvAuditEntryJdbcRepository.scala: good point. I’ll add feeType column to this instead

**Source stance:** requested-change

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvAuditEntryJdbcRepository.scala; PR: [INV-2015] feat(charge): Support estimated daily fee

**Source-preserving request, proposal, or question:**

> Yeah good point. I’ll add feeType column to this instead

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1848 · comment 440195409 · PR 7266 · 2023-10-30

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvAuditEntryJdbcRepository.scala`

**Evidence:** anon-2.jsonl:1848 · comment 440195409 · PR 7266 · 2023-10-30

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvAuditEntryJdbcRepository.scala`

**Explicit source context (hunk):**

> +
> +  def streamCustomerUpdatedMvBusinessDates(feeType: FeeType, from: Instant, to: Instant, businessDateCutOff: LocalDate): Source[CustomerUpdatedMvBusinessDate, NotUsed] = {
> +    Slick.source {
> +      dailyMvAuditEntries
> +        .filter(_.feeType === feeType)
> +        .filter(_.lastUpdatedAt >= from)
> +        .filter(_.lastUpdatedAt <= to)

## A3-0039 — DailyMvPersistenceHelper.scala: Can. This cache is very small anyway. I’ll put a month?

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvPersistenceHelper.scala; PR: [INV-2015] feat(charge): Support estimated daily fee

**Source-preserving request, proposal, or question:**

> Can. This cache is very small anyway. I’ll put a month?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1849 · comment 440195538 · PR 7266 · 2023-10-30

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvPersistenceHelper.scala`

**Evidence:** anon-2.jsonl:1849 · comment 440195538 · PR 7266 · 2023-10-30

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvPersistenceHelper.scala`

**Explicit source context (hunk):**

> +
> +  private val planProfileDetailCache: AsyncLoadingCache[(UUID, UUID), PlanProfileDetail] =
> +    Scaffeine()
> +      .recordStats()
> +      .expireAfterWrite(30.day)
> +      .maximumSize(20000)
> +      .buildAsyncFuture { case (goalId, planId) => queryPlanProfileDetail(goalId, planId) }

## A3-0040 — BaseServiceLogicImpl.scala: Good catch. Let me just handle empty MV inside batchUpsert then

**Source stance:** requested-change

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala; PR: [INV-2015] feat(charge): Support estimated daily fee

**Source-preserving request, proposal, or question:**

> Good catch. Let me just handle empty MV inside batchUpsert then

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1850 · comment 440195725 · PR 7266 · 2023-10-30

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1850 · comment 440195725 · PR 7266 · 2023-10-30

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> -                mv <- db.run(dailyMvJdbcRepository.batchUpsert(dailyMvs)).map(_ => dailyMvs)
> -                r = if (mv.nonEmpty) {
> -                  s"Updated MV(${mv.length}). Customer: ${mv.head.customerId}, Plan: ${mv.head.planId}, GoalType: ${mv.head.goalType} Plan: ${mv.head.planId}, Ccy: ${mv.head.planCcy}, Business dates: ${mv.head.businessDate}."
> +                _ <- dailyMvPersistenceHelper.batchUpsert(
> +                  customerId = plan.customerId,
> +                  goalId = plan.goalId,
> +                  planId = plan.planId,

## A3-0041 — DailyFeeCalculationManager.scala: ok. Will oso clean up fees older than business date cutoff :thumbsup:

**Source stance:** requested-change

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/DailyFeeCalculationManager.scala; PR: [INV-2015] feat(charge): Support estimated daily fee

**Source-preserving request, proposal, or question:**

> Yeah ok. Will oso clean up fees older than business date cutoff :thumbsup:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1851 · comment 440195842 · PR 7266 · 2023-10-30

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/DailyFeeCalculationManager.scala`

**Evidence:** anon-2.jsonl:1851 · comment 440195842 · PR 7266 · 2023-10-30

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/DailyFeeCalculationManager.scala`

**Explicit source context (hunk):**

> +    for {
> +      _ <- triggerEstimatedDailyFeeCalculationFromUpdatedMv(feeType = NonAlts, mvUpdatedFrom = mvUpdatedFrom, mvUpdatedTo = mvUpdatedTo)
> +      _ <- triggerEstimatedDailyFeeCalculationFromUpdatedMv(feeType = Alts, mvUpdatedFrom = mvUpdatedFrom, mvUpdatedTo = mvUpdatedTo)
> +      _ <- dailyMvAuditEntryJdbcDbHandler.removeOldEntries(oldMvEntriesLastUpdatedAtCutOff)
> +    } yield Done
> +  }
> +

## A3-0042 — InstrumentTable.scala: maybe change this as tableNamePrefix and use it below?

**Source stance:** suggestion

**Context:**

> instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/db/jdbc/InstrumentTable.scala; PR: [PLATFORM-1066] Postgres read side table migration: Create aurora tables for instrument

**Source-preserving request, proposal, or question:**

> Nit: maybe change this as tableNamePrefix and use it below?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1853 · comment 439086829 · PR 7127 · 2023-10-26

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/db/jdbc/InstrumentTable.scala`

**Evidence:** anon-2.jsonl:1853 · comment 439086829 · PR 7127 · 2023-10-26

Source path: `instrument-impl/src/main/scala/com/endowus/silver/instrument/impl/instrument/db/jdbc/InstrumentTable.scala`

**Explicit source context (hunk):**

> val tableName = "instruments_v4"
>  }
>  
> -class InstrumentTable(tag: Tag)

## A3-0116 — RPC endpoints intentionally differ: customer readside versus goal entity consistency

**Source stance:** requested-change

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [INV-1988] feat(gateway, rebalance): migrate recommended portfolio changes endpoint from davinci

**Source-preserving request, proposal, or question:**

> Ah nevermind me lol. Let’s put a comment to explain that customer endpoint is using readside while goal endpoint is using entity for data consistency

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Related source rows 1932, 1933: Struck-through shared-code suggestion is revised to explain customer-readside versus goal-entity behavior.

**Evidence:** anon-2.jsonl:1933 · comment 431718424 · PR 6874 · 2023-09-29

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:1933 · comment 431718424 · PR 6874 · 2023-09-29

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +      plans = goal.plans.map(p => (p.planId, p.tradingAccountType, goal.name, goal.investmentGoalType))
> +      recommendedPortfolioChangeDtos <- Source(plans)
> +        .mapAsync(2) {
> +          case (planId, tradingAccountType, goalName, goalType) =>
> +            for {
> +              rebalanceRequestDtos <- getRebalanceRequestDtosForGoal(
> +                customerId = goal.customerId,

## A3-0124 — ServiceLogicImpl.scala: We have utils in OptionUtils so this can be written as ``` rpcCmsWebflowIdJdbcRepository .find(portfolioId, effectiveDate) .map(_.map { entry => RpcCm

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Feat/INV-1986/rpc-communication-details-crud

**Source-preserving request, proposal, or question:**

> We have utils in OptionUtils so this can be written as
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .find(portfolioId, effectiveDate)
>   .map(_.map { entry =>
>     RpcCmsWebflowIdEntryDto(
>       portfolioId = entry.portfolioId,
>       effectiveDate = entry.effectiveDate,
>       collectionId = entry.collectionId,
>       itemId = entry.itemId,
>       description = entry.description,
>       updatedAt = entry.updatedAt
>     )
>   }.onNone(logger.warn(...)))
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1942 · comment 429926815 · PR 6989 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

> We have utils in OptionUtils so this can be written as
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .find(portfolioId, effectiveDate)
>   .map(_.map { entry =>
>     RpcCmsWebflowIdEntryDto(
>       portfolioId = entry.portfolioId,
>       effectiveDate = entry.effectiveDate,
>       collectionId = entry.collectionId,
>       itemId = entry.itemId,
>       description = entry.description,
>       updatedAt = entry.updatedAt
>     )
>   }.onNone(logger.warn(...)))
> ```
> 
> ‌

## A3-0125 — ServiceLogicImpl.scala: Same here, you don’t need to match. Can extract to reuse same toDto method as well ``` rpcCmsWebflowIdJdbcRepository .findByItemId(itemId) .map(_.map(

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: Feat/INV-1986/rpc-communication-details-crud

**Source-preserving request, proposal, or question:**

> Same here, you don’t need to match. Can extract to reuse same toDto method as well
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .findByItemId(itemId)
>   .map(_.map(toDto))
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:1943 · comment 429927351 · PR 6989 · 2023-09-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

> Same here, you don’t need to match. Can extract to reuse same toDto method as well
> 
> ```
> rpcCmsWebflowIdJdbcRepository
>   .findByItemId(itemId)
>   .map(_.map(toDto))
> ```
> 
> ‌

## A3-0127 — RebalanceService.scala: Should we query by collectionId \+ itemId then, as I understand this is composite key from Webflow?

**Source stance:** open-question

**Context:**

> rebalance-api/src/main/scala/com/endowus/silver/rebalance/api/RebalanceService.scala; PR: Feat/INV-1986/rpc-communication-details-crud

**Source-preserving request, proposal, or question:**

> Should we query by collectionId \+ itemId then, as I understand this is composite key from Webflow?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:1945 · comment 430310658 · PR 6989 · 2023-09-25

Source path: `rebalance-api/src/main/scala/com/endowus/silver/rebalance/api/RebalanceService.scala`

**Evidence:** anon-2.jsonl:1945 · comment 430310658 · PR 6989 · 2023-09-25

Source path: `rebalance-api/src/main/scala/com/endowus/silver/rebalance/api/RebalanceService.scala`

**Explicit source context (hunk):**

> def getRecommendedPortfolioChangesSummary(planId: UUID, requestId: UUID, displayCcy: CurrencyUnit): ServiceCall[NotUsed, RecommendedPortfolioChangesSummaryDto]
>  
> +  def findRpcCommunicationDetails(portfolioId: UUID, effectiveDate: LocalDate, locale: Locale): ServiceCall[NotUsed, Option[RpcCommunicationDetailsDto]]
> +

## A3-0221 — InstrumentDailyReturnIndexDaoJdbc.scala: Change this so that we actually test the clause limit in test

**Source stance:** requested-change

**Context:**

> performance-impl/src/main/scala/com/endowus/silver/performance/impl/db/marketdata/jdbc/InstrumentDailyReturnIndexDaoJdbc.scala; PR: feat(performance): Fix flaky InstrumentDailyReturnIndexDaoJdbcTest

**Concern stated in the source:** Change this so that we actually test the clause limit in test

**Source-preserving request, proposal, or question:**

> Change this so that we actually test the clause limit in test

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2043 · comment 823818136 · PR 14248 · 2026-07-09

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/db/marketdata/jdbc/InstrumentDailyReturnIndexDaoJdbc.scala`

**Evidence:** anon-2.jsonl:2043 · comment 823818136 · PR 14248 · 2026-07-09

Source path: `performance-impl/src/main/scala/com/endowus/silver/performance/impl/db/marketdata/jdbc/InstrumentDailyReturnIndexDaoJdbc.scala`

**Explicit source context (hunk):**

> def findMany(instrumentId: String, dates: Set[LocalDate], sort: Option[SortOrder]): Future[List[InstrumentDailyReturnIndex]] = {
>      Source(dates)
> -      .grouped(InClauseLimit)
> +      .grouped(inClauseLimit)
>        .flatMapConcat(Source.single(_).mapAsync(parallelism = 1)(findIn(instrumentId, _, sort)).mapConcat(identity))
>        .runWith(Sink.collection[InstrumentDailyReturnIndex, List[InstrumentDailyReturnIndex]])
>    }

## A3-0254 — PlanRecurringInvestmentScheduleTable.scala: Do we need to key on all 3? Just planId?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleTable.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> Do we need to key on all 3? Just planId?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2077 · comment 422182120 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleTable.scala`

**Evidence:** anon-2.jsonl:2077 · comment 422182120 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleTable.scala`

**Explicit source context (hunk):**

> +  def endingOnDate: Rep[Option[LocalDate]] = column[Option[LocalDate]]("ending_on_date")
> +  def recurrenceEndConfig: Rep[Option[RecurrenceEndConfig]] = column[Option[RecurrenceEndConfig]]("recurrence_end_config")
> +  def expiredOnDate: Rep[Option[LocalDate]] = column[Option[LocalDate]]("expired_on_date")
> +
> +  def pk = primaryKey(PlanRecurringInvestmentScheduleTable.PkName, planId)
> +  def indexEndingOnDate = index(s"${PlanRecurringInvestmentScheduleTable.EndingOnDateIndex}", endingOnDate, unique = false)
> +  def indexExpiredOnDate = index(s"${PlanRecurringInvestmentScheduleTable.ExpiredOnDateIndex}", expiredOnDate, unique = false)

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

## A3-0257 — RecurringInvestmentScheduleJdbcEventProcessor.scala: `upsertPlanRecurringInvestmentSchedule` will skip if schedule is None? don’t we need another method to delete in dbHandler?

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> `upsertPlanRecurringInvestmentSchedule` will skip if schedule is None? don’t we need another method to delete in dbHandler?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2081 · comment 422183564 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2081 · comment 422183564 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +        endingOnDate = scheduleEndingOnDate,
> +        recurrenceEndConfig = scheduleEndConfig,
> +        expiredOnDate = getExpiredOnDate(scheduleEndingOnDate, scheduleEndConfig),
> +        updatedAt = updatedAt
> +      )
> +      val resultFut = for {
> +        result <- scheduleJdbcDbHandler.upsert(schedule)

## A3-0258 — PlanRecurringInvestmentScheduleJdbcRepositoryImpl.scala: So we want to support 2 modes of query? 1. query by expiry date \(don’t care how it expires, either explicit date or occurrence count\) 2. query by ex

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleJdbcRepositoryImpl.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> So we want to support 2 modes of query?
> 
> 1. query by expiry date \(don’t care how it expires, either explicit date or occurrence count\)
> 2. query by explicit expiry date specified by customer
> 
> Can you explain the use case for \(2\)? I’m thinking maybe better to break into 2 methods to make it clearer

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2082 · comment 422184041 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleJdbcRepositoryImpl.scala`

**Evidence:** anon-2.jsonl:2082 · comment 422184041 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleJdbcRepositoryImpl.scala`

**Explicit source context (hunk):**

> +            .filter(_.endingOnDate === date)
> +            .result
> +        )
> +      )
> +  }
> +
> +  override def streamRecurringInvestmentSchedulesByExpiredOnDate(

## A3-0259 — : Can we add tests too please, for both processor and repository

**Source stance:** requested-change

**Context:**

> None; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> Can we add tests too please, for both processor and repository

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2083 · comment 422184060 · PR 6740 · 2023-08-25

## A3-0261 — PlanRecurringInvestmentScheduleTable.scala: Note: No need index on PlanId if it’s pk

**Source stance:** explanation

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleTable.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> Note: No need index on PlanId if it’s pk

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2085 · comment 422184854 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleTable.scala`

**Evidence:** anon-2.jsonl:2085 · comment 422184854 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleTable.scala`

**Explicit source context (hunk):**

> +  def endingOnDate: Rep[Option[LocalDate]] = column[Option[LocalDate]]("ending_on_date")
> +  def recurrenceEndConfig: Rep[Option[RecurrenceEndConfig]] = column[Option[RecurrenceEndConfig]]("recurrence_end_config")
> +  def expiredOnDate: Rep[Option[LocalDate]] = column[Option[LocalDate]]("expired_on_date")
> +
> +  def pk = primaryKey(PlanRecurringInvestmentScheduleTable.PkName, planId)
> +  def indexEndingOnDate = index(s"${PlanRecurringInvestmentScheduleTable.EndingOnDateIndex}", endingOnDate, unique = false)
> +  def indexExpiredOnDate = index(s"${PlanRecurringInvestmentScheduleTable.ExpiredOnDateIndex}", expiredOnDate, unique = false)

## A3-0262 — RecurringInvestmentScheduleJdbcEventProcessor.scala: I’m now thinking we should add composite key using combination of fields… updatedAt should definitely part of that

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> I’m now thinking we should add composite key using combination of fields… updatedAt should definitely part of that

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Related source rows 2080, 2086, 2089: History PK opinion evolves from broad composite suggestion to duplicate-tolerance or fakeUUID PK; do not flatten to mandatory wide composite key.

**Evidence:** anon-2.jsonl:2086 · comment 422228724 · PR 6740 · 2023-08-25

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

## A3-0263 — Schedule deactivation domain events belong in command/PlanProjection; JDBC writes only

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Source-preserving request, proposal, or question:**

> Ideally I’d prefer that either:
> 
> * `DeactivateGoalCmdHandler` should also check and emit `PlanRecurringInvestmentScheduleRemovedEvt`
> * or `PlanProjection` to handle `PlanDeactivatedEvt` and trigger cmd `StopRecurringInvestmentScheduleCmd`
> 
> Then in jdbc projections \(both history and latest\), we just perform purely db update.
> 
> 
> 
> Today we don’t have such logic, and the `RecurringInvestmentProcessor` only cares about active plans, and that’s why it works.
> 
> I think let’s add the above logic, and we can leave the old inactive plans with recurring schedule as is, or run a script to stop them. But let’s not mix the logic here.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Do not mix deactivation/schedule domain behavior into JDBC projections; preserves both command/event alternatives and historical inactive-plan options.

**Evidence:** anon-2.jsonl:2087 · comment 422617963 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleHistoryJdbcEventProcessor.scala`

> Ideally I’d prefer that either:
> 
> * `DeactivateGoalCmdHandler` should also check and emit `PlanRecurringInvestmentScheduleRemovedEvt`
> * or `PlanProjection` to handle `PlanDeactivatedEvt` and trigger cmd `StopRecurringInvestmentScheduleCmd`
> 
> Then in jdbc projections \(both history and latest\), we just perform purely db update.
> 
> ‌
> 
> Today we don’t have such logic, and the `RecurringInvestmentProcessor` only cares about active plans, and that’s why it works.
> 
> I think let’s add the above logic, and we can leave the old inactive plans with recurring schedule as is, or run a script to stop them. But let’s not mix the logic here.
> 
> ‌

## A3-0264 — Mutable endingOnDate/toBeExpiredOn indices: catch up projection before adding indices

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleJdbcRepositoryImpl.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Concern stated in the source:** Indices on customerId/goalId are generally ok because for a given planId \(pkey\), these fields do not change.

**Source-preserving request, proposal, or question:**

> Just something to note, index is not free, it has impact on writes. Indices on customerId/goalId are generally ok because for a given planId \(pkey\), these fields do not change. It’s just single insert/update for these indices.
> 
> However, endingOnDate / toBeExpiredOn fields can be updated a given planId. That would be a delete and then insert for these indices. It might be ok still for our usage, but just something to think about. I would suggest we release the projection to prod without these 2 indices first, let it catch up with all the events, then we make another release to add the indices.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve rollout: project without endingOnDate/toBeExpiredOn indices, catch up all events, release indices later; mutable indexed fields require delete+insert.

**Evidence:** anon-2.jsonl:2088 · comment 422619100 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleJdbcRepositoryImpl.scala`

**Evidence:** anon-2.jsonl:2088 · comment 422619100 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/PlanRecurringInvestmentScheduleJdbcRepositoryImpl.scala`

**Explicit source context (hunk):**

> +            .filter(_.endingOnDate === date)
> +            .result
> +        )
> +      )
> +  }
> +
> +  override def streamRecurringInvestmentSchedulesByExpiredOnDate(

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

## A3-0267 — RecurringInvestmentScheduleJdbcEventProcessor.scala: In theory again, since we don’t actually care about this table from application side, we should just add another topic producer that re-publish all me

**Source stance:** suggestion

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala; PR: [EN-2021] Add readside table for plan recurring investment

**Concern stated in the source:** Creating a table in PG so that BQ can ingest from PG to BQ sounds a bit extra.

**Source-preserving request, proposal, or question:**

> In theory again, since we don’t actually care about this table from application side, we should just add another topic producer that re-publish all messages again for data side to consume, and populate the table in BQ directly.
> 
> Creating a table in PG so that BQ can ingest from PG to BQ sounds a bit extra. But I suppose we might not have bandwidth to do this yet.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Direct republish-to-BQ alternative is explicitly bandwidth constrained.

**Evidence:** anon-2.jsonl:2091 · comment 422622805 · PR 6740 · 2023-08-28

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/processors/jdbc/RecurringInvestmentScheduleJdbcEventProcessor.scala`

## A3-0319 — Schedule history created/stopped rows have no link ID: data-team join expectations

**Source stance:** open-question

**Context:**

> goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleHistory.scala; PR: [EN-1361] Create read side history table for Recurring investment schedule

**Source-preserving request, proposal, or question:**

> Did we confirm with data team that they will know how to read this table? For same schedule, when it’s stopped/cancelled, there will be 2 rows \(one for created, and one for cancelled/stopped\) without any obvious reference id to link them \(will need to link using data fields\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2144 · comment 421206881 · PR 6668 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleHistory.scala`

**Evidence:** anon-2.jsonl:2144 · comment 421206881 · PR 6668 · 2023-08-22

Source path: `goal-impl/src/main/scala/com/endowus/silver/goal/impl/entities/goal/db/jdbc/models/PlanRecurringInvestmentScheduleHistory.scala`

**Explicit source context (hunk):**

> +  investmentAmount: BigDecimal,
> +  createdAt: Option[LocalDate],
> +  recurrenceEndDetails: Option[RecurrenceEndDetails],
> +  isCancelled: Boolean,
> +  isStopped: Boolean,
> +  updatedAt: ZonedDateTime,
> +)

## A3-0325 — TAA has four entities/two BQ copies; remove rebalance TAA entity and janitor remaining three

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [INV-1939] feat(rebalance): Add endpoint to sync rebalance plan state to readside (due to missed events)

**Source-preserving request, proposal, or question:**

> Yes. There are 4 entities having this TAA, only 2 have data in BQ. That’s why we didn’t add to the dashboard last time.
> 
> There are planned tasks to get rid of one useless entity \(TAA entity in rebalance\), and add janitor for the other 3 \(goal, rebalance, trading\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve four TAA entities, two in BQ, intended removal of rebalance TAA entity, janitors for goal/rebalance/trading.

**Evidence:** anon-2.jsonl:2150 · comment 421228601 · PR 6764 · 2023-08-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2150 · comment 421228601 · PR 6764 · 2023-08-22

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +  override def syncReadSideRebalancePlan(planId: UUID): Future[RebalancePlanDto] = {
> +    for {
> +      maybeRebalancePlan <- refProvider.getPlanRebalancerEntityRef(planId).ask(GetRebalancePlanCmd(_))
> +      result <- maybeRebalancePlan match {
> +        case Some(rebalancePlan) =>
> +          rebalancePlanJdbcRepository

## A3-0328 — BaseServiceLogicImpl.scala: Not that we don’t have index on customerId for this table. So let’s not call for too many customers at once when we call the sync in prod. We can add 

**Source stance:** requested-change

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala; PR: [NE-138] (performance) fee charge request removal

**Source-preserving request, proposal, or question:**

> Not that we don’t have index on customerId for this table. So let’s not call for too many customers at once when we call the sync in prod.
> 
> We can add the index in future \(and probably support querying by planId too\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2153 · comment 420893949 · PR 6756 · 2023-08-21

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2153 · comment 420893949 · PR 6756 · 2023-08-21

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/BaseServiceLogicImpl.scala`

**Explicit source context (hunk):**

> }
> +
> +  override def findFeeChargeRequests(customerId: UUID): Future[List[PlanFeeChargeRequestDto]] = {
> +    feeChargeRequestJdbcRepository.findByFilter(customerId = Some(customerId)).map(_.toList)
> +  }
>  }

## A3-0378 — SgInvestmentServiceImpl.scala: Better to just inject db directly into `investmentScheduleActivePeriodJdbcRepository` and the methods can return Future instead of DBIO

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala; PR: [ONB-2585] Add endpoint to retrieve missing recurring investments

**Source-preserving request, proposal, or question:**

> Better to just inject db directly into `investmentScheduleActivePeriodJdbcRepository` and the methods can return Future instead of DBIO

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2205 · comment 416502920 · PR 6619 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala`

**Evidence:** anon-2.jsonl:2205 · comment 416502920 · PR 6619 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/SgInvestmentServiceImpl.scala`

**Explicit source context (hunk):**

> val entityInspection: TypedEntityInspectionService,
>    val serviceLogic: ServiceLogic,
>    val localConfig: LocalConfig,
>    val system: ActorSystem,
> +  dateTimeProvider: DateTimeProvider,
> +  investmentScheduleActivePeriodJdbcRepository: InvestmentScheduleActivePeriodJdbcRepository
>  )(implicit val executionContext: ExecutionContext, val materializer: Materializer)

## A3-0381 — Future schedule startingDate PK collision across01Aug/05Aug/15Aug updates tolerated for CKAE

**Source stance:** explanation

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Since startingDate is in future at the point of schedule creation, it might not be unique enough
> 
> 1. 01Aug create monthly schedule on day 1, hence starting from 01Sep
> 2. 05Aug update monthly schedule to day 10, hence starting from 10Aug - row of \(1\) is now populated with endingDate = 05Aug
> 3. 15Aug update monthly schedule back to day 1, hence starting from 01Sep - we now update the row of \(1\) back to endingDate = None
> 
> 
> 
> This might be fine in context of the CKAE investigation task, but something to keep in mind. If we are fine with this \(as there won’t be any requestedDates populated for such scenario anyway\) and that we will remove this table once we are done with investigation, I guess it’s ok.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Preserve exact 01Aug/05Aug/15Aug changing monthly day1/day10/day1 timeline; duplicate startingDate PK reuse is tolerated only for temporary CKAE investigation without requestedDates.

**Evidence:** anon-2.jsonl:2208 · comment 416495706 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala`

> Since startingDate is in future at the point of schedule creation, it might not be unique enough
> 
> 1. 01Aug create monthly schedule on day 1, hence starting from 01Sep
> 2. 05Aug update monthly schedule to day 10, hence starting from 10Aug - row of \(1\) is now populated with endingDate = 05Aug
> 3. 15Aug update monthly schedule back to day 1, hence starting from 01Sep - we now update the row of \(1\) back to endingDate = None
> 
> ‌
> 
> This might be fine in context of the CKAE investigation task, but something to keep in mind. If we are fine with this \(as there won’t be any requestedDates populated for such scenario anyway\) and that we will remove this table once we are done with investigation, I guess it’s ok.
> 
> ‌

**Evidence:** anon-2.jsonl:2208 · comment 416495706 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala`

**Explicit source context (hunk):**

> +  def endingDate = column[Option[LocalDate]]("ending_date")
> +  def requestedDates = column[List[LocalDate]]("requested_dates")
> +
> +  def pk = primaryKey(InvestmentScheduleActivePeriodTable.PkName, (planId, startingDate))
> +  def idxCustomerId = index(s"${InvestmentScheduleActivePeriodTable.TableName}_customer_id_idx_v${InvestmentScheduleActivePeriodTable.DbVersion}", customerId, unique = false)
> +
> +  override def * : ProvenShape[InvestmentScheduleActivePeriod] =

## A3-0382 — InvestmentScheduleActivePeriodTable.scala: Can we prefix these timestamp field names with `plan_` to indicate they belong to plan level, not schedule level?

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Can we prefix these timestamp field names with `plan_` to indicate they belong to plan level, not schedule level?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2209 · comment 416495832 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala`

**Evidence:** anon-2.jsonl:2209 · comment 416495832 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala`

**Explicit source context (hunk):**

> +
> +  def ccy = column[CurrencyUnit]("ccy")
> +
> +  def planCreatedAt = column[Option[ZonedDateTime]]("plan_created_at")
> +  def planUpdatedAt = column[Option[ZonedDateTime]]("plan_updated_at")
> +
> +  // Recurring investment

## A3-0392 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Better to check if `recurringInvestmentSchedule` exists then upsert, then recurringAmount/Interval won’t be optional

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Better to check if `recurringInvestmentSchedule` exists then upsert, then recurringAmount/Interval won’t be optional

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2219 · comment 416500485 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2219 · comment 416500485 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +    for {
> +      _ <- investmentPlanFromEvt.recurringInvestmentSchedule match {
> +        case Some(_) =>
> +          investmentScheduleActivePeriodJdbcRepository.upsert(
> +            InvestmentScheduleActivePeriod(
> +              customerId = investmentPlanFromEvt.customerId,
> +              tradingAccountType = investmentPlanFromEvt.tradingAccountType,

## A3-0393 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Same for customerId/tradingAccountType/ccy. If we can remove them and join on planId instead, then we can make this projection much faster as it doesn

**Source stance:** suggestion

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Same for customerId/tradingAccountType/ccy. If we can remove them and join on planId instead, then we can make this projection much faster as it doesn’t need to fetch entity

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2220 · comment 416500676 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2220 · comment 416500676 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +              planUpdatedAt = investmentPlanFromEvt.updatedAt,
> +              recurringAmount = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.investmentAmount).get,
> +              recurringInterval = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.interval).get,
> +              startingDate = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.startingFrom).get,
> +              endingDate = None,
> +              requestedDates = List()
> +            )

## A3-0395 — InvestmentScheduleActivePeriodJdbcRepository.scala: I see that `deActivatedAt` is at plan level, but `markDeletionByPlanId` is called when schedule is removed, nothing to do with plan deactivation

**Source stance:** observed-defect

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodJdbcRepository.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> I see that `deActivatedAt` is at plan level, but `markDeletionByPlanId` is called when schedule is removed, nothing to do with plan deactivation

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2222 · comment 416501187 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodJdbcRepository.scala`

**Evidence:** anon-2.jsonl:2222 · comment 416501187 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodJdbcRepository.scala`

**Explicit source context (hunk):**

> +      maybeActiveInvestmentSchedule <- findActiveInvestmentSchedule(planId)
> +      _ <- maybeActiveInvestmentSchedule match {
> +        case Some(investmentSchedule) => upsert(investmentSchedule.copy(endingDate = Some(deletedAt.toLocalDate)))
> +        case None =>
> +          logger.error(s"InvestmentScheduleActivePeriodJdbcRepository unable to find active planId $planId to delete")
> +          Future.successful()
> +      }

## A3-0396 — InvestmentScheduleActivePeriodTable.scala: \(3\) will override \(1\) because they have same pk - but ok, we establish it’s ok in context of CKAE

**Source stance:** explanation

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Concern stated in the source:** \(3\) will override \(1\) because they have same pk - but ok, we establish it’s ok in context of CKAE

**Source-preserving request, proposal, or question:**

> \(3\) will override \(1\) because they have same pk - but ok, we establish it’s ok in context of CKAE

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2223 · comment 416506901 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala`

**Evidence:** anon-2.jsonl:2223 · comment 416506901 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodTable.scala`

**Explicit source context (hunk):**

> +  def endingDate = column[Option[LocalDate]]("ending_date")
> +  def requestedDates = column[List[LocalDate]]("requested_dates")
> +
> +  def pk = primaryKey(InvestmentScheduleActivePeriodTable.PkName, (planId, startingDate))
> +  def idxCustomerId = index(s"${InvestmentScheduleActivePeriodTable.TableName}_customer_id_idx_v${InvestmentScheduleActivePeriodTable.DbVersion}", customerId, unique = false)
> +
> +  override def * : ProvenShape[InvestmentScheduleActivePeriod] =

## A3-0397 — Declared customerId index is not created; use JdbcSchema index-adjustment helper

**Source stance:** observed-defect

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/db/JdbcSchema.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> This won’t create your customerId index. And I realize other tables have same bug too!
> 
> One good example is JdbcSchema in charge svc

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2224 · comment 416509216 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/db/JdbcSchema.scala`

**Evidence:** anon-2.jsonl:2224 · comment 416509216 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/db/JdbcSchema.scala`

**Explicit source context (hunk):**

> _ <- createTableIfNotExists(TableQuery[InvestmentPlanTable])
>          _ <- createTableIfNotExists(TableQuery[InvestmentRequestTable])
>          _ <- createTableIfNotExists(TableQuery[InvestmentPlanTableV3])
> +        _ <- createTableIfNotExists(TableQuery[InvestmentScheduleActivePeriodTable])
>        } yield ()
>      }
>    }

## A3-0398 — InvestmentScheduleActivePeriodJdbcEventProcessor.scala: Actually, here you should use the `recurringInvestmentSchedule` inside the investmentPlan of the event, instead of fetching latest from entity Also, i

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> Actually, here you should use the `recurringInvestmentSchedule` inside the investmentPlan of the event, instead of fetching latest from entity
> 
> Also, if we store plan level fields, you still fetch from entity for every `upsertSchedule` call

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2225 · comment 416509831 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2225 · comment 416509831 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/processors/sg/InvestmentScheduleActivePeriodJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +              planUpdatedAt = investmentPlanFromEvt.updatedAt,
> +              recurringAmount = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.investmentAmount).get,
> +              recurringInterval = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.interval).get,
> +              startingDate = investmentPlanFromEvt.recurringInvestmentSchedule.map(_.startingFrom).get,
> +              endingDate = None,
> +              requestedDates = List()
> +            )

## A3-0399 — InvestmentScheduleActivePeriodJdbcRepository.scala: You will need ``` sqlStatements( adjustCompositePkAndIndexIfNotExists( investmentSchedules, pkName = <pkName>, indexNames = List(<indexName>) ) ) ```

**Source stance:** requested-change

**Context:**

> investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodJdbcRepository.scala; PR: [ONB-2557] Add readside for recurring investment schedules with their active periods

**Source-preserving request, proposal, or question:**

> You will need
> 
> ```
> sqlStatements(
>   adjustCompositePkAndIndexIfNotExists(
>     investmentSchedules,
>     pkName = <pkName>,
>     indexNames = List(<indexName>)
>   )
> )
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2226 · comment 416513031 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodJdbcRepository.scala`

> You will need
> 
> ```
> sqlStatements(
>   adjustCompositePkAndIndexIfNotExists(
>     investmentSchedules,
>     pkName = <pkName>,
>     indexNames = List(<indexName>)
>   )
> )
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2226 · comment 416513031 · PR 6614 · 2023-08-03

Source path: `investment-impl/src/main/scala/com/endowus/silver/investment/impl/entities/plan/db/jdbc/InvestmentScheduleActivePeriodJdbcRepository.scala`

**Explicit source context (hunk):**

> +  }
> +}
> +
> +object InvestmentTransferScheduleActivePeriodJdbcRepository extends StrictLogging {
> +
> +  def createTable(implicit ec: ExecutionContext): DBIOAction[Unit, NoStream, Effect.Read with Effect.Schema] = {
> +    val investmentSchedule = TableQuery[InvestmentScheduleActivePeriodTable]

## A3-0425 — : I see we can improve the charge customer/plan query a bit more, e.g. currently for each customer, we query all plans to calculate fee, then again quer

**Source stance:** suggestion

**Context:**

> None; PR: [INV-1719] feat(charge)(trading): Minor logging and parallelism change

**Source-preserving request, proposal, or question:**

> I see we can improve the charge customer/plan query a bit more, e.g. currently for each customer, we query all plans to calculate fee, then again query relevant plans \(satisfying the filter\) to charge → should be able to reuse the result?
> 
> But decided not to change too much without proper thoughts and testing.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Fee-query reuse optimization is explicitly deferred pending thought and tests.

**Evidence:** anon-2.jsonl:2255 · comment 414427861 · PR 6557 · 2023-07-26

## A3-0435 — RebalanceRequestJdbcRepositoryImpl.scala: ``` filterOpt(planId)(_.planId === _) ``` Does this work?

**Source stance:** open-question

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala; PR: Feat/INV-1663 migrate to readside rebalance

**Source-preserving request, proposal, or question:**

> ```
> filterOpt(planId)(_.planId === _)
> ```
> 
> Does this work?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2265 · comment 412992702 · PR 6482 · 2023-07-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala`

**Evidence:** anon-2.jsonl:2265 · comment 412992702 · PR 6482 · 2023-07-20

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala`

**Explicit source context (hunk):**

> +            v.assetAllocationToUse.asColumnOf[JsValue].+>>("effectiveDate").asColumnOf[LocalDate] === target)
> +          .sortBy(_.createdAt)
> +          .result
> +      }
> +      .map(_.toList)
> +  }
> +

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

## A3-0441 — RebalanceRequestJdbcRepositoryImpl.scala: So we don’t filter for effectiveDate? Same for streamAll

**Source stance:** open-question

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala; PR: Feat/INV-1663 migrate to readside rebalance

**Source-preserving request, proposal, or question:**

> So we don’t filter for effectiveDate? Same for streamAll

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2272 · comment 413339168 · PR 6482 · 2023-07-21

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala`

**Evidence:** anon-2.jsonl:2272 · comment 413339168 · PR 6482 · 2023-07-21

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/entities/rebalancer/db/jdbc/RebalanceRequestJdbcRepositoryImpl.scala`

**Explicit source context (hunk):**

> +    planId: Option[UUID] = None,
> +    status: Option[RebalanceRequestStatus] = None,
> +    reason: Option[RebalanceReason] = None,
> +    effectiveDate: Option[LocalDate] = None
> +  ): Future[List[RebalanceRequestEntry]] = {
> +    database
> +      .run{

## A3-0454 — WithdrawalTopicSubscriber.scala: pk is \(customerId, transactionId\)… no other index I think it’s better to query using both customerId \+ goalId / customerId \+ planId

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala; PR: [INV-1425] feat(report): Added tax details to instrumentTransactionDto and refactor accessFeeTax statement calculation

**Source-preserving request, proposal, or question:**

> pk is \(customerId, transactionId\)… no other index
> 
> I think it’s better to query using both customerId \+ goalId / customerId \+ planId

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2287 · comment 407989819 · PR 6309 · 2023-07-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala`

## A3-0455 — WithdrawalTopicSubscriber.scala: Also, query by planId if exists would give fewer results, so let’s match that first

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala; PR: [INV-1425] feat(report): Added tax details to instrumentTransactionDto and refactor accessFeeTax statement calculation

**Source-preserving request, proposal, or question:**

> Also, query by planId if exists would give fewer results, so let’s match that first

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2288 · comment 407989870 · PR 6309 · 2023-07-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala`

## A3-0457 — WithdrawalTopicSubscriber.scala: Also maybe we extract `feeChargeRequestId` first… if not exist, then we can save the lookup

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala; PR: [INV-1425] feat(report): Added tax details to instrumentTransactionDto and refactor accessFeeTax statement calculation

**Source-preserving request, proposal, or question:**

> Also maybe we extract `feeChargeRequestId` first… if not exist, then we can save the lookup

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2290 · comment 407990152 · PR 6309 · 2023-07-03

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/WithdrawalTopicSubscriber.scala`

## A3-0463 — StatementDataGenerator.scala: We would need to remove the absorbed tax details at transaction level in this method `calculateIfSameStatementDataExists` to avoid reprinting old stat

**Source stance:** requested-change

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala; PR: [INV-1425] feat(report): Added tax details to instrumentTransactionDto and refactor accessFeeTax statement calculation

**Source-preserving request, proposal, or question:**

> We would need to remove the absorbed tax details at transaction level in this method `calculateIfSameStatementDataExists` to avoid reprinting old statement as well.
> 
> I’ll have a query to cross check the data we backfill matches the existing data in old statements.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2296 · comment 407994107 · PR 6309 · 2023-07-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Evidence:** anon-2.jsonl:2296 · comment 407994107 · PR 6309 · 2023-07-03

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/data/statementDataGenerator/StatementDataGenerator.scala`

**Explicit source context (hunk):**

> isReprint = maybeOldStatement.nonEmpty
>  
> -          sameStatementDataExists = calculateIfSameStatementDataExists(maybeOldStatement = maybeOldStatement, statementData = statementData)
> +          sameStatementDataExists = calculateIfSameStatementDataExists(maybeOldStatement = maybeOldStatement, statementData = statementData, startDateOfStatement)
>            statementInfo = StatementInfoDto(
>              statementPeriod = request.statementPeriod,
>              yearMonth = request.yearMonth,

## A3-0508 — FeeChargeRequestJdbcDbHandlerV3.scala: Can we change to use the utils in `ExtendedPostgresProfile` See example in advisory `TemplateJdbcDbHandler`

**Source stance:** requested-change

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcDbHandlerV3.scala; PR: Resolve INV-1688: Add new projection table with tax details.

**Source-preserving request, proposal, or question:**

> Can we change to use the utils in `ExtendedPostgresProfile`
> 
> See example in advisory `TemplateJdbcDbHandler`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2344 · comment 408154242 · PR 6342 · 2023-07-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcDbHandlerV3.scala`

**Evidence:** anon-2.jsonl:2344 · comment 408154242 · PR 6342 · 2023-07-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestJdbcDbHandlerV3.scala`

**Explicit source context (hunk):**

> +object FeeChargeRequestJdbcDbHandlerV3 {
> +  private val feeChargeRequests = TableQuery[FeeChargeRequestTableV3]
> +
> +  def createTable: FixedSqlAction[Unit, NoStream, Effect.Schema] = {
> +    sqlStatements(
> +      adjustCompositePkIfNotExists(
> +        feeChargeRequests,

## A3-0509 — FeeChargeRequestJdbcEventProcessorV5.scala: Hmm so we also update these planProfile too. I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcEventProcessorV5.scala; PR: Resolve INV-1688: Add new projection table with tax details.

**Concern stated in the source:** I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:

**Source-preserving request, proposal, or question:**

> Hmm so we also update these planProfile too. I guess it’s fine cuz this will look up latest planProfile, but still feel very expensive :sweat_smile:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2345 · comment 408154820 · PR 6342 · 2023-07-03

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/processors/jdbc/FeeChargeRequestJdbcEventProcessorV5.scala`

## A3-0510 — FeeChargeRequestTableV3.scala: typically pk name should be `tableName_pk` or `tableName_pkey`

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestTableV3.scala; PR: Resolve INV-1688: Add new projection table with tax details.

**Source-preserving request, proposal, or question:**

> typically pk name should be `tableName_pk` or `tableName_pkey`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2346 · comment 408306192 · PR 6342 · 2023-07-04

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestTableV3.scala`

**Evidence:** anon-2.jsonl:2346 · comment 408306192 · PR 6342 · 2023-07-04

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/entities/manager/db/feeCharge/jdbc/FeeChargeRequestTableV3.scala`

**Explicit source context (hunk):**

> +}
> +
> +object FeeChargeRequestTableV3 {
> +  private val dbVersion: Int = 3
> +  val schemaName = "charge"
> +  val tableName: String = "fee_charge_requests_v" + dbVersion
> +  val pkName: String = s"${tableName}_pk"

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

## A3-0615 — Slick cleanUp proposal preserves streaming and avoids running result twice

**Source stance:** open-question

**Context:**

> akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/SlickProjectionManager.scala; PR: TT-2311 Fix SlickProjectionManager#process to not execute transactions twice

**Source-preserving request, proposal, or question:**

> asTry scaladoc says
> 
> ```
> If possible, use andFinally or cleanUp instead, because those combinators, unlike asTry, support streaming.
> ```
> 
> 
> 
> would the below serve the same purpose? basically we just don’t want to trigger `result` again
> 
> ```
>       withMetrics(envelope, shardNo) { errorCounter =>
>         result.cleanUp(_.fold(DBIO.successful()) { _ =>
>           errorCounter()
>           DBIO.successful()
>         })
>       }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Slick asTry scaladoc specifically recommends andFinally/cleanUp for streaming; cleanUp proposal must not trigger result twice.

**Evidence:** anon-2.jsonl:2464 · comment 396743883 · PR 6045 · 2023-05-23

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/SlickProjectionManager.scala`

> asTry scaladoc says
> 
> ```
> If possible, use andFinally or cleanUp instead, because those combinators, unlike asTry, support streaming.
> ```
> 
> ‌
> 
> would the below serve the same purpose? basically we just don’t want to trigger `result` again
> 
> ```
>       withMetrics(envelope, shardNo) { errorCounter =>
>         result.cleanUp(_.fold(DBIO.successful()) { _ =>
>           errorCounter()
>           DBIO.successful()
>         })
>       }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2464 · comment 396743883 · PR 6045 · 2023-05-23

Source path: `akka-abstraction-layer/src/main/scala/com/endowus/silver/projection/SlickProjectionManager.scala`

**Explicit source context (hunk):**

> +      })
> +
> +      withMetrics(envelope, shardNo) { errorCounterFunc =>
> +        dbio.asTry.flatMap {
> +          case Failure(_) =>
> +            errorCounterFunc()
> +            DBIO.successful(Done)

## A3-0618 — AltsFeeManager.scala: I need an new version of planProfile table, but essentially the idea here is to compute for Alts plans only The `customerFeesCalculator: CustomerAltsF

**Source stance:** explanation

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/AltsFeeManager.scala; PR: [INV-1299] feat(charge): Support Atls Fee charge calculation & trigger

**Source-preserving request, proposal, or question:**

> I need an new version of planProfile table, but essentially the idea here is to compute for Alts plans only
> 
> The `customerFeesCalculator: CustomerAltsFeesCalculator` will make sure of that

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2467 · comment 394431556 · PR 5977 · 2023-05-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/AltsFeeManager.scala`

**Evidence:** anon-2.jsonl:2467 · comment 394431556 · PR 5977 · 2023-05-15

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/managers/AltsFeeManager.scala`

**Explicit source context (hunk):**

> +
> +    val chargeFut = fetchCustomers(maybeCustomerId, maybePlanId)
> +      .mapAsync(4) { customerId =>
> +        calculateFeeForCustomerId(
> +          customerId = customerId,
> +          periodStartDate = startDate,
> +          periodEndDate = endDate,

## A3-0639 — JdbcSchema.scala: We can’t drop until data team has moved

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/JdbcSchema.scala; PR: [INV-1438] feat(transaction): Listen to trading messages for asset_transfer

**Source-preserving request, proposal, or question:**

> We can’t drop until data team has moved

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2488 · comment 391965345 · PR 5918 · 2023-05-05

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/JdbcSchema.scala`

## A3-0660 — : We can run some mode query to check this one right?

**Source stance:** open-question

**Context:**

> None; PR: adds validations in goal and portfolio for ccy

**Source-preserving request, proposal, or question:**

> We can run some mode query to check this one right?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2510 · comment 389794090 · PR 5854 · 2023-04-26

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

## A3-0701 — RecommendedPortfolioChangePageLoader.scala: As discussed, this makes sense, but let’s implement this properly with a simple CRUD only table somewhere outside of gateway service.

**Source stance:** suggestion

**Context:**

> gateway-impl/src/main/scala/com/endowus/silver/gateway/impl/managers/bffs/RecommendedPortfolioChangePageLoader.scala; PR: [INV-1463] feat(gateway): Add hardcoded CMS Webflow ID mappings for RPC Flagship portfolios

**Source-preserving request, proposal, or question:**

> As discussed, this makes sense, but let’s implement this properly with a simple CRUD only table somewhere outside of gateway service.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2552 · comment 388288270 · PR 5766 · 2023-04-20

Source path: `gateway-impl/src/main/scala/com/endowus/silver/gateway/impl/managers/bffs/RecommendedPortfolioChangePageLoader.scala`

**Evidence:** anon-2.jsonl:2552 · comment 388288270 · PR 5766 · 2023-04-20

Source path: `gateway-impl/src/main/scala/com/endowus/silver/gateway/impl/managers/bffs/RecommendedPortfolioChangePageLoader.scala`

**Explicit source context (hunk):**

> utcCreatedAt = Some(v.createdAt.toInstant),
> -                        assetAllocationToUse = v.assetAllocationToUse
> +                        assetAllocationToUse = v.assetAllocationToUse,
> +                        cmsWebflowId = CmsWebflowIdMappings.get((v.assetAllocationToUse.portfolioId, v.assetAllocationToUse.effectiveDate))
>                      )
>                    )
>                  )

## A3-0712 — PlanTimeseriesTopicSubscriber.scala: How about ``` _ <- maybeLatestStoredMV match { case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) => logger.info("Skipping..

**Source stance:** suggestion

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> How about
> 
> ```
> _ <- maybeLatestStoredMV match {
>   case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) =>
>     logger.info("Skipping.....")
>     Future.successful(Done)
>   case _ =>
>     // upsert
> }
> ```

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2564 · comment 382583244 · PR 5603 · 2023-03-30

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

> How about
> 
> ```
> _ <- maybeLatestStoredMV match {
>   case Some(latestStoredMV) if latestStoredMV.updatedAt.isAfter(msg.updatedAt) =>
>     logger.info("Skipping.....")
>     Future.successful(Done)
>   case _ =>
>     // upsert
> }
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:2564 · comment 382583244 · PR 5603 · 2023-03-30

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> +        ) {
> +          for {
> +            rebalancePlan <- logger.logTime(s"Loading rebalance plan entity for planId ${msg.planId}") {
> +              refProvider.getPlanRebalancerEntityRef(msg.planId).ask(GetRebalancePlanCmd(_))
> +            }
> +            _ <- if (rebalancePlan.isEmpty) {
> +              logger.error(s"${UpdateMarketValueCmd.getClass.getName} is skipped for planId [${msg.planId}] because rebalancePlan is empty")

## A3-0716 — PlanTimeseriesTopicSubscriber.scala: Yup, just normal upserting projection data

**Source stance:** explanation

**Context:**

> rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> Yup, just normal upserting projection data

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2568 · comment 382944048 · PR 5603 · 2023-03-31

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2568 · comment 382944048 · PR 5603 · 2023-03-31

Source path: `rebalance-impl/src/main/scala/com/endowus/silver/rebalance/impl/subscribers/PlanTimeseriesTopicSubscriber.scala`

**Explicit source context (hunk):**

> +        logger.logTime(
> +          s"""[DIGEST-LOG] Process market value updated message for planId ${msg.planId}
> +             |for message in flight for ${ChronoUnit.MILLIS.between(msg.updatedAt, dateTimeProvider.now)}ms
> +             |and sent at ${msg.updatedAt}""".fuse
> +        ) {
> +          for {
> +            rebalancePlan <- logger.logTime(s"Loading rebalance plan entity for planId ${msg.planId}") {

## A3-0717 — MV projection upserts every latest message before rebalance checks; same-group migration

**Source stance:** requested-change

**Context:**

> None; PR: Feat/INV-1151 rebalance entity refactor phase 2 projections

**Source-preserving request, proposal, or question:**

> FYI  , let’s revisit this PR when you’re back. Absolutely no rush to do now.
> 
>  and me discussed. Key takeaways:
> 
> 1. The goal of this PR stays the same: build MV projection from timeseries `LatestPlanMarketValueUpdatedMsg` and any manual overridden via REST api
> 2. However, we need to change a little to keep the projection concern separated from the threshold rebalance concern
> 
>     1. In same subscriber, we should handle all `LatestPlanMarketValueUpdatedMsg`, do the timestamp checks and upsert all latest MV from timeseries
>     2. We should use a new DTO, e.g. MarketValueProjectionData to capture not only the MV but also a flag indicating whether confirmedMV and assumedMV are in sync \(logic of `isValidLatestPlanMarketValueUpdatedMsg`, useful for migration logic later\)
>     3. After upsert, retain the checks on `isValidLatestPlanMarketValueUpdatedMsg` and proceed if existing logic \(which we will migrate later\)
>     4. We can use same subscriber \(same consumer group\) to help with migration later. If different consumer group, we would need to double-release, one to turn off the old subscriber with logic, follow ed by another release to include logic in new subscriber.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- Preserve MV projection scope, timestamp-upsert of ALL messages, confirmed/assumed-sync flag, later rebalance checks, same-consumer-group migration versus two-release different-group rollout.

**Evidence:** anon-2.jsonl:2569 · comment 382951421 · PR 5603 · 2023-03-31

> FYI

**Evidence:** anon-2.jsonl:2569 · comment 382951421 · PR 5603 · 2023-03-31

> , let’s revisit this PR when you’re back. Absolutely no rush to do now.

**Evidence:** anon-2.jsonl:2569 · comment 382951421 · PR 5603 · 2023-03-31

> and me discussed. Key takeaways:
> 
> 1. The goal of this PR stays the same: build MV projection from timeseries `LatestPlanMarketValueUpdatedMsg` and any manual overridden via REST api
> 2. However, we need to change a little to keep the projection concern separated from the threshold rebalance concern
> 
>     1. In same subscriber, we should handle all `LatestPlanMarketValueUpdatedMsg`, do the timestamp checks and upsert all latest MV from timeseries
>     2. We should use a new DTO, e.g. MarketValueProjectionData to capture not only the MV but also a flag indicating whether confirmedMV and assumedMV are in sync \(logic of `isValidLatestPlanMarketValueUpdatedMsg`, useful for migration logic later\)
>     3. After upsert, retain the checks on `isValidLatestPlanMarketValueUpdatedMsg` and proceed if existing logic \(which we will migrate later\)
>     4. We can use same subscriber \(same consumer group\) to help with migration later. If different consumer group, we would need to double-release, one to turn off the old subscriber with logic, follow ed by another release to include logic in new subscriber.
>     
> 
> ‌

## A3-0764 — TransactionFxConverter.scala: Can we change the logging to be clearer that “no fx rate found for ccypair \+ date”. Asking marketdata svc is fine, but more important is we need to f

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala; PR: Feat/INV-913 tech debt fx rates

**Concern stated in the source:** I think it’s ok error here, so that someone can check.

**Source-preserving request, proposal, or question:**

> Can we change the logging to be clearer that “no fx rate found for ccypair \+ date”. Asking marketdata svc is fine, but more important is we need to fix the projection table, if indeed its data is missing.
> 
> I think it’s ok error here, so that someone can check. Outcome is either the transaction has wonky dates or data is missing \(which we can trigger the sync with marketdata\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2617 · comment 370779668 · PR 5266 · 2023-02-17

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

## A3-0767 — Auto FX sync tradeoff: stale fallback cached for a day versus repeated missing-rate sync

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> In case of missing date,
> 
> 1. if we call sync and put the fallback rate here, if the rate was indeed missing, and corrected after sync - we will continue to use the fallback rate for another day
> 2. if we don’t put the fallback rate, and if the rate cannot be found even if after sync call - we will keep calling sync over and over again
> 
> 
> 
> I’m not sure if we want to automatically sync without a human looking into it yet…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Fallback cached after sync may stay stale for another day; not caching can cause endless repeated sync if still absent. Automatic sync remains unresolved pending human inspection.

**Evidence:** anon-2.jsonl:2620 · comment 371373270 · PR 5266 · 2023-02-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

> In case of missing date,
> 
> 1. if we call sync and put the fallback rate here, if the rate was indeed missing, and corrected after sync - we will continue to use the fallback rate for another day
> 2. if we don’t put the fallback rate, and if the rate cannot be found even if after sync call - we will keep calling sync over and over again
> 
> ‌
> 
> I’m not sure if we want to automatically sync without a human looking into it yet…
> 
> ‌

**Evidence:** anon-2.jsonl:2620 · comment 371373270 · PR 5266 · 2023-02-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +  }
> +
> +  def completeAndFillFxRates(
> +    rates: Map[LocalDate, FxRateProjectionData]
> +  ): Map[LocalDate, CurrencyRate] = {
> +    if (rates.isEmpty) {
> +      throw new TransactionSvcException(

## A3-0770 — FX cache T-10 historical lookup can become wrong fallback for missingT rate

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> And is this logic flawed in this case:
> 
> * current date = T
> * rate for date T-10 is queried \(for example, for one of the past transactions\)
> 
>     * rate is not available in cache
>     * rate is fetched by exact date from repository
>     * rate is written to cache and returned for usage
>     
> * rate for date T is queried, however data is not available yet
> 
>     * rate is not available in cache
>     * rate is also not available in repository
>     * we ask for back dated rate from cache, and now rate for date T-10 is returned?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Keep T-10 exact historical-rate cached before missing-T query and incorrect fallback risk as a concrete unresolved scenario.

**Evidence:** anon-2.jsonl:2624 · comment 377401170 · PR 5266 · 2023-03-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

> And is this logic flawed in this case:
> 
> * current date = T
> * rate for date T-10 is queried \(for example, for one of the past transactions\)
> 
>     * rate is not available in cache
>     * rate is fetched by exact date from repository
>     * rate is written to cache and returned for usage
>     
> * rate for date T is queried, however data is not available yet
> 
>     * rate is not available in cache
>     * rate is also not available in repository
>     * we ask for back dated rate from cache, and now rate for date T-10 is returned?
>     
> 
> ‌

**Evidence:** anon-2.jsonl:2624 · comment 377401170 · PR 5266 · 2023-03-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +
> +  private def loadFxRates(baseCcy: CurrencyUnit, quoteCcy: CurrencyUnit) = {
> +    logger.logTime(s"Loading fx rates for baseCcy [$baseCcy] to quoteCcy [$quoteCcy] from source") {
> +      for {
> +        projectionRates <- fxRatesProjectionRepository.findFxRatesAfter(baseCcy, quoteCcy, timeService.localDateNow.minusYears(maxLookBackStoredInCache))
> +        patchedRatesMap = completeAndFillFxRates(
> +          projectionRates.map(s => (s.priceDate, s)).toMap

## A3-0771 — FxRateHelper.scala: Why do `we only care about month anyway` ? Current usage of transactions in A&B and monthly statement, we would always need to load all transactions s

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> Why do `we only care about month anyway` ? Current usage of transactions in A&B and monthly statement, we would always need to load all transactions since customer’s inception date

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2625 · comment 377402242 · PR 5266 · 2023-03-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Evidence:** anon-2.jsonl:2625 · comment 377402242 · PR 5266 · 2023-03-13

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +)(implicit ec: ExecutionContext) extends StrictLogging {
> +
> +  private val fxRateCache: AsyncLoadingCache[CurrencyPair, CurrencyPairFxCache] =
> +    Scaffeine()
> +      .recordStats()
> +      .expireAfterWrite(4.hours)
> +      .maximumSize(20)

## A3-0772 — TransactionFxConverter.scala: distinct the pairs before loading?

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> Let’s distinct the pairs before loading?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2626 · comment 377730008 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Evidence:** anon-2.jsonl:2626 · comment 377730008 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/utils/TransactionFxConverter.scala`

**Explicit source context (hunk):**

> +    toCcy: CurrencyUnit
> +  ): Future[List[TransactionDto]] = {
> +    logger.logTime(s"fxConvertTransactions for ${transactions.size}") {
> +      Source(transactions)
> +        .mapAsync(2) { transaction =>
> +          transaction.transactionType match {
> +            case TransactionType.FX_CONVERSION => applyDisplayAmountForFxSettlementDetails(transaction, toCcy)

## A3-0776 — FxRateHelper.scala: create a TreeMap keyed by priceDate first, then just lookup here? Otherwise we traverse the Seq everytime

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Concern stated in the source:** Otherwise we traverse the Seq everytime

**Source-preserving request, proposal, or question:**

> Maybe create a TreeMap keyed by priceDate first, then just lookup here? Otherwise we traverse the Seq everytime

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2630 · comment 377731048 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Evidence:** anon-2.jsonl:2630 · comment 377731048 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +      _ = fxRateCache.synchronous.invalidateAll()
> +    } yield projectionData
> +  }
> +
> +}
> +
> +object FxRateHelper {

## A3-0777 — FxRateHelper.scala: So if latest rate is requested when data is not available yet, we always reload from DB and fallback to near date. Is this intended so that we will ha

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Concern stated in the source:** Is this intended so that we will have latest data when it’s ready?

**Source-preserving request, proposal, or question:**

> So if latest rate is requested when data is not available yet, we always reload from DB and fallback to near date. Is this intended so that we will have latest data when it’s ready?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2631 · comment 377731612 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Evidence:** anon-2.jsonl:2631 · comment 377731612 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +  ): Map[LocalDate, CurrencyRate] = {
> +    if (rates.isEmpty) {
> +      throw new TransactionSvcException(
> +        s"Rates taken from db are empty! cannot refresh cache!", NO_FX_RATES_AVAILABLE
> +      )
> +    } else {
> +      val firstFxDate = rates.minBy(_._1)._1

## A3-0778 — FxRateHelper.scala: I mean we just need `loadCacheWithFxRates`, no need to `loadCacheAndFind` In fact, using latest date here means we will always load before 3pm everyda

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> I mean we just need `loadCacheWithFxRates`, no need to `loadCacheAndFind`
> 
> In fact, using latest date here means we will always load before 3pm everyday. Maybe we just need to check if cache contains any rates for the pair?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2633 · comment 377732817 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Evidence:** anon-2.jsonl:2633 · comment 377732817 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +            new CurrencyPairFxCache(ccyPair, fxRateMap, fxRatesProjectionRepository)
> +          })
> +      }}
> +
> +  def getFxRate(fxId: FxRateId): Future[(LocalDate, BigDecimal)] = {
> +    if (fxId.baseCcy == fxId.quoteCcy) {
> +      Future.successful((timeService.localDateNow, BigDecimal(1)))

## A3-0779 — FxRateHelper.scala: Exactly my comment here [<url> data-inline-card='' } We don’t put if latest rate is not available

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Source-preserving request, proposal, or question:**

> Exactly my comment here [<url> data-inline-card='' } 
> 
> We don’t put if latest rate is not available

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2634 · comment 377738443 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Evidence:** anon-2.jsonl:2634 · comment 377738443 · PR 5266 · 2023-03-14

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +            new CurrencyPairFxCache(ccyPair, fxRateMap, fxRatesProjectionRepository)
> +          })
> +      }}
> +
> +  def getFxRate(fxId: FxRateId): Future[(LocalDate, BigDecimal)] = {
> +    if (fxId.baseCcy == fxId.quoteCcy) {
> +      Future.successful((timeService.localDateNow, BigDecimal(1)))

## A3-0781 — FxRateHelper.scala: Should we invalidate the cache after this sync so that we reload fresh rate?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala; PR: Feat/INV-913 tech debt fx rates

**Concern stated in the source:** Should we invalidate the cache after this sync so that we reload fresh rate?

**Source-preserving request, proposal, or question:**

> Should we invalidate the cache after this sync so that we reload fresh rate?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2636 · comment 379646566 · PR 5266 · 2023-03-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Evidence:** anon-2.jsonl:2636 · comment 379646566 · PR 5266 · 2023-03-20

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/helper/FxRateHelper.scala`

**Explicit source context (hunk):**

> +    }
> +  }
> +
> +  def syncFxRatesWithMarketData(baseCcy: CurrencyUnit, quoteCcy: CurrencyUnit): Future[List[FxRateProjectionData]] = {
> +    for {
> +      marketDataRates <- marketDataService.getFxRates(baseCcy.toString, quoteCcy.toString).invoke()
> +      projectionData = marketDataRates.map(rate => FxRateProjectionData(

## A3-0861 — DividendService.scala: Indeed. I kept the API in AdminService intact, and changed it to use the pagination endpoint instead.

**Source stance:** explanation

**Context:**

> dividend-api/src/main/scala/com/endowus/silver/dividend/api/DividendService.scala; PR: [INV-1179] feat(dividend)(admin): Remove usage of Cassandra readside dividendPlanDistributionRecordsTable

**Source-preserving request, proposal, or question:**

> Indeed. I kept the API in AdminService intact, and changed it to use the pagination endpoint instead.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2719 · comment 371573629 · PR 5297 · 2023-02-21

Source path: `dividend-api/src/main/scala/com/endowus/silver/dividend/api/DividendService.scala`

**Evidence:** anon-2.jsonl:2719 · comment 371573629 · PR 5297 · 2023-02-21

Source path: `dividend-api/src/main/scala/com/endowus/silver/dividend/api/DividendService.scala`

**Explicit source context (hunk):**

> -  ): ServiceCall[NotUsed, List[DividendPlanDistributionRecord]]
> -
>    // Paginated
>    def paginateDividendPlanDistributionRecords: ServiceCall[NotUsed, PaginateResponse[DividendPlanDistributionRecord]]
>    def internalPaginateDividendPlanDistributionRecords: ServiceCall[PaginateRequest, PaginateResponse[DividendPlanDistributionRecord]]

## A3-0864 — SgServiceLogicImpl.scala: Ah this is just to compare between charge entity and charge readside? I think we can skip this, cuz we will anyhow fetch from entity and write again -

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala; PR: [SILVER-14633] feat(charge): Refactor sync with redemption to account states

**Concern stated in the source:** I think we can skip this, cuz we will anyhow fetch from entity and write again - which should upsert in readside

**Source-preserving request, proposal, or question:**

> Ah this is just to compare between charge entity and charge readside? I think we can skip this, cuz we will anyhow fetch from entity and write again - which should upsert in readside

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2722 · comment 371634458 · PR 5309 · 2023-02-21

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/logic/service/impl/SgServiceLogicImpl.scala`

## A3-0880 — FxRatesProjectionRepository.scala: If no streaming, then don’t need SlickSession I think

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/FxRatesProjectionRepository.scala; PR: Feat/INV-913 fx rates projection

**Source-preserving request, proposal, or question:**

> If no streaming, then don’t need SlickSession I think

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2739 · comment 354168399 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/FxRatesProjectionRepository.scala`

**Evidence:** anon-2.jsonl:2739 · comment 354168399 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/FxRatesProjectionRepository.scala`

**Explicit source context (hunk):**

> +
> +class FxRatesProjectionRepository (database: Database)(implicit ctx: ExecutionContext) {
> +
> +  private val fxRatesProjectionTable = TableQuery[FxRatesProjectionTable]
> +
> +  def findCcyPairRateByPriceDate(baseCcy: CurrencyUnit, quoteCcy: CurrencyUnit, priceDate: LocalDate): Future[Option[FxRateProjectionData]] = {
> +    database.run {

## A3-0882 — FxRatesTopicSubscriberV2.scala: We are writing to DB only, so I think we can just dump as in \(stay true to projection\). I think we have this logic last time because it was via enti

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala; PR: Feat/INV-913 fx rates projection

**Concern stated in the source:** I think we have this logic last time because it was via entity, we don’t want to spam events.

**Source-preserving request, proposal, or question:**

> We are writing to DB only, so I think we can just dump as in \(stay true to projection\). I think we have this logic last time because it was via entity, we don’t want to spam events.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2741 · comment 354168870 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2741 · comment 354168870 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +    .fxRatesMarketDataTopic
> +    .subscribe
> +    .withGroupId(FxRatesProjection)
> +    .atLeastOnce(Flow[FxRatesMsg].mapAsync(parallelism = 1) {
> +
> +    case msg: FxRateUpdatedMsg =>
> +      fxRatesProjectionJdbcDbHandler.upsert(FxRateProjectionData(

## A3-0883 — FxRatesTopicSubscriberV2.scala: This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the 

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala; PR: Feat/INV-913 fx rates projection

**Source-preserving request, proposal, or question:**

> This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the result of the upsert, if it succeeds”

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2742 · comment 354168987 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

> This the upsert call fails, the whole future will still error, and the subscriber will retry. The `.map(_ => Done)` purely means “we are ignoring the result of the upsert, if it succeeds”
> 
> ‌

**Evidence:** anon-2.jsonl:2742 · comment 354168987 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +    .atLeastOnce(Flow[FxRatesMsg].mapAsync(parallelism = 1) {
> +
> +    case msg: FxRateUpdatedMsg =>
> +      fxRatesProjectionJdbcDbHandler.upsert(FxRateProjectionData(
> +        baseCcy = msg.baseCcy, quoteCcy = msg.quoteCcy, priceDate = msg.priceDate, rate = msg.fxRate
> +      )).map(_ => Done)
> +

## A3-0884 — FxRatesTopicSubscriberV2.scala: Slick support bulk upsert too

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala; PR: Feat/INV-913 fx rates projection

**Source-preserving request, proposal, or question:**

> Slick support bulk upsert too

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2743 · comment 354169083 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

**Evidence:** anon-2.jsonl:2743 · comment 354169083 · PR 4915 · 2022-12-16

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/subscribers/FxRatesTopicSubscriberV2.scala`

**Explicit source context (hunk):**

> +      fxRatesProjectionJdbcDbHandler.bulkUpsert(
> +        msg.fxRates.map(rates => {
> +          FxRateProjectionData(baseCcy = msg.baseCcy, quoteCcy = msg.quoteCcy, priceDate = rates._1, rate = rates._2)
> +        })
> +      ).map(_ => Done)
> +
> +    case _ =>

## A3-0886 — AdvisoryApplication.scala: Don’t we need subscriber to customer/onboarding topic to populate the `customerProjectionDataJdbcRepository`?

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Don’t we need subscriber to customer/onboarding topic to populate the `customerProjectionDataJdbcRepository`?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2745 · comment 365574347 · PR 5109 · 2023-01-31

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Evidence:** anon-2.jsonl:2745 · comment 365574347 · PR 5109 · 2023-01-31

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/AdvisoryApplication.scala`

**Explicit source context (hunk):**

> +  lazy val craExpiryDailyTriggerTopicProducerDirect: CRAExpiryDailyTriggerTopicProducerDirect = wire[CRAExpiryDailyTriggerTopicProducerDirect]
> +  lazy val vcStateChangeDailyTriggerTopicProducerDirect: VCStateChangeDailyTriggerTopicProducerDirect = wire[VCStateChangeDailyTriggerTopicProducerDirect]
> +  createCustomTopics().map(_ => for {
> +    //TODO(nate) Find better way to wire this subscribers...
> +    _ <- Future.unit
> +    _ = wire[CRAExpiryDailyTriggerTopicSubscriber]
> +    _ = wire[VCStateChangeDailyTriggerTopicSubscriber]

## A3-0894 — CustomerProjectionDataJdbcRepository.scala: If this gets expensive, we should consider adding another readside table for advisory profile containing only the latest entry

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> If this gets expensive, we should consider adding another readside table for advisory profile containing only the latest entry

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2753 · comment 366320781 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala`

**Evidence:** anon-2.jsonl:2753 · comment 366320781 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala`

**Explicit source context (hunk):**

> +  def findNonVCWithMaybeAdvisoryProfile(bornUpTo: LocalDate): Source[(CustomerProjectionData, Option[CustomerAdvisoryProfileData]), NotUsed] = {
> +    Slick.source(
> +      customerData
> +        .joinLeft(customerAdvisorProfiles)
> +        .on((customerData, customerAdvisoryProfile) => {
> +          customerData.customerId === customerAdvisoryProfile.customerId
> +        })

## A3-0895 — CustomerAdvisoryProfileJdbcRepository.scala: Hmm alright, maybe another readside table containing only latest is worth it :grimacing:

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileJdbcRepository.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Hmm alright, maybe another readside table containing only latest is worth it :grimacing:

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2754 · comment 366321122 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileJdbcRepository.scala`

## A3-0896 — CustomerAdvisoryProfileJdbcRepository.scala: And in that new table, we can consider extract this field as an optional column, to make query simpler

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileJdbcRepository.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> And in that new table, we can consider extract this field as an optional column, to make query simpler

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.

**Evidence:** anon-2.jsonl:2755 · comment 366321253 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileJdbcRepository.scala`

## A3-0899 — HkServiceLogicImpl.scala: add batchUpsert?

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Let’s add batchUpsert?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2758 · comment 366321805 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2758 · comment 366321805 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +                    ))
> +                )
> +              })
> +          } yield customerProjectionData
> +          res recoverWith {
> +            case ex =>
> +              logger.error(s"failed to customerProjectionDataSync of customer ID [${customer.customerId}]", ex)

## A3-0909 — CraManager.scala: Ok customer projection table will have data from onboarding entity, just no sync endpoint… So the sync needs to check customer status somehow

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Ok customer projection table will have data from onboarding entity, just no sync endpoint… So the sync needs to check customer status somehow

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2768 · comment 366325780 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:2768 · comment 366325780 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        case (totalCustomers, _) =>
> +        totalCustomers + 1
> +      }
> +      .map { totalCustomers =>
> +        logger.info(
> +          s"""
> +             |[DIGEST-LOG] Ran VC re-assessment for execute date $executeDate,

## A3-0910 — CustomerProjectionDataJdbcRepository.scala: findCustomerWithNonVcProfile\(bornBeforeDate: LocalDate\)

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> findCustomerWithNonVcProfile\(bornBeforeDate: LocalDate\)

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2769 · comment 366326170 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala`

**Evidence:** anon-2.jsonl:2769 · comment 366326170 · PR 5109 · 2023-02-02

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/customer/CustomerProjectionDataJdbcRepository.scala`

**Explicit source context (hunk):**

> +    )
> +  }
> +
> +  def findNonVCWithMaybeAdvisoryProfile(bornUpTo: LocalDate): Source[(CustomerProjectionData, Option[CustomerAdvisoryProfileData]), NotUsed] = {
> +    Slick.source(
> +      customerData
> +        .joinLeft(customerAdvisorProfiles)

## A3-0912 — CustomerAdvisoryProfileSnapshotJdbcRepository.scala: should be “with expiry before” right? how about `streamNonVcProfile(expiringBefore: LocalDate)`

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcRepository.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> should be “with expiry before” right? how about `streamNonVcProfile(expiringBefore: LocalDate)`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2771 · comment 367130653 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcRepository.scala`

**Evidence:** anon-2.jsonl:2771 · comment 367130653 · PR 5109 · 2023-02-06

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/jdbc/hk/profile/CustomerAdvisoryProfileSnapshotJdbcRepository.scala`

**Explicit source context (hunk):**

> +    }
> +  }
> +
> +  def streamValidNonVcProfile(expiringUpTo: LocalDate): Source[CustomerAdvisoryProfileData, NotUsed] = {
> +    Slick.source(
> +      customerAdvisoryProfiles
> +        .filter(s =>

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

## A3-0931 — HkServiceLogicImpl.scala: Oh bulk upsert for whole set of customers would be too large… either batch the source, or just upsert one by one I think…

**Source stance:** suggestion

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> Oh bulk upsert for whole set of customers would be too large… either batch the source, or just upsert one by one I think…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2790 · comment 367471398 · PR 5109 · 2023-02-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2790 · comment 367471398 · PR 5109 · 2023-02-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +              Future.successful(None)
> +          }
> +      }
> +      .grouped(10)
> +      .map(customers => customerProjectionDataJdbcDbHandler.bulkUpsert(customers.flatten))
> +      .runWith(Sink.ignore)
> +      .onComplete({

## A3-0932 — HkServiceLogicImpl.scala: I didn’t realize getPaginatedSource already concat all the page previously..

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala; PR: Feat/INV-969 auto change VC

**Source-preserving request, proposal, or question:**

> I didn’t realize getPaginatedSource already concat all the page previously..

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2791 · comment 367471585 · PR 5109 · 2023-02-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2791 · comment 367471585 · PR 5109 · 2023-02-07

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/logic/service/HkServiceLogicImpl.scala`

**Explicit source context (hunk):**

> +              Future.successful(None)
> +          }
> +      }
> +      .grouped(10)
> +      .map(customers => customerProjectionDataJdbcDbHandler.bulkUpsert(customers.flatten))
> +      .runWith(Sink.ignore)
> +      .onComplete({

## A3-0938 — DividendApplication.scala: The lags are tracked based on offsets only. So if offset table is not created, nothing will work…

**Source stance:** explanation

**Context:**

> dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendApplication.scala; PR: [INV-1096] feat(dividend)(admin,broker,communication,investment,timeseries,trading,transaction): Region split for Dividend svc

**Source-preserving request, proposal, or question:**

> The lags are tracked based on offsets only. So if offset table is not created, nothing will work…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2798 · comment 366690569 · PR 5136 · 2023-02-03

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendApplication.scala`

**Evidence:** anon-2.jsonl:2798 · comment 366690569 · PR 5136 · 2023-02-03

Source path: `dividend-impl/src/main/scala/com/endowus/silver/dividend/impl/DividendApplication.scala`

**Explicit source context (hunk):**

> readSide.register(wire[BrokerAccountDividendCommunicationV2EventProcessor])
> -  readSide.register(wire[DividendCommunicationV2EventProcessor])
> +
> +  // register jdbc event processor only after offsets are created
> +  runCreateOffsetStore()
> +    .recover({
> +      case ex: AskTimeoutException =>

## A3-0974 — TransactionJdbcRepositoryV2Test.scala: Good idea to truncate the table at the end. Save yourself some head scratching when you add the next test

**Source stance:** suggestion

**Context:**

> transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2Test.scala; PR: [EN-674] feat(transaction) create an api to get transactions for a customer id with goal id and statuses filter

**Source-preserving request, proposal, or question:**

> Good idea to truncate the table at the end. Save yourself some head scratching when you add the next test

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2834 · comment 357770225 · PR 5028 · 2023-01-05

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2Test.scala`

**Evidence:** anon-2.jsonl:2834 · comment 357770225 · PR 5028 · 2023-01-05

Source path: `transaction-impl/src/test/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2Test.scala`

**Explicit source context (hunk):**

> +            )
> +          )
> +        _ <- db.run(truncateTable(TransactionTableV2.tableName))
> +      } yield {
> +        result1.size shouldBe 1
> +        result2.size shouldBe 1
> +        result3.size shouldBe 0

## A3-0978 — ServiceLogicImpl.scala: this existing endpoint is already a hot mess with various conditional check - they are not intuitive API for consumer at all. How about we add new end

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala; PR: [EN-674] feat(transaction) add transactionStatuses param in api query-transactions

**Source-preserving request, proposal, or question:**

> I think this existing endpoint is already a hot mess with various conditional check - they are not intuitive API for consumer at all.
> 
> How about we add new endpoint, something like this
> 
> ```
> /transactions/:customerId/:goalId?statuses
> ```
> 
> Then it is clearer for consumer what exactly being filter on? I would argue existing endpoint should also be split into multiple ones in this manner

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2838 · comment 357471316 · PR 4952 · 2023-01-04

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala`

**Evidence:** anon-2.jsonl:2838 · comment 357471316 · PR 4952 · 2023-01-04

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/logic/service/impl/ServiceLogicImpl.scala`

**Explicit source context (hunk):**

> -    lazy val retrieveFromDbFut = (customerId, accountType, goalId, planId) match {
> -      case (_, _, _, Some(actualPlanId)) =>
> +    lazy val retrieveFromDbFut = (customerId, accountType, goalId, planId, transactionStatuses) match {
> +      case (_, _, _, Some(actualPlanId), _) =>
>          transactionJdbcRepository.findByPlanId(actualPlanId)
>            .map(txs => txs.map(Transaction.toDto))

## A3-0979 — TransactionJdbcRepositoryV2.scala: we can all agree that having a single find\(\) method with various \(optional\) filters is better? If we do not want to change existing code, let’s ad

**Source stance:** suggestion

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala; PR: [EN-674] feat(transaction) add transactionStatuses param in api query-transactions

**Source-preserving request, proposal, or question:**

> I think we can all agree that having a single find\(\) method with various \(optional\) filters is better? If we do not want to change existing code, let’s add new method in this repository, and use it to implement the new endpoint. And mark existing find methods as deprecated, and we clean them up separately

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2839 · comment 357471469 · PR 4952 · 2023-01-04

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala`

**Evidence:** anon-2.jsonl:2839 · comment 357471469 · PR 4952 · 2023-01-04

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala`

**Explicit source context (hunk):**

> }
>    }
>  
> +  def findByCustomerIdGoalIdAndStatuses(customerId: UUID, goalId: UUID, statuses: Set[TransactionStatus]): Future[Seq[Transaction]] = {
> +    database.run {
> +      transactions
> +        .filter(_.customerId === customerId)

## A3-0980 — TransactionJdbcRepositoryV2.scala: You can see example for find method accepting list of filters at `com.endowus.silver.portfolio.impl.entities.portfolio.db.jdbc.PortfolioRepository`

**Source stance:** explanation

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala; PR: [EN-674] feat(transaction) add transactionStatuses param in api query-transactions

**Source-preserving request, proposal, or question:**

> You can see example for find method accepting list of filters at `com.endowus.silver.portfolio.impl.entities.portfolio.db.jdbc.PortfolioRepository`

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2840 · comment 357471588 · PR 4952 · 2023-01-04

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala`

**Evidence:** anon-2.jsonl:2840 · comment 357471588 · PR 4952 · 2023-01-04

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala`

**Explicit source context (hunk):**

> }
>    }
>  
> +  def findByCustomerIdGoalIdAndStatuses(customerId: UUID, goalId: UUID, statuses: Set[TransactionStatus]): Future[Seq[Transaction]] = {
> +    database.run {
> +      transactions
> +        .filter(_.customerId === customerId)

## A3-0997 — CorporateProfileJdbcEventProcessor.scala: We only need to call create tables once, either here or when wiring DbHandler in Application

**Source stance:** requested-change

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/corporate/CorporateProfileJdbcEventProcessor.scala; PR: advisory service to have customer profile jdbc db

**Source-preserving request, proposal, or question:**

> We only need to call create tables once, either here or when wiring DbHandler in Application

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2858 · comment 353302286 · PR 4907 · 2022-12-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/corporate/CorporateProfileJdbcEventProcessor.scala`

**Evidence:** anon-2.jsonl:2858 · comment 353302286 · PR 4907 · 2022-12-13

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/corporate/CorporateProfileJdbcEventProcessor.scala`

**Explicit source context (hunk):**

> +  override def buildHandler(): ReadSideProcessor.ReadSideHandler[CorporateProfileEvt] =
> +    readSide
> +      .builder[CorporateProfileEvt](READ_SIDE_ID)
> +      .setGlobalPrepare(createTables)
> +      .setFutureEventHandler[CorporateProfileCreatedEvt](ele => handleCorporateProfileCreatedEvt(ele.entityId, ele.event))
> +      .setFutureEventHandler[CorporateProfileUpdatedEvt](ele => handleCorporateProfileUpdatedEvt(ele.entityId, ele.event))
> +      .build()

## A3-1032 — InvestmentRequestProjectionJdbcDbHandler.scala: add repository and move the query there

**Source stance:** requested-change

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/database/investment/InvestmentRequestProjectionJdbcDbHandler.scala; PR: Feat/INV-676 cancel investment vc expired

**Source-preserving request, proposal, or question:**

> Let’s add repository and move the query there

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- No hunk is available for this short source statement; its exact target may remain unresolved beyond the component/PR context.

**Evidence:** anon-2.jsonl:2896 · comment 349397855 · PR 4789 · 2022-11-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/database/investment/InvestmentRequestProjectionJdbcDbHandler.scala`

## A3-1035 — HkInvestmentTopicSubscriber.scala: Then we can upsert always… don’t need another update method

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala; PR: Feat/INV-676 cancel investment vc expired

**Source-preserving request, proposal, or question:**

> Then we can upsert always… don’t need another update method

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2899 · comment 349491434 · PR 4789 · 2022-11-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala`

**Evidence:** anon-2.jsonl:2899 · comment 349491434 · PR 4789 · 2022-11-29

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/subscribers/hk/HkInvestmentTopicSubscriber.scala`

**Explicit source context (hunk):**

> +          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request, Some(msg.request.createdAt))
>          case msg: InvestmentRequestOrdersGeneratedMsg =>
> -          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request)
> +          upsertInvestmentRequest(msg.customerId)(msg.goalId, msg.planId, msg.request, Some(msg.request.orders
> +            .map(_.createdAt)
> +            .maxBy(_.toInstant)
> +          ))

## A3-1038 — InvestmentRequestProjectionTable.scala: Can we name the table column matching field name? either updatedAt or lastUpdatedTS

**Source stance:** open-question

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/database/investment/InvestmentRequestProjectionTable.scala; PR: Feat/INV-676 cancel investment vc expired

**Source-preserving request, proposal, or question:**

> Can we name the table column matching field name? either updatedAt or lastUpdatedTS

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:2902 · comment 350104049 · PR 4789 · 2022-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/database/investment/InvestmentRequestProjectionTable.scala`

**Evidence:** anon-2.jsonl:2902 · comment 350104049 · PR 4789 · 2022-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/database/investment/InvestmentRequestProjectionTable.scala`

**Explicit source context (hunk):**

> def status = column[InvestmentRequestStatus]("status")
> -
> -  //TODO @

**Evidence:** anon-2.jsonl:2902 · comment 350104049 · PR 4789 · 2022-12-01

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/cr/database/investment/InvestmentRequestProjectionTable.scala`

**Explicit source context (hunk):**

> for INV-676 timestamp column for idempotence check
> +  def updatedAt = column[Instant]("updated_at")
>  
>    def pk = primaryKey(InvestmentRequestProjectionTable.PrimaryKeyName, investmentRequestId)

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

## A3-1135 — PlanTradingRestrictionResponse.scala: Hmm don’t we need different DTO for this? The table columns are different

**Source stance:** open-question

**Context:**

> compliance-api/src/main/scala/com/endowus/silver/compliance/api/responses/hk/queryTradingRestriction/PlanTradingRestrictionResponse.scala; PR: [INV-669] State change impacted plans

**Source-preserving request, proposal, or question:**

> Hmm don’t we need different DTO for this? The table columns are different

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3006 · comment 342247607 · PR 4577 · 2022-11-02

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/responses/hk/queryTradingRestriction/PlanTradingRestrictionResponse.scala`

**Evidence:** anon-2.jsonl:3006 · comment 342247607 · PR 4577 · 2022-11-02

Source path: `compliance-api/src/main/scala/com/endowus/silver/compliance/api/responses/hk/queryTradingRestriction/PlanTradingRestrictionResponse.scala`

**Explicit source context (hunk):**

> +)
> +
> +case class PlanTradingRestrictionResponse(
> +  recurringPlansRequireAcks: List[ImpactedPlanDto] = List(),
> +  tradingBlockedPlans: List[ImpactedPlanDto] = List(),
> +)
> +

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

## A3-1332 — Measure goal-readside lookups before adding local eventually-consistent projections

**Source stance:** suggestion

**Context:**

> compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/InvestmentValueCalculator.scala; PR: [INV-485] feat(compliance): Initial CR validation logic

**Source-preserving request, proposal, or question:**

> This API queries readside table of goal service. We can change to streaming, but should be ok for now?
> 
> All lookup performed here and the CRA class are actually can be done from local DB, if we build the projection. But let’s measure first, before we dive into the eventual consistence hole.

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.
- Streaming/local projections are options; source says measure before adding eventual consistency and currently tolerates goal readside lookup.

**Evidence:** anon-2.jsonl:3217 · comment 330804569 · PR 4189 · 2022-09-15

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/InvestmentValueCalculator.scala`

**Evidence:** anon-2.jsonl:3217 · comment 330804569 · PR 4189 · 2022-09-15

Source path: `compliance-impl/src/main/scala/com/endowus/silver/compliance/impl/logic/hk/cr/InvestmentValueCalculator.scala`

**Explicit source context (hunk):**

> +    taaModificationEarmarks: Map[PlanId, TaaModificationEarmark]
> +  ): Future[Map[RiskLevel, BigDecimal]] = {
> +    for {
> +      allPlanTaas <- queryAllPlanTaas(customerId)
> +      effectivePlanTaas = allPlanTaas.map {
> +        case (planId, currentInstrumentWeights) =>
> +          val effectivePlanTaa = taaModificationEarmarks.get(planId).map(_.instrumentWeights).getOrElse(currentInstrumentWeights)

## A3-1334 — TransactionJdbcRepositoryV2.scala: Just curious, what would be the use case to sort by these uuid?

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala; PR: [WIP] INV-440 transaction database Refactor

**Source-preserving request, proposal, or question:**

> Just curious, what would be the use case to sort by these uuid?

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3219 · comment 331997308 · PR 4236 · 2022-09-21

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala`

**Evidence:** anon-2.jsonl:3219 · comment 331997308 · PR 4236 · 2022-09-21

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala`

**Explicit source context (hunk):**

> +
> +    def multiSort(sort: List[SortBy]): Query[TransactionTableV2, TransactionVo, Seq] =
> +      sort.foldLeft(query) {
> +        case (q, sortOp) =>
> +          sortOp match {
> +            case SortBy("transactionId", SortOrder.Asc)  => q.sortBy(_.transactionId.asc)
> +            case SortBy("transactionId", SortOrder.Desc) => q.sortBy(_.transactionId.desc)

## A3-1335 — TransactionJdbcRepositoryV2.scala: I see this too. But I’m just wondering, as an admin user, why would I ever want to sort by some UUID…

**Source stance:** open-question

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala; PR: [WIP] INV-440 transaction database Refactor

**Source-preserving request, proposal, or question:**

> Yeah I see this too. But I’m just wondering, as an admin user, why would I ever want to sort by some UUID…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3220 · comment 332000275 · PR 4236 · 2022-09-21

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala`

**Evidence:** anon-2.jsonl:3220 · comment 332000275 · PR 4236 · 2022-09-21

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionJdbcRepositoryV2.scala`

**Explicit source context (hunk):**

> +
> +    def multiSort(sort: List[SortBy]): Query[TransactionTableV2, TransactionVo, Seq] =
> +      sort.foldLeft(query) {
> +        case (q, sortOp) =>
> +          sortOp match {
> +            case SortBy("transactionId", SortOrder.Asc)  => q.sortBy(_.transactionId.asc)
> +            case SortBy("transactionId", SortOrder.Desc) => q.sortBy(_.transactionId.desc)

## A3-1412 — MasApiService.scala: Actually why don’t we query repository here…

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiService.scala; PR: fixes fx rate mas parsing issue and daily price fx conversion issue

**Source-preserving request, proposal, or question:**

> Actually why don’t we query repository here…

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3307 · comment 314039996 · PR 3796 · 2022-07-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiService.scala`

**Evidence:** anon-2.jsonl:3307 · comment 314039996 · PR 3796 · 2022-07-06

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/mas/MasApiService.scala`

**Explicit source context (hunk):**

> +            logger.debug(
>                s"cross fx rate [$baseCcy|$quoteCcy] for fxDate [${baseCcyAgainstSgd._1}] has been calculated to be [$crossFxRate], multiplied [$baseCcy|SGD] of [${baseCcyAgainstSgd}] with [SGD|$quoteCcy] of [${sgdAgainstQuoteCcy}]..."
>              )
> +            //not sure why the date of base ccy is taken
>              (baseCcyAgainstSgd._1, crossFxRate)
>            }
>          } yield baseQuote

## A3-1417 — CraManager.scala: I’ll add the Jdbc event processor \+ repository to query for this bit separately… PR is getting too fat now

**Source stance:** explanation

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala; PR: HK CRA changes

**Source-preserving request, proposal, or question:**

> I’ll add the Jdbc event processor \+ repository to query for this bit separately… PR is getting too fat now

**Conditions and limits:**

- Source wording is preserved in requested_change; interrogatives and proposals are not settled answers.
- The component path and PR title identify source context only; merged/resolved status is not evidence of implementation or correctness.
- The hunk evidence is source context; symbols or conditions found only there must not be attributed to the comment.

**Evidence:** anon-2.jsonl:3313 · comment 311998249 · PR 3754 · 2022-06-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Evidence:** anon-2.jsonl:3313 · comment 311998249 · PR 3754 · 2022-06-27

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/managers/hk/CraManager.scala`

**Explicit source context (hunk):**

> +        case Some(state) =>
> +          Future.successful(
> +            CraDetailsResponse(
> +              craQuestionnaireVersion = state.craQuestionnaireVersion,
> +              advisoryProfile = toDto(state.advisoryProfile),
> +              annualIncome = state.annualIncome,
> +              liquidNetWorth = state.liquidNetWorth,

## R-3320 — FYI this one uses Cassandra repository with IN clause. Not sure if anyone would create a FundSmart goal with 25 instruments though

**Source stance:** open-question

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/goalcreate/GoalCreateConfirmationBehaviour.scala; PR 3721: Feat/IA productLine/FundSmartCreate

**Source-preserving request, proposal, or question:**

> FYI [incidental identifier omitted] this one uses Cassandra repository with IN clause. Not sure if anyone would create a FundSmart goal with 25 instruments though

**Conditions and limits:**

- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3320 · comment 313763140 · PR 3721 · 2022-07-05

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/goalcreate/GoalCreateConfirmationBehaviour.scala`

>  this one uses Cassandra repository with IN clause. Not sure if anyone would create a FundSmart goal with 25 instruments though

## R-3367 — Withdrawn EXPLAIN result for instrument_holdings_v1 SUM/MIN join

**Source stance:** reported-verification

**Context:**

> rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/db/jdbc/InstrumentHoldingDaoJdbc.scala; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> This query is translated into
> 
> ```sql
> SELECT
>     x2."plan_id", x2."instrument_id", x2."business_date", x2."ccy", x2."goal_id", x2."customer_id", x2."broker", x2."account_number", x2."market_value", x2."holding_units",
>     x3.x4
> FROM
>     (SELECT "plan_id" AS x5, SUM("market_value") AS x4
>      FROM "rebate"."instrument_holdings_v1"
>      WHERE ((((("broker" = 'UOBKH_SGD_CASH')
>                    AND ("instrument_id" = 'Vargan'))
>                   AND ("business_date" >= ?))
>                  AND ("business_date" <= ?))
>                 AND ("ccy" = 'SGD'))
>        AND ("market_value" >= 0)
>      GROUP BY "plan_id") x3,
> 
>     (SELECT "plan_id" AS x6, MIN("business_date") AS x7
>      FROM "rebate"."instrument_holdings_v1"
>      WHERE ((((("broker" = 'UOBKH_SGD_CASH')
>                    AND ("instrument_id" = 'Vargan'))
>                   AND ("business_date" >= ?))
>                  AND ("business_date" <= ?))
>                 AND ("ccy" = 'SGD'))
>        AND ("market_value" >= 0)
>      GROUP BY "plan_id") x8,
> 
>     "rebate"."instrument_holdings_v1" x2
> 
> WHERE
>     ((((((((x2."broker" = 'UOBKH_SGD_CASH')
>                AND (x2."instrument_id" = 'Vargan'))
>               AND (x2."business_date" >= ?))
>              AND (x2."business_date" <= ?))
>             AND (x2."ccy" = 'SGD'))
>            AND (x2."market_value" >= 0))
>           AND (x2."plan_id" = x8.x6))
>          AND (x2."business_date" = x8.x7))
>         AND (x2."plan_id" = x3.x5)
> ```
> 
> ‌
> 
> ~~Query analysis looks ok, with correct index being used~~
> 
> ```
> Hash Join  (cost=2325.98..3477.82 rows=1 width=134) (actual time=0.198..0.200 rows=0 loops=1)
>   Hash Cond: ((x2.plan_id = instrument_holdings_v1_1.plan_id) AND (x2.business_date = (min(instrument_holdings_v1_1.business_date))))
>   ->  Hash Join  (cost=1163.27..2315.09 rows=4 width=150) (never executed)
>         Hash Cond: (x2.plan_id = x3.x5)
>         ->  Index Scan using instrument_holdings_v1_instrument_id_broker_id_business_date_pl on instrument_holdings_v1 x2  (cost=0.56..1151.66 rows=278 width=102) (never executed)
>               Index Cond: (((instrument_id)::text = 'Vargan'::text) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND (business_date >= '2021-10-01'::date) AND (business_date <= '2021-12-31'::date) AND ((ccy)::text = 'SGD'::text))
>               Filter: (market_value >= '0'::numeric)
>         ->  Hash  (cost=1159.26..1159.26 rows=276 width=48) (never executed)
>               ->  Subquery Scan on x3  (cost=1153.05..1159.26 rows=276 width=48) (never executed)
>                     ->  HashAggregate  (cost=1153.05..1156.50 rows=276 width=48) (never executed)
>                           Group Key: instrument_holdings_v1.plan_id
>                           ->  Index Scan using instrument_holdings_v1_instrument_id_broker_id_business_date_pl on instrument_holdings_v1  (cost=0.56..1151.66 rows=278 width=22) (never executed)
>                                 Index Cond: (((instrument_id)::text = 'Vargan'::text) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND (business_date >= '2021-10-01'::date) AND (business_date <= '2021-12-31'::date) AND ((ccy)::text = 'SGD'::text))
>                                 Filter: (market_value >= '0'::numeric)
>   ->  Hash  (cost=1158.57..1158.57 rows=276 width=20) (actual time=0.149..0.149 rows=0 loops=1)
>         Buckets: 1024  Batches: 1  Memory Usage: 8kB
>         ->  HashAggregate  (cost=1153.05..1155.81 rows=276 width=20) (actual time=0.149..0.149 rows=0 loops=1)
>               Group Key: instrument_holdings_v1_1.plan_id
>               ->  Index Scan using instrument_holdings_v1_instrument_id_broker_id_business_date_pl on instrument_holdings_v1 instrument_holdings_v1_1  (cost=0.56..1151.66 rows=278 width=20) (actual time=0.146..0.146 rows=0 loops=1)
>                     Index Cond: (((instrument_id)::text = 'Vargan'::text) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND (business_date >= '2021-10-01'::date) AND (business_date <= '2021-12-31'::date) AND ((ccy)::text = 'SGD'::text))
>                     Filter: (market_value >= '0'::numeric)
> Planning Time: 1.086 ms
> Execution Time: 0.399 ms
> ```
> 
> ‌
> 
> ^ Wrong query analysis. See below

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3367 · comment 296868673 · PR 3438 · 2022-04-25

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/db/jdbc/InstrumentHoldingDaoJdbc.scala`

## R-3368 — Historical allocation/time comparison: in-memory versus DB holding aggregation at parallelism 4

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> Created [<url> data-inline-card='' } following method 1
> 
> ‌
> 
> Memory usage wise it’s working well. It uses more memory, since we are aggregating plan’s MV in logic \(instead of DB\), but we can control how much by adjusting the mapAsync parallelism.
> 
> With parallelism = 4:
> 
> |  | **from\_date** | **Memory allocation rate** | **Time taken** |
> | --- | --- | --- | --- |
> | Aggregate in memory | 2021-10-01 | ~100MB/s | ~155s |
> |  | 2021-01-01 | ~100MB/s | ~1,080s |
> | Aggregate in DB | 2021-10-01 | ~10MB/s | ~2s |
> |  | 2021-01-01 | ~10MB/s | ~15s |
> 
> ‌
> 
> In terms of time, it’s clear that using DB aggregate functions is faster, but I’m not sure if it can cope when we have more plans \(hence the suggestion to in method 1 to find the planIds only\)
> 
> In staging, with from\_date = 2021-01-01
> 
> * query with SUM \+ MIN aggregate function would take ~15s
> * query with DISTINCT plan would take ~6s, and afterwards, we would issue as many queries as plan count to get holdings per plan \(but these are all key fields, so should be fast\)
> 
> ‌

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3368 · comment 297114159 · PR 3438 · 2022-04-26

## R-3369 — Corrected holdings EXPLAIN uses two roughly seven-second parallel sequential scans

**Source stance:** explanation

**Context:**

> rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/db/jdbc/InstrumentHoldingDaoJdbc.scala; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> I realized I executed explain analyse for wrong query previously. The correct analysis does not look too great
> 
> ```
> Merge Join  (cost=3249878.82..3407363.96 rows=108816 width=134) (actual time=15379.153..15464.994 rows=5966 loops=1)
>   Merge Cond: (x2.plan_id = instrument_holdings_v1_1.plan_id)
>   ->  Nested Loop  (cost=1624917.95..1777634.18 rows=1252 width=118) (actual time=7535.609..7599.196 rows=5966 loops=1)
>         ->  Finalize GroupAggregate  (cost=1624917.39..1629322.89 rows=17389 width=20) (actual time=7535.558..7546.409 rows=5966 loops=1)
>               Group Key: instrument_holdings_v1.plan_id
>               ->  Gather Merge  (cost=1624917.39..1628975.11 rows=34778 width=20) (actual time=7535.541..7541.183 rows=17881 loops=1)
>                     Workers Planned: 2
>                     Workers Launched: 2
>                     ->  Sort  (cost=1623917.37..1623960.84 rows=17389 width=20) (actual time=7530.338..7531.447 rows=5960 loops=3)
>                           Sort Key: instrument_holdings_v1.plan_id
>                           Sort Method: quicksort  Memory: 658kB
>                           Worker 0:  Sort Method: quicksort  Memory: 658kB
>                           Worker 1:  Sort Method: quicksort  Memory: 658kB
>                           ->  Partial HashAggregate  (cost=1622518.78..1622692.67 rows=17389 width=20) (actual time=7525.509..7527.290 rows=5960 loops=3)
>                                 Group Key: instrument_holdings_v1.plan_id
>                                 ->  Parallel Seq Scan on instrument_holdings_v1  (cost=0.00..1620104.33 rows=482889 width=20) (actual time=0.057..7210.369 rows=579172 loops=3)
>                                       Filter: ((business_date >= '2021-01-01'::date) AND (business_date <= '2021-12-31'::date) AND (market_value >= '0'::numeric) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND ((instrument_id)::text = 'IE00BF20LB02'::text) AND ((ccy)::text = 'SGD'::text))
>                                       Rows Removed by Filter: 18646832
>         ->  Index Scan using instrument_holdings_v1_instrument_id_broker_id_business_date_pl on instrument_holdings_v1 x2  (cost=0.56..8.52 rows=1 width=102) (actual time=0.008..0.008 rows=1 loops=5966)
>               Index Cond: (((instrument_id)::text = 'IE00BF20LB02'::text) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND (business_date = (min(instrument_holdings_v1.business_date))) AND (business_date >= '2021-01-01'::date) AND (business_date <= '2021-12-31'::date) AND (plan_id = instrument_holdings_v1.plan_id) AND ((ccy)::text = 'SGD'::text))
>               Filter: (market_value >= '0'::numeric)
>   ->  Finalize GroupAggregate  (cost=1624960.86..1629496.78 rows=17389 width=48) (actual time=7843.537..7862.449 rows=5966 loops=1)
>         Group Key: instrument_holdings_v1_1.plan_id
>         ->  Gather Merge  (cost=1624960.86..1629018.58 rows=34778 width=48) (actual time=7843.514..7849.588 rows=17879 loops=1)
>               Workers Planned: 2
>               Workers Launched: 2
>               ->  Sort  (cost=1623960.84..1624004.31 rows=17389 width=48) (actual time=7837.487..7838.726 rows=5960 loops=3)
>                     Sort Key: instrument_holdings_v1_1.plan_id
>                     Sort Method: quicksort  Memory: 1030kB
>                     Worker 0:  Sort Method: quicksort  Memory: 1030kB
>                     Worker 1:  Sort Method: quicksort  Memory: 1031kB
>                     ->  Partial HashAggregate  (cost=1622518.78..1622736.14 rows=17389 width=48) (actual time=7828.709..7833.764 rows=5960 loops=3)
>                           Group Key: instrument_holdings_v1_1.plan_id
>                           ->  Parallel Seq Scan on instrument_holdings_v1 instrument_holdings_v1_1  (cost=0.00..1620104.33 rows=482889 width=22) (actual time=0.068..7393.723 rows=579172 loops=3)
>                                 Filter: ((business_date >= '2021-01-01'::date) AND (business_date <= '2021-12-31'::date) AND (market_value >= '0'::numeric) AND ((broker)::text = 'UOBKH_SGD_CASH'::text) AND ((instrument_id)::text = 'IE00BF20LB02'::text) AND ((ccy)::text = 'SGD'::text))
>                                 Rows Removed by Filter: 18646832
> Planning Time: 0.701 ms
> Execution Time: 15466.966 ms
> ```
> 
> ‌
> 
> Table is “parallel seq scan”-ed 2 times - each takes 7s \(hence total ~15s\), without using index

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3369 · comment 297130273 · PR 3438 · 2022-04-26

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/db/jdbc/InstrumentHoldingDaoJdbc.scala`

## R-3370 — Holdings index use differs between all-plan grouped and specific-plan queries

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> Updated the query analysis here [<url> data-inline-card='' }
> 
> But basically, when querying with broker, instrument, ccy and date range, with group by on planId: it uses parallel seq scan, no index used \(affect both approaches\)
> 
> ‌
> 
> When query with broker, instrument, ccy, date range and specific plan: it uses index created on the composite keys

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3370 · comment 297134997 · PR 3438 · 2022-04-26

## R-3371 — October and January date ranges lead PostgreSQL to choose different scan plans

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> So it turns out that PG would switch to use sequential scan, instead of using index, if it \(somehow\) expects more rows to be returned \(I read [<url> data-inline-card='' } \)
> 
> ‌
> 
> In the above case:
> 
> * when querying with from\_date = 2021-10-01, both SUM \+ MIN and DISTINCT plans queries use index
> * when querying with from\_date = 2021-01-01, both use seq scan
> 
> So pg is doing its thing, and not an issue on our side.

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3371 · comment 297392128 · PR 3438 · 2022-04-27

## R-3372 — There were 2144 hits of this warn log in Kibana in last distribution. Isn’t it too high to be Trade Ops mistake? Nevertheless, monitoring if any probably s

**Source stance:** open-question

**Context:**

> rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/DistributionCalculator.scala; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> There were 2144 hits of this warn log in Kibana in last distribution. Isn’t it too high to be Trade Ops mistake?
> 
> Nevertheless, monitoring if any probably should happen upstream, like timeseries service itself, rather than rebate - which is only run quarterly?

**Evidence:** anon-2.jsonl:3372 · comment 297394232 · PR 3438 · 2022-04-27

Source path: `rebate-impl/src/main/scala/com/endowus/silver/rebate/impl/entities/distribution/processors/DistributionCalculator.scala`

## R-3373 — Metrics of both approaches observed using [<url> ‌ I think I’m going with the approach in this PR, even though it’s tightly fit to the rebate distribution 

**Source stance:** explanation

**Context:**

> General PR discussion; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> Metrics of both approaches observed using [<url>
> 
> ‌
> 
> I think I’m going with the approach in this PR, even though it’s tightly fit to the rebate distribution purpose, and unlikely to be reuse for anything else. [incidental identifier omitted] [incidental identifier omitted]
> 
> ![](<url>
> ‌

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3373 · comment 297455850 · PR 3438 · 2022-04-27

> Metrics of both approaches observed using [<url>
> 
> ‌
> 
> I think I’m going with the approach in this PR, even though it’s tightly fit to the rebate distribution purpose, and unlikely to be reuse for anything else. 

**Evidence:** anon-2.jsonl:3373 · comment 297455850 · PR 3438 · 2022-04-27

> 
> 
> ![](<url>
> ‌

## R-3374 — Oops my bad: * Red and green box is approach in [<url> data-inline-card='' } , triggered with fromDate = 2021-10-01 \(not so much holding data\) and 2021-0

**Source stance:** reported-verification

**Context:**

> General PR discussion; PR 3438: [IAO-133,IAO-158,IAO-135]: Switch logic to aggregate plan MV to DB

**Source-preserving request, proposal, or question:**

> Oops my bad:
> 
> * Red and green box is approach in [<url> data-inline-card='' } , triggered with fromDate = 2021-10-01 \(not so much holding data\) and 2021-01-01 \(a lot holding data\)
> * Pink and blue box is approach in this PR, also triggered with fromDate = 2021-10-01 and 2021-01-01
> 
> ‌

**Conditions and limits:**

- PR3438 discussion: the first EXPLAIN analysis is explicitly withdrawn. Corrected plans and date-range-dependent index/seq-scan behavior follow. Measurements are historical observations, not a performance guarantee. Source rows: anon-2.jsonl:3367, anon-2.jsonl:3368, anon-2.jsonl:3369, anon-2.jsonl:3370, anon-2.jsonl:3371, anon-2.jsonl:3373, anon-2.jsonl:3374.

**Evidence:** anon-2.jsonl:3374 · comment 297460282 · PR 3438 · 2022-04-27

## R-3410 — Reset version since we rename to follow standard naming convention: * using singular noun for table names * using `tableName_pk_v` for pk ‌

**Source stance:** requested-change

**Context:**

> transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionTable.scala; PR 3265: IAO changes for FX admin

**Source-preserving request, proposal, or question:**

> Reset version since we rename to follow standard naming convention:
> 
> * using singular noun for table names
> 
> * using `tableName_pk_v` for pk
> 
> ‌

**Evidence:** anon-2.jsonl:3410 · comment 289211443 · PR 3265 · 2022-03-22

Source path: `transaction-impl/src/main/scala/com/endowus/silver/transaction/impl/db/jdbc/TransactionTable.scala`

## R-3443 — Number of rows play a part, but main reason why select without where condition is slow because it needs to jump multiple nodes to get all data - these netw

**Source stance:** observed-defect

**Context:**

> advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala; PR 2780: Feat/advisory jdbc

**Source-preserving request, proposal, or question:**

> Number of rows play a part, but main reason why select without where condition is slow because it needs to jump multiple nodes to get all data - these network hops are the culprit.  
>   
> And that doesn’t matter if you have 80 rows or 1M rows…
> 
> ‌

**Evidence:** anon-2.jsonl:3443 · comment 268972138 · PR 2780 · 2021-12-22

Source path: `advisory-impl/src/main/scala/com/endowus/silver/advisory/impl/entities/portfolio/db/repository/ProductPortfolioRepository.scala`

## R-3446 — StatementRepository IN-clause comment is conditional on customerId clustering-key placement

**Source stance:** explanation

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/StatementRepository.scala; PR 3217: moves to generate metadata separately

**Source-preserving request, proposal, or question:**

> FYI using IN clause only works if customerId is clustering key, not partition key

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3446 · comment 286837031 · PR 3217 · 2022-03-11

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/statement/db/StatementRepository.scala`

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

## R-3481 — I have one side question. This DB handler is not tied to any event processor, so we have to call `handler.createTables` here. If there is a readside event 

**Source stance:** open-question

**Context:**

> report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala; PR 3038: SILVER-11957: Fix auto creation of report table

**Source-preserving request, proposal, or question:**

> I have one side question. This DB handler is not tied to any event processor, so we have to call `handler.createTables` here.
> 
> If there is a readside event processor, we could also call this as part of the global prepare.
> 
> Is there any preference / difference between them?

**Evidence:** anon-2.jsonl:3481 · comment 280642865 · PR 3038 · 2022-02-17

Source path: `report-impl/src/main/scala/com/endowus/silver/report/impl/ReportApplication.scala`

## R-3489 — Would `filter().result.headOption` be enough?

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/plan/PlanProfileDaoJdbc.scala; PR 3059: Feat/SILVER-11759 jdbc readside plan mv

**Source-preserving request, proposal, or question:**

> Would `filter().result.headOption` be enough?

**Conditions and limits:**

- The result.headOption suggestion is followed by recognition that take(1) remains in the query and becomes LIMIT 1; the later response prefers the existing take(1) approach. Source rows: anon-2.jsonl:3489, anon-2.jsonl:3490.
- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3489 · comment 280645232 · PR 3059 · 2022-02-17

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/plan/PlanProfileDaoJdbc.scala`

## R-3490 — take(1) translates to LIMIT 1, correcting the earlier result.headOption suggestion

**Source stance:** reported-verification

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/plan/PlanProfileDaoJdbc.scala; PR 3059: Feat/SILVER-11759 jdbc readside plan mv

**Source-preserving request, proposal, or question:**

> [incidental identifier omitted] Ah ok I was confused. `take(1)` is still query API, so it would translate to `LIMIT 1` in actual query. So this is better :thumbsup: 

**Conditions and limits:**

- The result.headOption suggestion is followed by recognition that take(1) remains in the query and becomes LIMIT 1; the later response prefers the existing take(1) approach. Source rows: anon-2.jsonl:3489, anon-2.jsonl:3490.
- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3490 · comment 280661395 · PR 3059 · 2022-02-17

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/plan/PlanProfileDaoJdbc.scala`

>  Ah ok I was confused. `take(1)` is still query API, so it would translate to `LIMIT 1` in actual query. So this is better :thumbsup: 

## R-3515 — Historical question about TestContainers versus EmbeddedPostgres and in-memory tests

**Source stance:** open-question

**Context:**

> General PR discussion; PR 2962: TestContainer Trial

**Source-preserving request, proposal, or question:**

> Are we planning to make use of TestContainers for full fledge e2e integration tests, in which DB state is shared between tests? Otherwise I’m not sure if it’s worth the trouble just to test Postgres related pieces.
> 
> If we trust Slick, we should already be agnostic to the underlying database, and hence can potentially use another DB driver that supports in-memory for unit tests, instead of EmbeddedPostgres. If we don’t trust, then we should just write tests to explicitly test Slick, without repository logic.
> 
> ‌

**Conditions and limits:**

- The TestContainers/EmbeddedPostgres discussion is historical and the concern is followed by acceptance of the clarification. It is not a blanket rejection of database integration tests. Source rows: anon-2.jsonl:3515, anon-2.jsonl:3516.

**Evidence:** anon-2.jsonl:3515 · comment 276984427 · PR 2962 · 2022-02-03

## R-3519 — typo: `indexName` Could we also explain why we need this, and cannot use existing `createIndexIfNotExists` that uses slick?

**Source stance:** open-question

**Context:**

> jdbc-commons/src/main/scala/com/endowus/jdbc/slick/postgres/ExtendedPostgresProfile.scala; PR 2896: adds indices for making charge performant

**Source-preserving request, proposal, or question:**

> typo: `indexName`
> 
> Could we also explain why we need this, and cannot use existing `createIndexIfNotExists` that uses slick?

**Evidence:** anon-2.jsonl:3519 · comment 273947618 · PR 2896 · 2022-01-20

Source path: `jdbc-commons/src/main/scala/com/endowus/jdbc/slick/postgres/ExtendedPostgresProfile.scala`

## R-3520 — Postgres has this naming convention apparently ``` {tablename}_{columnname(s)}_{suffix} ```

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvTable.scala; PR 2896: adds indices for making charge performant

**Source-preserving request, proposal, or question:**

> Postgres has this naming convention apparently
> ```
> {tablename}_{columnname(s)}_{suffix}
> ```

**Evidence:** anon-2.jsonl:3520 · comment 273951635 · PR 2896 · 2022-01-20

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvTable.scala`

## R-3521 — Maybe rename this method to `fixIfNotExistsStatement` or something along that line? Same in `PlanProfileJdbcTable`

**Source stance:** suggestion

**Context:**

> charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvTable.scala; PR 2896: adds indices for making charge performant

**Source-preserving request, proposal, or question:**

> Maybe rename this method to `fixIfNotExistsStatement` or something along that line?
> 
> Same in `PlanProfileJdbcTable`

**Evidence:** anon-2.jsonl:3521 · comment 273953214 · PR 2896 · 2022-01-20

Source path: `charge-impl/src/main/scala/com/endowus/silver/charge/impl/db/mv/jdbc/DailyMvTable.scala`

## R-3551 — It’s actually recommended to use `NetworkTopologyStrategy` even for local \(with only one DC configured\). But I guess not too important for this PR

**Source stance:** suggestion

**Context:**

> conf-reference/src/main/resources/local/env.conf; PR 2726: D2/SILVER-9967 support dynamic env

**Source-preserving request, proposal, or question:**

> It’s actually recommended to use `NetworkTopologyStrategy` even for local \(with only one DC configured\). But I guess not too important for this PR

**Evidence:** anon-2.jsonl:3551 · comment 270856515 · PR 2726 · 2022-01-05

Source path: `conf-reference/src/main/resources/local/env.conf`

## R-3553 — You can run `NetworkTopologyStrategy` with single node. And it will work fine too. And this will make it easy if we want to increase number of nodes later.

**Source stance:** suggestion

**Context:**

> conf-reference/src/main/resources/local/env.conf; PR 2726: D2/SILVER-9967 support dynamic env

**Source-preserving request, proposal, or question:**

> You can run `NetworkTopologyStrategy` with single node. And it will work fine too.
> 
> And this will make it easy if we want to increase number of nodes later. Testing within a multi-node cluster is very important if we have special query / write pattern.
> 
> This is minor in scope of this PR btw :thumbsup: 

**Evidence:** anon-2.jsonl:3553 · comment 272165839 · PR 2726 · 2022-01-12

Source path: `conf-reference/src/main/resources/local/env.conf`

## R-3555 — I think it’s better to let consumer\(s\) have to chance to decide what to do with missing data - rather than throwing

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcRepository.scala; PR 2807: Feat/projection svc portfolio stats jdbc

**Source-preserving request, proposal, or question:**

> I think it’s better to let consumer\(s\) have to chance to decide what to do with missing data - rather than throwing

**Evidence:** anon-2.jsonl:3555 · comment 270149129 · PR 2807 · 2021-12-30

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcRepository.scala`

## R-3556 — If you prefer Exception instead, because say you expect caller to always call with valid ID… then code is little cleaner to read if we return Future.failed

**Source stance:** open-question

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcRepository.scala; PR 2807: Feat/projection svc portfolio stats jdbc

**Source-preserving request, proposal, or question:**

> If you prefer Exception instead, because say you expect caller to always call with valid ID… then code is little cleaner to read if we return Future.failed\(NotFound\(\)\)

**Evidence:** anon-2.jsonl:3556 · comment 270149593 · PR 2807 · 2021-12-30

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/db/jdbc/portfolioStats/PortfolioStatsJdbcRepository.scala`

## R-3558 — Portfolio stats exact-ID lookup and filter lookup both produce a List response

**Source stance:** suggestion

**Context:**

> projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala; PR 2807: Feat/projection svc portfolio stats jdbc

**Source-preserving request, proposal, or question:**

> Maybe something like this?
> 
> ```scala
> for {
>   stats <- (portfolioId, effectiveDate, statsCcy) match {
>     case (Some(pid), Some(date), Some(ccy)) => portfolioStatsJdbcRepository.findById(pid, date, ccy).map(_.toSeq)
>     case _ => portfolioStatsJdbcRepository.findByFilter(portfolioId, effectiveDate, statsCcy)
>   }
> } yield stats.map(PortfolioStats.toDto).toList
> ```
> 
> ‌

**Evidence:** anon-2.jsonl:3558 · comment 270161114 · PR 2807 · 2021-12-30

Source path: `projection-impl/src/main/scala/com/endowus/silver/projection/impl/ProjectionServiceImpl.scala`

## R-3561 — Nit: Do we want `v%d` instead?

**Source stance:** suggestion

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/fx/db/FxRateTable.scala; PR 2790: Feat/SILVER-10779 multiccy monthly changes

**Source-preserving request, proposal, or question:**

> Nit: Do we want `v%d` instead?

**Conditions and limits:**

- This is a short source statement; its complete referent may depend on the historical diff or surrounding thread. Do not infer a missing requirement.

**Evidence:** anon-2.jsonl:3561 · comment 269632426 · PR 2790 · 2021-12-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/fx/db/FxRateTable.scala`

## R-3562 — I think mentioned not to use this syntax in the PR for advisory..

**Source stance:** open-question

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/fx/db/FxRateTable.scala; PR 2790: Feat/SILVER-10779 multiccy monthly changes

**Source-preserving request, proposal, or question:**

> I think [incidental identifier omitted] mentioned not to use this syntax in the PR for advisory..

**Conditions and limits:**

- Only incidental reviewer mentions and customer/account UUID literals are omitted in the displayed source wording; symbols, predicates, dates, thresholds, and alternatives are retained.

**Evidence:** anon-2.jsonl:3562 · comment 269632747 · PR 2790 · 2021-12-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/fx/db/FxRateTable.scala`

>  mentioned not to use this syntax in the PR for advisory..

## R-3576 — Yup, that’s correct. Apparent this table was manually updated in all environment without committing back to source code. ‌ See [<url> data-inline-card='' }

**Source stance:** reported-verification

**Context:**

> marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangeDbHandler.scala; PR 2788: Feat/SILVER-10999 recalculate portfolio

**Source-preserving request, proposal, or question:**

> Yup, that’s correct. Apparent this table was manually updated in all environment without committing back to source code.
> 
> ‌
> 
> See [<url> data-inline-card='' } 

**Evidence:** anon-2.jsonl:3576 · comment 269597542 · PR 2788 · 2021-12-27

Source path: `marketdata-impl/src/main/scala/com/endowus/silver/marketdata/impl/entities/instrument/db/monthlyChanges/InstrumentMonthlyChangeDbHandler.scala`

